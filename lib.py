from mido import MetaMessage, Message, MidiFile, MidiTrack
import numpy.random as rd
import midi2audio as m2a
from pydub.playback import play
from pydub import AudioSegment


def char2note(char):
    """Convert a char to a midi note number wih the followung syntax. First
    the note ('a', 'b' , etc..) then the number of the note, and finally
    it's accentuation ('-', '=', '+')."""
    if char == 's':  # Return a silence
        return 1, 0, 0
    notes = {'a': 69, 'b': 71, 'c': 60, 'd': 62, 'e': 64, 'f': 65, 'g': 67}
    note_nb = notes[char[0]]
    note_nb += (int(char[1])-4) * 12
    if len(char) == 3:
        if char[2] == '-':
            note_nb -= 1
        if char[2] == '+':
            note_nb += 1
    v_on = 64
    v_off = 100
    return note_nb, v_on, v_off


def notes2trk(trk, notes, bck_n=('s', 0)):
    """Add notes to a track the notes have a particular syntax. for instance
    [('c4 e4 g4', 3*430), [('c4', 430), ('s', 430), ('g4', 430)]] """

    bck_list = bck_n[0].split(' ')
    for bck_c_n in bck_list:  # Add the note on message
        if bck_c_n == 's':
            trk.append(Message("note_on", note=0, velocity=0, time=0))
            trk.append(Message("note_off", note=0, velocity=0, time=bck_n[1]))
        else:
            n_nb, v_on, v_off = char2note(bck_c_n)
            trk.append(Message("note_on", note=n_nb, velocity=v_on, time=0))

    time = 0
    for i, note in enumerate(notes):
        if i + 1 < len(notes):
            if isinstance(notes[i+1], list):
                trk = notes2trk(trk, notes[i+1], bck_n = notes[i])
                continue

        if isinstance(note, list):
            continue

        if note == 's':
            trk.append(Message("note_on", note=0, velocity=0, time=0))
            trk.append(Message("note_off", note=0, velocity=0, time=note[1]))
            time += note[1]
            continue

        nlist = note[0].split(' ')

        for c_n in nlist:  # Add the note on message
            n_nb, v_on, v_off = char2note(c_n)
            trk.append(Message("note_on", note=n_nb, velocity=v_on, time=0))

        time += note[1]
        trk.append(Message("note_off", note=n_nb, velocity=v_off,
                           time=note[1]))
        for c_n in nlist[:-1]:  # Add the note off message
            n_nb, v_on, v_off = char2note(c_n)
            trk.append(Message("note_off", note=n_nb, velocity=v_off,
                               time=0))
        if time == bck_n[1]:
            for bck_c_n in bck_list:
                n_nb, v_on, v_off = char2note(bck_c_n)
                trk.append(Message("note_off", note=n_nb, velocity=v_off,
                                   time=0))

    return trk



def vel_r(track, t_vels, r):
    """Randomly change the velocity of a note in a track"""
    time = 0
    i = 0
    for msg in track:
        print(time)
        if msg.type == 'note_on':
            if msg.velocity != 0:  # To avoid messing with certain mid
                if time >= t_vels[i][1]:
                    i += 1
                    time = 0
                t_vel = t_vels[i][0]
                r_mod = t_vel*r
                msg.velocity = rd.randint(max(t_vel - r_mod, 0),
                                          min(t_vel + r_mod, 127))
        if msg.type=='note_off':
            time += msg.time
    return track


def pedal_r(mid, nbt, nmeas, add=0):
    """Play the pedal every n beat starting with the pedal on"""
    bt = mid.ticks_per_beat
    trk = MidiTrack()
    trk.name = "Pedal"
    p_on = rd.randint(64, 127)
    p_off = rd.randint(64, 127)
    trk.append(Message("control_change", control=64, value=p_on, time=add))
    for i in range(nmeas):
        p_off = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_off,
                           time=bt*nbt))
        p_on = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_on))
    mid.tracks.append(trk)
    return mid




def tempo_r(mid, beats, rs):
    """Create a new track with randomly varying tempo"""
    bt = mid.ticks_per_beat
    trk = MidiTrack()
    trk.name = "Tempo variation"
    trk.append(MetaMessage("set_tempo",
                           tempo=beats[0],
                           time=0))

    for i, beat in enumerate(beats):
        r = rs[i]
        if r == 0:  # For the deterministic case
            tempo_r = beat
        else:
            tempo_r = rd.randint(beat-int(beat*r), beat + int(beat*r)) + 1
        trk.append(MetaMessage("set_tempo",
                               time=bt,
                               tempo=tempo_r))

    mid.tracks.append(trk)
    return mid


