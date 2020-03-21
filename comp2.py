from mido import Message, MidiFile, MidiTrack
import numpy.random as rd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from lib import tempo_r, volume, velocity_r, mid2aud


def comp_lh1(track):
    """Generate the track for the left hand of comptine N°2"""
    # A beat is a 100
    track.append(Message('note_on', note=52, velocity=100, time=0))
    track.append(Message('note_on', note=59, velocity=100, time=50))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_on', note=64, velocity=100, time=0))
    track.append(Message('note_off', note=64, velocity=64, time=50))
    track.append(Message('note_on', note=59, velocity=100, time=0))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_off', note=52, velocity=64, time=0))
    track.append(Message('note_on', note=54, velocity=100, time=0))
    track.append(Message('note_on', note=59, velocity=100, time=50))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_on', note=64, velocity=100, time=0))
    track.append(Message('note_off', note=64, velocity=64, time=50))
    track.append(Message('note_off', note=54, velocity=64, time=0))
    track.append(Message('note_on', note=55, velocity=100, time=0))
    track.append(Message('note_off', note=55, velocity=64, time=50))

    track.append(Message('note_on', note=57, velocity=100, time=0))
    track.append(Message('note_on', note=59, velocity=100, time=50))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_on', note=64, velocity=100, time=0))
    track.append(Message('note_off', note=64, velocity=64, time=50))
    track.append(Message('note_on', note=59, velocity=100, time=0))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_on', note=57, velocity=100, time=0))
    track.append(Message('note_off', note=57, velocity=64, time=50))
    track.append(Message('note_on', note=59, velocity=100, time=0))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_on', note=64, velocity=100, time=0))
    track.append(Message('note_off', note=64, velocity=64, time=50))
    track.append(Message('note_on', note=59, velocity=100, time=0))
    track.append(Message('note_off', note=59, velocity=64, time=50))
    track.append(Message('note_off', note=57, velocity=64, time=0))

    return track


def comp_lh2(track):
    """Generate the track for the left hand of comptine N°2"""
    # A beat is a 100
    track.append(Message('note_on', note=48, velocity=100, time=0))
    track.append(Message('note_on', note=55, velocity=100, time=50))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_on', note=60, velocity=100, time=0))
    track.append(Message('note_off', note=60, velocity=64, time=50))
    track.append(Message('note_on', note=55, velocity=100, time=0))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_off', note=48, velocity=64, time=0))

    track.append(Message('note_on', note=50, velocity=100, time=0))
    track.append(Message('note_on', note=55, velocity=100, time=50))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_on', note=60, velocity=100, time=0))
    track.append(Message('note_off', note=60, velocity=64, time=50))
    track.append(Message('note_off', note=50, velocity=64, time=0))
    track.append(Message('note_on', note=52, velocity=100, time=0))
    track.append(Message('note_off', note=52, velocity=64, time=50))

    track.append(Message('note_on', note=54, velocity=100, time=0))
    track.append(Message('note_on', note=55, velocity=100, time=50))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_on', note=60, velocity=100, time=0))
    track.append(Message('note_off', note=60, velocity=64, time=50))
    track.append(Message('note_on', note=55, velocity=100, time=0))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_on', note=54, velocity=100, time=0))
    track.append(Message('note_off', note=54, velocity=64, time=50))
    track.append(Message('note_on', note=55, velocity=100, time=0))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_on', note=60, velocity=100, time=0))
    track.append(Message('note_off', note=60, velocity=64, time=50))
    track.append(Message('note_on', note=55, velocity=100, time=0))
    track.append(Message('note_off', note=55, velocity=64, time=50))
    track.append(Message('note_off', note=54, velocity=64, time=0))

    return track


def octave(track, note, dur):
    """Generate the couple of blanche"""
    track.append(Message('note_on', note=note, velocity=100, time=0))
    track.append(Message('note_on', note=note + 12, velocity=100, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=dur))
    track.append(Message('note_off', note=note + 12, velocity=64, time=0))
    return track


def croche(track, notes, dur=50):
    """Generet the duet of multiple corche during the sequence"""
    track.append(Message('note_on', note=notes[0], velocity=100, time=0))
    track.append(Message('note_on', note=notes[1], velocity=100, time=dur))
    track.append(Message('note_off', note=notes[0], velocity=64, time=0))
    track.append(Message('note_off', note=notes[1], velocity=64, time=dur))
    return track


def comp_rh1(track):
    """Generate the first part for the right hand of comptine N°2"""
    # A beat is a 100
    # To account for the silence on the right hand

    for i in range(4):
        track = octave(track, 67, dur=400)
        track = octave(track, 66, dur=400)

    for i in range(4):
        track = octave(track, 71, dur=400)
        track = octave(track, 69, dur=400)

    return track


def comp_rh2(track):
    """Generate the first part for the right hand of comptine N°2"""
    # A beat is a 100
    # To account for the silence on the right hand

    for i in range(2):
        for j in range(4):
            track = croche(track, [71, 67])

        track = croche(track, [71, 66])
        track = croche(track, [71, 66])
        track = croche(track, [71, 69])
        track = croche(track, [67, 66])

    for i in range(2):
        for j in range(4):
            track = croche(track, [67, 64])

        if i == 0:
            track = croche(track, [66, 62])
            track = croche(track, [66, 62])
            track = croche(track, [66, 67])
            track = croche(track, [66, 62])
        else:
            track = croche(track, [66, 62])
            track = croche(track, [66, 62])
            track = croche(track, [66, 62])
            track = croche(track, [67, 69])

    return track


