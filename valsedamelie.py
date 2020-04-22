from mido import MidiFile, MidiTrack
import lib
import numpy as np
# import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play
from importlib import reload
reload(lib)

b = 480
c = int(b/2)
cc = int(c/2)
t = int(b/3)
w = int(2*b)

rhand1, rhand2, lhand1, lhand2, vell1, vell2, velr1, velr2 = [], [], [], [], [], [], [], []
beats = [400000]
beats = [600000 for i in range(2*32)] + [400000 for i in range(3*64)]
rs = [0.08]
rs = [0.08 for i in range(2*32)] + [0.08 for i in range(3*64)]



#First Part
rhand1 = [('d5', w+b+c+cc), ('c5', cc), ('b4', w+b), ('a4', b), ('d5', w+t),
         ('e5', t), ('d5', t), ('c5', t), ('b4', t), ('c5', t), ('b4', w+b),
         ('a4',b)]
rhand1 +=[('c5', w+b+c+cc), ('b4', cc), ('e4', 2*w), ('c5', w+t), ('d5', t),
         ('c5',t), ('b4',t), ('c5',t), ('b4', t), ('e4', w+w)]
rhand1 += [('d5 d6', w+b+c+cc), ('c5 c6', cc), ('b4 b5', w+b), ('a4 a5', b),
          ('d5 d6', w+t), ('e5', t), ('d5', t), ('c5', t), ('b4', t),
          ('c5', t), ('b4 b5', w+b), ('a4 a5',b)]
rhand1 +=[('c5 c6', w+b+c+cc), ('b4 b5', cc), ('e4 e5', 2*w), ('c5 c6', w+t),
         ('d5', t), ('c5',t), ('b4',t), ('c5',t), ('b4', t), ('e4 e5', w+w)]
rhand2 = [('s', 32*w)]

velr1 = [[64, 5*w+t], [68, t], [70, t], [72,3*t], [68, 2*w],
        [67, 5*w+t], [68, t], [70, t], [72,3*t], [66, 2*w],
        [54, w+b+c], [64, c], [65, w], [75, w+b], [78, b], [78, w+t], [78, t], [79, t], [80,3*t+w+b], [70,b],
        [54, 5*w+t], [64, t], [66, t], [70,3*t], [64, 2*w]]


lhand1 = [('d3', w), ('f3 a3 d4', w), ('a2', w), ('c3 e3 b3', w)] * 2
lhand1 += [('f3', w), ('a3 c4', w), ('c3', w), ('e3 g3 b3', w)] * 2
lhand1 += [('d3', w), ('f3 a3 d4', w), ('a2', w), ('c3 e3 b3', w)] * 2
lhand1 += [('f3', w), ('a3 c4', w), ('c3', w), ('e3 g3 b3', w)] * 2

vell1 = [[24, 4*w],
        [24, 4*w],
        [19, w], [20, w], [25, w], [30, w], [35, w], [24, 3*w],
        [24, 30*w]]

lhand2 = [('s', 32*w)]
velr2 = [[1, 32*w]]
vell2 = [[1, 32*w]]