def add_notes(trk, notes, dur):
    """DEPRECATED Add notes to a track"""
    for i, ns in enumerate(notes):
        if type(ns) is not list:
            return "notes must be a list of lists"

        d = dur[i]
        for n in ns:
            if n == -1:
                trk.append(Message("note_on", note=0, velocity=0, time=0))
            else:
                trk.append(Message("note_on", note=n, velocity=100, time=0))

        if len(ns) >= 2:
            for i, n in enumerate(ns):
                if i > 0:
                    trk.append(Message("note_off", note=n, velocity=64,
                                       time=0))
                else:
                    trk.append(Message("note_off", note=n, velocity=64,
                                       time=d))

        else:
            for n in ns:
                if n == -1:
                    trk.append(Message("note_off", note=0, velocity=0, time=d))
                else:
                    trk.append(Message("note_off", note=n, velocity=64,
                                       time=d))
    return trk


def add_couples(trk, main_notes, notes, dur):
    """DEPRECATED Add notes while another is played in the background"""
    if type(main_notes) is not list:
        return "main_notes must be a list"
    for m_n in main_notes:
        trk.append(Message("note_on", note=m_n, velocity=100, time=0))

    trk = add_notes(trk, notes, dur)

    for m_n in main_notes:
        trk.append(Message("note_off", note=m_n, velocity=64, time=0))

    return trk


def velocity_r(track, t_vel, r):
    """DEPRECATED Randomly change the velocity of a note in a track"""
    time = 0
    for msg in track:
        if msg.type == 'note_on' or msg.type=='note_off':
            time += msg.time
        if msg.type == 'note_on':
            if msg.velocity != 0:  # To avoid messing with certain mid
                r_mod = t_vel*r
                msg.velocity = rd.randint(max(t_vel - r_mod, 0),
                                          min(t_vel + r_mod, 127))
    return track


def volume(mid, vols):
    """Change the volume of a midi"""
    bt = mid.ticks_per_beat
    trk = MidiTrack()
    trk.name = "Volume variation"
    trk.append(Message("control_change",
                       control=7,
                       time=0,
                       value=vols[0]))

    for i, vol in enumerate(vols):
        trk.append(Message("control_change",
                           control=7,
                           time=bt,
                           value=vol))

    mid.tracks.append(trk)
    return mid


def mid2aud(n_mid):
    """Return an audio segment from a mid file and build a wav meanwhile"""
    m2a.FluidSynth().midi_to_audio(n_mid + '.mid',
                                   n_mid + '.wav')
    seg = AudioSegment.from_file(n_mid + '.wav')
    return seg


def interpret(mid, beats, rs, vols, ts_vol=[]):
    """Interpret a given midi, record and play the associated mid file"""
    mid = tempo_r(mid, beats, rs)
    for t_vol in ts_vol:
        mid.tracks[t_vol[0]] = velocity_r(mid.tracks[t_vol[0]],
                                          t_vol[1], rs[0])
    mid = volume(mid, vols)
    return mid


def mid_play(mid, mid_name):
    """Play a mid file and eventually save it"""
    mid.save(mid_name + ".mid")
    out = mid2aud(mid_name)
    out.export(mid_name + ".wav")
    play(out)
    return mid


def compo_test():
    """Generate the midi file to test the different function"""
    mid = MidiFile()
    track = MidiTrack()
    beat = mid.ticks_per_beat
    for i in range(2):
        track.append(Message('note_on', velocity=100, note=60))
        track.append(Message('note_off', velocity=64, note=60, time=beat))
        track.append(Message('note_on', velocity=100, note=60))
        track.append(Message('note_on', velocity=0, note=60, time=beat))
    mid.tracks.append(track)
    return mid

    mid = MidiFile()
    track = MidiTrack()
    beat = mid.ticks_per_beat
    for i in range(2):
        track.append(Message('note_on', velocity=100, note=60))
        track.append(Message('note_off', velocity=64, note=60, time=beat))
        track.append(Message('note_on', velocity=100, note=60))
        track.append(Message('note_on', velocity=0, note=60, time=beat))
    mid.tracks.append(track)


if __name__ == "__main__":
    mid = compo_test()
    trk = MidiTrack()
    beats_int = [500000, 500000]
    rs = [0.1, 0.1]
    ts_vol = [(0, 50)]
    vols = [100, 100]
    notes = [('c4 e4 g4', 3*430), [('c4', 860), [('s', 430), ('g4', 430)]],
             ('c4', 430)]
    trk =  notes2trk(trk, notes)
    for msg in trk:
        print(msg)
    #mid_play(mid, "test")