def comp_rh3(track, end=True):
    """Generate the third part for the right hand of comptine N°2"""
    # To account for the silence on the right hand

    track = octave(track, 67, dur=200)
    track = octave(track, 69, dur=150)
    track = octave(track, 71, dur=50)

    track = octave(track, 72, dur=300)
    track = octave(track, 71, dur=50)
    track = octave(track, 69, dur=50)

    track = octave(track, 67, dur=200)
    track = octave(track, 69, dur=150)
    track = octave(track, 71, dur=50)

    track = octave(track, 72, dur=250)
    track = octave(track, 71, dur=50)
    track = octave(track, 69, dur=50)
    track = octave(track, 67, dur=50)

    track = octave(track, 64, dur=200)
    track = octave(track, 66, dur=150)
    track = octave(track, 67, dur=50)

    track = octave(track, 69, dur=300)
    track = octave(track, 67, dur=50)
    track = octave(track, 66, dur=50)

    track = octave(track, 64, dur=200)
    track = octave(track, 66, dur=150)
    track = octave(track, 67, dur=50)

    track = octave(track, 69, dur=300)

    if end:
        track = octave(track, 66, dur=100)

    return track


def comp_rh4(track):
    """Generate the fourth part for the right hand of comptine N°2"""
    # A beat is a 100
    # To account for the silence on the right hand
    for i in range(2):
        track = croche(track, [67, 71])
        track = croche(track, [79, 67])
        track = croche(track, [71, 79])
        track = croche(track, [67, 71])

        track = croche(track, [66, 71])
        track = croche(track, [78, 66])
        track = croche(track, [71, 78])
        track = croche(track, [66, 71])

    for i in range(2):
        track = croche(track, [67, 72])
        track = croche(track, [79, 67])
        track = croche(track, [72, 79])
        track = croche(track, [67, 72])

        track = croche(track, [66, 72])
        track = croche(track, [78, 66])
        track = croche(track, [72, 78])
        track = croche(track, [66, 72])

    return track


def generate_vol():
    vols = [44 for i in range(7*4)] + [int(i) for i in np.linspace(44, 24, 3)]
    vols += [44 for i in range(15*4 + 1)]
    vols += [int(i) for i in np.linspace(44, 34, 4)]
    for i in range(7):
        vols += [int(i) for i in np.linspace(34, 44, 4)]
        vols += [int(i) for i in np.linspace(44, 34, 4)]
    vols += [int(i) for i in np.linspace(34, 44, 4)]
    vols += [int(i) for i in np.linspace(44, 34, 3)]

    for i in range(8):
        vols += [68]
        vols += [int(i) for i in np.linspace(68, 70, 2)]
        vols += [int(i) for i in np.linspace(70, 60, 2)]
        vols += [60 for i in range(4)]

    for i in range(3):
        vols += [44, 48, 50, 44] + [44 for i in range(4)]
    vols += [44 for i in range(4)]
    vols += [34]
    return vols


def comptineN2():
    """Generate the midi file of the comptine d'un autre été"""
    mid = MidiFile()
    trackl = MidiTrack()
    trackl.name = "Left hand"
    for i in range(8):
        trackl = comp_lh1(trackl)
        trackl = comp_lh1(trackl)
        trackl = comp_lh2(trackl)
        trackl = comp_lh2(trackl)
    trackl.append(Message('note_on', note=52))
    trackl.append(Message('note_off', note=52, time=200))
    mid.tracks.append(trackl)

    trackr = MidiTrack()
    trackr.name = 'Right hand'
    trackr.append(Message('note_on', note=67, velocity=0, time=3200))
    trackr = comp_rh1(trackr)
    trackr = comp_rh2(trackr)
    trackr = comp_rh2(trackr)
    trackr = comp_rh3(trackr)
    trackr = comp_rh3(trackr, end=True)
    trackr = comp_rh4(trackr)
    trackr.append(Message('note_on', note=71))
    trackr.append(Message('note_off', note=71, time=200))
    mid.tracks.append(trackr)

    mid.ticks_per_beat = 100
    vols = generate_vol()
    mid = volume(mid, vols)
    return mid


silence = AudioSegment.silent(duration=1000)
out = silence
for i in range(3):
    n = "comp2"
    mid = comptineN2()
    tp = rd.randint(450000, 550000)
    beats = [tp for i in range(252)]
    end_beats = [int(i) for i in np.linspace(tp, 4*tp, 8)]
    beats += end_beats
    rs = [0.1 for i in range(260)]
    mid = tempo_r(mid, beats, rs)
    rh = rd.randint(90, 110)
    lh = rd.randint(40, 60)
    mid.tracks[0] = velocity_r(mid.tracks[0], lh, 0.1)
    mid.tracks[1] = velocity_r(mid.tracks[1], rh, 0.1)
    mid.save("I" + n + ".mid")
    out += mid2aud("I" + n) + silence

out = out + 15
out.export("Icomp2.wav")
play(out)
