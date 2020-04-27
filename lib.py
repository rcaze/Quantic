from mido import MetaMessage, Message, MidiFile, MidiTrack
import numpy.random as rd
import midi2audio as m2a
from pydub.playback import play
from pydub import AudioSegment
import itertools

def rand_ev(low, high, nstp, stp=3, seed=None, inc=True, dec=True):
    """Generate the random size"""
    if not seed:
        seed = rd.randint(low, high)

    rands = [seed]
    for i in range(nstp-1):
        if 0 == rd.randint(2):
            if inc:
                seed += stp
            else:
                seed += 0
        else:
            if dec:
                seed -= stp
            else:
                seed += 0

        if seed < low:
            rands += [low]
        elif seed > high:
            rands += [high]
        else:
            rands += [seed]

    return rands


def char2note(char):
    """Convert a char to a midi note number wih the followung syntax. First
    the note ('a', 'b' , etc..) then the number of the note, and finally
    it's accentuation ('-', '=', '+')."""
    if char == 's':  # Return a silence
        return 0, 0, 0
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


def notes2trk(notes):
    """Create a track from notes with a particular syntax. for instance     [('c4 e4 g4', 3*430, 90), [('c4', 430), ('s', 430), ('g4', 430)]] """

    trk = MidiTrack()

    for i, note in enumerate(notes):
        if note[0] == 's':  # Message for a silence
            trk.append(Message("note_on", note=0, velocity=0, time=0))
            trk.append(Message("note_off", note=0, velocity=0, time=note[1]))
            continue

        nlist = note[0].split(' ')

        for c_n in nlist:  # Add the note on message
            n_nb, v_on, v_off = char2note(c_n)
            if len(note)==2:
                trk.append(Message("note_on", note=n_nb, velocity=v_on, time=0))
            else:
                trk.append(Message("note_on", note=n_nb, velocity=note[2],
                                   time=0))
        if len(note) == 4:
            trk.append(Message("note_off", note=n_nb, velocity=v_off,
                               time=note[1]))
        else:
            trk.append(Message("note_off", note=n_nb, velocity=v_off,
                               time=note[1]))
        for c_n in nlist[:-1]:  # Add the note off message
            n_nb, v_on, v_off = char2note(c_n)
            if len(note) == 4:  # For short note
                trk.append(Message("note_off", note=n_nb, velocity=note[3],
                                   time=0))
            else:
                trk.append(Message("note_off", note=n_nb, velocity=v_off,
                                   time=0))

    return trk








def repeat_vel(vel, nb):
    """Repeat a velocity to match track from the same hand"""
    out = list(itertools.chain.from_iterable(itertools.repeat(x, nb) for x in vel))
    return out


def velocity(vel_init, nuance, notes,
             offset=0, drift=2, cresc=False, decresc=False, acc=[]):
    """Generate a drifting velocity within a given range"""
    vel = [vel_init]
    nuance = [max(0, nuance[0]-offset), nuance[1]]

    for note in notes:
        if note[1] == 0:
            vel += rand_ev(nuance[0], nuance[1], note[0], stp=drift,
                           seed=vel[-1])
        elif note[1] == 1:
            vel += rand_ev(nuance[0], nuance[1], note[0], stp=drift,
                           seed=vel[-1], dec=False)
        elif note[1] == -1:
            vel += rand_ev(nuance[0], nuance[1], note[0], stp=drift,
                           seed=vel[-1], inc=False)

    for c_acc in acc:
        vel[c_acc[0]] = c_acc[1]

    return vel


def vel(track, t_vel, r):
    """Randomly change the velocity of a note in a track"""
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




def pedal(nbt, nmeas, trk=None, bt=480):
    """Play the pedal every n beat starting with the pedal on nbt is the numbr
    of beat per measure and meas is the number of measure"""
    if not trk:
        trk = MidiTrack()
        trk.name = "Pedal"
    p_on = rd.randint(64, 127)
    p_off = rd.randint(64, 127)
    trk.append(Message("control_change", control=64, value=p_on, time=0))
    for i in range(nmeas):
        p_off = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_off,
                           time=bt*nbt))
        p_on = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_on))
    return trk




def tempo(beats, trk=None, bt=480):
    """Create a track setting a tempo at each new beat"""
    if not trk:
        trk = MidiTrack()
        trk.name = "Tempo variation"
    trk.append(MetaMessage("set_tempo",
                           tempo=beats[0],
                           time=0))

    for i, beat in enumerate(beats):
        trk.append(MetaMessage("set_tempo",
                               time=bt,
                               tempo=beat))

    return trk



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
    trk = MidiTrack()
    b = mid.ticks_per_beat
    t = int(b/3)
    notes = [['c4', b], ['s', b], ['c4', t], ['e4', t], ['g4', t], ['c4', b]]
    trk = notes2trk(trk, notes)
    return trk


if __name__ == "__main__":
    mid = MidiFile()
    trk = compo_test()
    t_vel = [[60, 2*b], [30, 3*t], [1, b]]
    trk = vel_r(trk, t_vel, 0.1)
    mid.tracks.append(trk)
    mid.print_tracks()
