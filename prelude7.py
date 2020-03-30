from mido import MidiFile, MidiTrack
from lib import velocity_r, tempo_r, mid2aud, add_notes, add_couples, pedal_r
# import numpy as np
# import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play

def pre7r(trk, bt):
    cl = int(bt/2)
    c = int(bt/4)
    bp = cl + int(cl/2)
    bl = int(2*bt)

    trk = add_notes(trk, [[64], [61+12], [62+12], [62, 67+1, 71],
                          [62, 67+1, 71],[62, 67+1, 71]],
                    [bt, bp, c, bt, bt, bl] )

    trk = add_notes(trk, [[62+12, 66+12], [60+12, 63+12], [61+12, 64+12],
                          [61+12, 69+12], [61+12, 69+12], [61+12, 69+12]],
                    [bt, bp, c, bt, bt, 2*bt])

    trk = add_notes(trk, [[64, 61+12], [62, 70], [62, 71]],
                          [bt, bp, c])
    trk = add_couples(trk, [62], [[66, 62+12], [66, 62+12], [66, 62+12]]
                      ,[bt, bt, bl])

    trk = add_notes(trk, [[62, 68], [62, 68], [61, 69], [61, 61 + 12],
                          [61, 61+12], [61, 61+12]],
                    [bt, bp, c, bt, bt, bl])

    trk = add_notes(trk, [[64]], [bt])
    trk = add_couples(trk, [64, 68], [[61+12], [62+12]], [bp, c])
    trk = add_notes(trk, [[62, 68, 71],  [62, 68, 71], [62, 68, 71]],
                    [bt, bt, bl])

    trk = add_notes(trk, [[62+12, 66+12], [72, 63+12], [61+12, 64+12],
                          [61+12, 64+12, 69+12, 61+24],
                          [61+12, 64+12, 69+12, 61+24],
                          [70, 61+12, 64+12, 70+12, 61+24]],
                    [bt, bp, c, bt, bt, bl])

    trk = add_notes(trk, [[70, 61+12], [70, 61+12], [71, 62+12],
                          [71, 66+12],
                          [70, 66+12],
                          [68, 66+12]],
                    [bt, bp, c, bt, bt, bl])

    trk = add_notes(trk, [[62, 68], [62, 71], [61, 69]],
                    [bt, bp, c])
    trk = add_couples(trk, [69], [[61+12, 69+12], [61+12, 69+12], [61+12, 69+12]],
                      [bt, bt, bl])
    return trk


def pre7l(trk, bt):
    bl = int(2*bt)
    d_pat = [bt, bt, bt, bl, bt]
    trk = add_notes(trk, [[-1]], [bt])
    trk = add_notes(trk, [[64-24], [64-12, 64],  [64-12, 64], [64-12, 64],
                          [-1]],
                    d_pat)
    trk = add_notes(trk, [[69-24], [69-12, 64],  [69-12, 64], [69-12, 64],
                          [-1]],
                    d_pat)
    trk = add_notes(trk, [[64-24], [64-12, 71-12],  [64-12, 71-12],
                          [64-12, 71-12],
                          [-1]],
                    d_pat)

    trk = add_notes(trk, [[64-24], [64-12, 64],  [64-12, 64], [64-12, 64],
                          [-1]],
                    d_pat)

    trk = add_notes(trk, [[69-36], [64-12, 69-12, 64],
                          [64-12, 69-12, 64],
                          [69-12, 69-12, 64], [-1]],
                    d_pat)

    trk = add_notes(trk, [[69-24], [69-12, 64, 69], [69-12, 64, 69],
                          [66-12, 64, 61, 66],
                          [-1]],
                    d_pat)
    trk = add_notes(trk, [[71-36], [66-12, 62], [66-12, 71-12, 62],
                          [66-12, 71-12, 62], [-1]],
                    d_pat)
    trk = add_notes(trk, [[69-36], [64-12, 69-12, 64],
                          [64-12, 69-12, 64],
                          [69-12, 64], [-1]],
                    d_pat)
    return trk



n = "prelude7"
mid = MidiFile()
bt = mid.ticks_per_beat
trkr = MidiTrack()
trkl = MidiTrack()
trkr = pre7r(trkr, bt)
trkl = pre7l(trkl, bt)
beats = [1000000 for i in range(1+15*3)]
out = AudioSegment.silent(duration=1000)
for rep in range(1, 4):
    rs = [0.08*rep for j in range(1+15*3)] # Given my count there are 144 measures
    trkr = velocity_r(trkr, 90, 0.1)
    trkl = velocity_r(trkl, 50, 0.1)
    mid.tracks.append(trkr)
    mid.tracks.append(trkl)
    mid = tempo_r(mid, beats, rs)
    mid = pedal_r(mid, 3, 16, add=mid.ticks_per_beat)
    mid.save("I" + n + ".mid")
    new = mid2aud("I" + n)
    out += new
out.export("I" + n + ".wav")
play(out)
