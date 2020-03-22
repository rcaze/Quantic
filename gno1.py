from mido import MidiFile, MidiTrack
from lib import velocity_r, tempo_r, mid2aud, add_notes, add_couples, pedal_r
from lib import volume
import numpy as np
# import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play


def gno1_l(trk, bt, second=False):
    for i in range(8):
        trk = add_couples(trk, [67-24], [[-1], [71-12, 62, 66]], [bt, 2*bt])
        trk = add_couples(trk, [62-24], [[-1], [69-12, 61, 66]], [bt, 2*bt])

    trk = add_couples(trk, [66-24], [[-1], [69-12, 61, 66]], [bt, 2*bt])
    trk = add_couples(trk, [71-36], [[-1], [71-12, 62, 66]], [bt, 2*bt])
    trk = add_couples(trk, [64-24], [[-1], [71-12, 69-12]], [bt, 2*bt])
    trk = add_couples(trk, [64-24], [[-1], [71-12, 62, 67]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [65-12, 69-12, 62]], [bt, 2*bt])
    trk = add_couples(trk, [69-36], [[-1], [69-12, 60, 64]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [67-12, 71-12, 64]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [62-12, 67-12, 71-12, 64]], [bt, 2*bt])

    trk = add_couples(trk, [62-24], [[-1], [60-24, 64-12, 69-12, 62]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [60-24, 66-12, 69-12, 62]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [69-12, 60, 65]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [69-12, 60, 64]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [62-12, 67-12, 71-12, 64]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [60-12, 64-12, 69, 62]], [bt, 2*bt])
    trk = add_couples(trk, [62-24], [[-1], [60-12, 66-12, 69, 62]], [bt, 2*bt])

    if not second:
        trk = add_couples(trk, [64-24], [[-1], [71-12, 64, 67]], [bt, 2*bt])
        trk = add_couples(trk, [66-24], [[-1], [69-12, 61, 66]], [bt, 2*bt])
        trk = add_couples(trk, [71-36], [[-1], [71-12, 62, 66]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [61, 64, 69]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [69-12, 61, 66, 69]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [71-24, 69-12, 62],
                                         [64-12, 71-12, 62, 67]],
                          [bt, bt, bt])
        trk = add_notes(trk, [[69-24, 67-12]], [3*bt])
        trk = add_notes(trk, [[62-24, 69-12, 62-12]], [3*bt])
    else:
        trk = add_couples(trk, [64-24], [[-1], [71-12, 64, 67]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [69-12, 62, 65, 69]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [69-12, 60, 65]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [60, 64, 69]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [69-12, 60, 65, 69]], [bt, 2*bt])
        trk = add_couples(trk, [64-24], [[-1], [71-24, 69-12, 62],
                                         [64-12, 71-12, 62, 67]],
                          [bt, bt, bt])
        trk = add_notes(trk, [[69-24, 67-12]], [3*bt])
        trk = add_notes(trk, [[62-24, 69-12, 62-12]], [3*bt])
    return trk


def gno1_r(trk, bt, second=False):

    trk = add_notes(trk, [[-1], [66+12], [69+12], [67+12], [66+12], [61 + 12],
                          [71], [61+12], [62+12], [69], [66]],
                    [bt*13, bt, bt , bt, bt, bt, bt, bt, bt, 3*bt, 12*bt])
    trk = add_notes(trk, [[-1], [66+12], [69+12], [67+12], [66+12], [61 + 12],
                          [71], [61+12], [62+12], [69]],
                    [bt for i in range(9)] + [3*bt])
    trk = add_notes(trk, [[61+12], [66+12], [64], [69], [71], [60+12], [64+12],
                          [62+12], [71], [62+12], [60+12], [71]],
                    [3*bt, 3*bt, 9*bt, bt, bt, bt, bt, bt, bt, bt, bt, bt])
    trk = add_notes(trk, [[62+12], [62+12], [64+12], [65+12], [67+12], [69+12],
                          [60+12], [62+12], [64+12], [62+12], [71],
                          [62+12], [62+12]],
                    [5*bt] + [bt for i in range(10)] + [5*bt, bt])
    if not second:
        trk = add_notes(trk, [[67+12], [66+12], [71], [69], [71],
                              [61+12], [62+12], [64+12], [61+12], [62+12], [64+12],
                              [66], [60, 64, 69, 60+12], [62, 66, 69, 62]],
                        [3*bt, 3*bt] + [bt for i in range(9)] + [3*bt, 3*bt, 3*bt])
    else:
        trk = add_notes(trk, [[67+12], [65+12], [71], [60+12], [65+12],
                              [64+12], [62+12], [60+12], [64+12], [62+12], [60+12],
                              [65], [60, 64, 69, 60+12], [62, 65, 69, 62]],
                        [3*bt, 3*bt] + [bt for i in range(9)] + [3*bt, 3*bt, 3*bt])

    return trk



n = "gno1"
beats = [750000 for i in range(76*3)]
out = AudioSegment.silent(duration=1000)
mid = MidiFile()
bt = int(mid.ticks_per_beat)
vols = []
for i in range(2):
    vols += [75 for i in range(3*4)]
    vols += [int(i) for i in np.linspace(75, 80, 9)]
    vols += [80, 75, 70]
    vols += [90 for i in range(3*4+1)]
    vols += [int(i) for i in np.linspace(80, 90, 9)]
    vols += [int(i) for i in np.linspace(90, 75, 9)]
    vols += [75 for i in range(3*3)]
    vols += [int(i) for i in np.linspace(75, 90, 9)]
    vols += [int(i) for i in np.linspace(90, 80, 5)]
    vols += [int(i) for i in np.linspace(80, 90, 6)]
    vols += [int(i) for i in np.linspace(90, 80, 5)]
    vols += [80 for i in range(3)]
    vols += [int(i) for i in np.linspace(80, 90, 3)]
    vols += [90 for i in range(10)]
    vols += [int(i) for i in np.linspace(90, 80, 6)]

for rep in range(1,4):
    rs = [0.08*rep for j in range(76*3)]
    trkr = MidiTrack()
    trkl = MidiTrack()
    trkr = gno1_r(trkr, bt)
    trkr = gno1_r(trkr, bt, second=True)
    trkl = gno1_l(trkl, bt)
    trkl = gno1_l(trkl, bt, second=True)
    trkr = velocity_r(trkr, 100, 0.1)
    trkl = velocity_r(trkl, 50, 0.1)
    mid = volume(mid, vols)
    mid = pedal_r(mid, 4, 16)
    mid.tracks.append(trkr)
    mid.tracks.append(trkl)
    mid = tempo_r(mid, beats, rs)
    mid.save("I" + n + ".mid")
    out += mid2aud("I" + n)
out.export("I" + n + ".wav")
play(out)
