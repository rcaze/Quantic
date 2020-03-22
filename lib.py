from mido import MetaMessage, Message, MidiFile, MidiTrack
import numpy.random as rd
import midi2audio as m2a
from pydub.playback import play
from pydub import AudioSegment

def pedal_r(mid, nbt, nmeas):
    """Play the pedal every n beat starting with the pedal on"""
    bt = mid.ticks_per_beat
    trk = MidiTrack()
    trk.name = "Pedal"
    p_on = rd.randint(64, 127)
    p_off = rd.randint(64, 127)
    trk.append(Message("control_change", control=64, value=p_on))
    for i in range(nmeas):
        p_off = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_off,
                           time=bt*nbt))
        p_on = rd.randint(64, 127)
        trk.append(Message("control_change", control=64, value=p_on))
    mid.tracks.append(trk)
    return mid


def add_couples(trk, main_notes, notes, dur):
    """ Add notes while another is played in the background"""
    if type(main_notes) is not list:
        return "main_notes must be a list"
    for m_n in main_notes:
        trk.append(Message("note_on", note=m_n, velocity=100, time=0))

    trk = add_notes(trk, notes, dur)

    for m_n in main_notes:
        trk.append(Message("note_off", note=m_n, velocity=64, time=0))

    return trk


def add_notes(trk, notes, dur):
    """Add notes to a track"""
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


def velocity_r(track, t_vel, r):
    """Randomly change the velocity of a note in a track"""
    for msg in track:
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
    beats_int = [500000, 500000]
    rs = [0.1, 0.1]
    ts_vol = [(0, 50)]
    vols = [100, 100]

    mid = interpret(mid, beats_int, rs, ts_vol, vols)
    mid_play(mid, "test")