# Second part
rhand1 += 2 * [('d5', w+b), ('d5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

velr += 2*[[54, 3*b],
          [60, b], [62, b], [64, b],
          [64, 3*b],
          [64, b], [62, b], [60, b]]


lhand1 += 2 * ([('d3', w+b)] * 2 + [('a2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('f3 a3 d4', b), ('f3 a3 d4', b)] * 2 + [('s', b), ('c3 e3 a3', b), ('c3 e3 a3', b)] * 2)

vell1 += 2 * [[60, w+b], [60, w+b], [60, w+b], [60, w+b]]
vell2 += 2 * [[40, 12*b]]

rhand1 += 2 * [('c5', w+b), ('c5', w+b), ('c5', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]

velr += 2*[[64, 3*b],
           [64, 3*b],
           [64, b], [66, b], [70, b],
           [70, b], [66, b], [64, b]]


lhand1 += 2 * ([('f3', w+b)] * 2 + [('c2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('a3 c4', b), ('a3 c4', b)] * 2 + [('s', b), ('e3 g3', b), ('e3 g3', b)] * 2)

vell1 += 2 * [[60, w+b], [60, w+b], [60, w+b], [60, w+b]]
vell2 += 2 * [[40, 12*b]]

rhand1 += 2 * [('d5', w+b), ('e5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

velr += 2*[[74, 3*b],
           [74, 3*b],
           [74, 3*b],
           [74, b], [66, b], [64, b]]

lhand1 += 2 * ([('d3', w+b)] * 2 + [('a2', w+b)] + [('c3', w+b)])
lhand2 += 2 * ([('s', b), ('f3 a3 d4', b), ('f3 a3 d4', b)] * 2 + [('s', b), ('c3 e3 a3', b), ('c3 e3 a3', b-10)] + [('s', b), ('e3 a3', b), ('e3 a3', b)])

vell1 += 2 * [[65, w+b], [65, w+b], [65, w+b], [65, w+b]]
vell2 += 2 * [[45, 12*b]]

rhand1 += 2 * [('c5', w+b), ('c5', b+c), ('b4', b+c), ('g4', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]

velr += 2*[[74, 3*b],
          [74, 3*b],
          [74, b], [78, b], [80, b],
          [80, b], [78, b], [74, b]]


lhand1 += 2 * ([('f3', w+b)] * 2 + [('c2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('a3 c4', b), ('a3 c4', b)] * 2 + [('s', b), ('e3 g3', b), ('e3 g3', b)] * 2)

vell1 += 2 * [[65, w+b], [65, w+b], [60, w+b], [60, w+b]]
vell2 += 2 * [[45, 12*b]]

# Third part
rhand1 += [('d5', w+b+c), ('e5', c), ('f5', c), ('e5', c), ('f5', c), ('e5', c),
           ('a4', w+2*b), ('b4', b+c), ('c5', c),
           ('d5', w+b+c), ('e5', c), ('f5', c), ('e5', c), ('f5', c), ('e5', c),
           ('a4', w+2*b+c), ('g4', b+c),
           ('a4', w+b+c), ('b4', c), ('c5', c), ('b4', c), ('c5', c), ('b4', c),
           ('e4', w+2*b), ('f4', b+c), ('g4', c),
           ('a4', w+b+c), ('b4', c), ('c5', c), ('b4', c), ('c5', c), ('b4', c),
           ('e4', 2*(w+b)),
           ('d5 d6', 2*w), ('c5 c6', w), ('b4 b5', w+b), ('a4 a5', w+b),
           ('d5 d6', w+b+c), ('e5', c), ('d5', c), ('c5', c), ('b4', c),
           ('c5', c), ('b4 b5', w+b), ('a4 a5', w+b),
           ('c5 c6', 2*w+c), ('b4 b5', b+c), ('e4 e5', 2*(w+b)),
           ('c5 c6', w+b+c), ('d5', c), ('c5', c), ('b4', c), ('c5', c),
           ('b4', c), ('e4 e5', 2*(w+b))]

velr += [[100, w+b], [100, b], [105, b], [110, b], [115, 2*(w+b)],
         [115, 4*(w+b)],
         [100, w+b], [100, b], [105, b], [108, b], [110, 2*(w+b)],
         [110, 4*(w+b)],
         [100, w+b], [100, b], [105, b], [108, b], [110, 2*(w+b)],
         [110, 3*(w+b)], [108, w+b],
         [108, 4*(w+b)],
         [108, 4*(w+b)],
         [108, 4*(w+b)],
         [108, 3*(w+b)], [100, w+b]]

lpart3 = 2 * [('d3', c), ('a3', c), ('d4', c), ('e4', c), ('f4', c), ('a4', c),
              ('f4', c), ('e4', c), ('d4', c), ('a3', c), ('d3', c), ('a3', c),
              ('a2', c), ('e3', c), ('a3', c), ('b3', c), ('c4', c), ('e4', c),
              ('c4', c), ('b3', c), ('a3', c), ('e3', c), ('a2', c), ('e3', c)]

lpart3 += 2 * [('f2', c), ('c3', c), ('f3', c), ('g3', c), ('a3', c), ('c4', c),
              ('a3', c), ('g3', c), ('f3', c), ('c3', c), ('f2', c), ('c3', c),
              ('c2', c), ('g2', c), ('c3', c), ('d3', c), ('e3', c), ('g3', c),
              ('e3', c), ('d3', c), ('c3', c), ('g2', c), ('c2', c), ('g2', c)]

lhand1 += 2*lpart3
vell1 += [[50, 40*(w+b)]]



n = "valse_amelie"
mid = MidiFile()
trkr1 = lib.notes2trk(MidiTrack(), rhand1)
trkr2 = lib.notes2trk(MidiTrack(), rhand2)
trkl1 = lib.notes2trk(MidiTrack(), lhand1)
trkl2 = lib.notes2trk(MidiTrack(), lhand2)

trkr1 = lib.vel_r(trkr1, velr, 0.1)
#trkr2 = lib.vel_r(trkr2, velr, 0.1)
trkl1 = lib.vel_r(trkl1, vell1, 0.1)
trkl2 = lib.vel_r(trkl2, vell2, 0.1)

mid.tracks.append(trkr1)
mid.tracks.append(trkr2)
mid.tracks.append(trkl1)
mid.tracks.append(trkl2)

mid = lib.tempo_r(mid, beats, rs)
mid.save("I" + n + ".mid")
out = lib.mid2aud("I" + n) + 10
out.export("I" + n + ".wav")
play(out)
