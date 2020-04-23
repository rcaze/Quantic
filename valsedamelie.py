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
beats = [700000 for i in range(2*32-1)] + [350000 for i in range(3*(3*32)+1)]
rs = [0.08 for i in range(2*32)] + [0.08 for i in range(3*(3*32))]
beats += [700000 for i in range(2*6)] + [800000, 900000]
rs += [0.08 for i in range(2*8)]

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

vr1 = [[64, 5*w+t]]
vr1 += [[64, t], [67, t], [69, t], [70, t], [72, t], [70, w], [68, w]]
velr = 2*vr1
vr2 = [[int(i), w] for i in np.linspace(64, 74, 5)]
vr2 += [[74, t], [75, t], [77, t], [79, t], [80, t], [82, t], [85, w], [75, w]]
velr += vr2
velr += vr1

lhand1 = [('d3', w), ('f3 a3 d4', w), ('a2', w), ('c3 e3 b3', w)] * 2
lhand1 += [('f3', w), ('a3 c4', w), ('c3', w), ('e3 g3 b3', w)] * 2
lhand1 += [('d3', w), ('f3 a3 d4', w), ('a2', w), ('c3 e3 b3', w)] * 2
lhand1 += [('f3', w), ('a3 c4', w), ('c3', w), ('e3 g3 b3', w)] * 2
lhand2 = [('s', 32*w)]

# Second part
rhand1 += 2 * [('d5', w+b), ('d5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

lhand1 += 2 * ([('d3', w+b)] * 2 + [('a2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('f3 a3 d4', b), ('f3 a3 d4', b)] * 2 + [('s', b), ('c3 e3 a3', b), ('c3 e3 a3', b)] * 2)

rhand1 += 2 * [('c5', w+b), ('c5', w+b), ('c5', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]

lhand1 += 2 * ([('f3', w+b)] * 2 + [('c2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('a3 c4', b), ('a3 c4', b)] * 2 + [('s', b), ('e3 g3', b), ('e3 g3', b)] * 2)

rhand1 += 2 * [('d5', w+b), ('e5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

lhand1 += 2 * ([('d3', w+b)] * 2 + [('a2', w+b)] + [('c3', w+b)])
lhand2 += 2 * ([('s', b), ('f3 a3 d4', b), ('f3 a3 d4', b)] * 2 + [('s', b), ('c3 e3 a3', b), ('c3 e3 a3', b-10)] + [('s', b), ('e3 a3', b+10), ('e3 a3', b)])


rhand1 += 2 * [('c5', w+b), ('c5', b+c), ('b4', b+c), ('g4', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]


lhand1 += 2 * ([('f3', w+b)] * 2 + [('c2', w+b)] * 2)
lhand2 += 2 * ([('s', b), ('a3 c4', b), ('a3 c4', b)] * 2 + [('s', b), ('e3 g3', b), ('e3 g3', b)] * 2)

velr += 4*[[60, 2*(w+b)], [65, 2*b],  [70, b], [65, 2*b],  [60, b]]
velr += 4*[[78, 2*(w+b)], [80, 2*b],  [84, b], [80, 2*b],  [60, b]]
vell = [[i[0]-40, i[1]] for i in velr]

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
rhand2 += [('s', 32*(w+b))]

lpart3 = 2 * [('d3', c), ('a3', c), ('d4', c), ('e4', c), ('f4', c), ('a4', c),
              ('f4', c), ('e4', c), ('d4', c), ('a3', c), ('d3', c), ('a3', c),
              ('a2', c), ('e3', c), ('a3', c), ('b3', c), ('c4', c), ('e4', c),
              ('c4', c), ('b3', c), ('a3', c), ('e3', c), ('a2', c), ('e3', c)]

lpart3 += 2 * [('f2', c), ('c3', c), ('f3', c), ('g3', c), ('a3', c), ('c4', c),
              ('a3', c), ('g3', c), ('f3', c), ('c3', c), ('f2', c), ('c3', c),
              ('c2', c), ('g2', c), ('c3', c), ('d3', c), ('e3', c), ('g3', c),
              ('e3', c), ('d3', c), ('c3', c), ('g2', c), ('c2', c), ('g2', c)]

lhand1 += 2*lpart3
lhand2 += [['s', 32*(w+b)]]

velr += [[100, w+b], [100, b], [105, b], [110, b], [115, 2*(w+b)],
         [115, 4*(w+b)],
         [100, w+b], [100, b], [105, b], [108, b], [110, 2*(w+b)],
         [110, 4*(w+b)],
         [100, w+b], [100, b], [105, b], [108, b], [110, 2*(w+b)],
         [110, 3*(w+b)], [108, w+b],
         [108, 4*(w+b)],
         [108, 3*(w+b)], [108, w+b]]

vell += [[50, 32*(w+b)]]

# Fourth part
rhand1 += 2 * [('d5', w+b), ('d5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

rhand1 += 2 * [('c5', w+b), ('c5', w+b), ('c5', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]


rhand1 += 2 * [('d5', w+b), ('e5', b+c), ('c5', b+c), ('b4', w+b), ('a4', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('e4', c), ('f4', c),
               ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
               ('s', c), ('c4', c), ('d4', c), ('e4', c), ('d4', c), ('c4', c)]

rhand1 += 2 * [('c5', w+b), ('c5', b+c), ('b4', b+c), ('g4', w+b), ('s', w+b)]
rhand2 += 2 * [('s', c), ('e4', c), ('f4', c), ('e4', c), ('f4', c), ('e4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('e4', c), ('f4', c),
              ('s', c), ('d4', c), ('e4', c), ('d4', c), ('e4', c), ('d4', c),
              ('e4', c), ('d4', c), ('c4', c), ('e4', c), ('d4', c), ('c4', c)]


lc1 = ['d2', 'a2', 'd3', 'e3', 'f3', 'a3', 'f3', 'e3', 'd3', 'a2', 'd2', 'a2']
lc1 += ['a1', 'e2', 'a2', 'b2', 'c3', 'e3', 'c3', 'b2', 'a2', 'e2', 'a1', 'e2']
lc1 = 2*lc1
lc2 = ['f2', 'c3', 'f3', 'g3', 'a3', 'c4', 'a3', 'g3', 'f3', 'c3', 'f2', 'c3']
lc2 += ['c2', 'g2', 'c3', 'd3', 'e3', 'g3', 'e3', 'd3', 'c3', 'g2', 'c2', 'g2']
lc2 = 2*lc2
lc = 2*(lc1 + lc2)
lhand1 += [(i, c) for i in lc]


velr += 8*[[60, 2*(w+b)], [65, 2*b],  [70, b], [65, 2*b],  [60, b]]
vell += 8*[[30, 2*(w+b)], [35, 2*b],  [40, b], [35, 2*b],  [30, b]]

#Fifth Part
rhand1 += [('d5', w+b+c+cc), ('c5', cc), ('b4', w+b), ('a4', b), ('d5', w+t),
         ('e5', t), ('d5', t), ('c5', t), ('b4', t), ('c5', t), ('b4', w+b),
         ('a4',b)]
velr += [[50, 5*w+t], [50, t], [45, t], [40 ,3*t], [40, w+b], [30, b]]

lhand1 += [('d3', w), ('f3 a3 d4', w), ('a2', w), ('c3 e3 b3', w)] * 2
vell1 += [[20, 8*w]]

trkr1 = lib.notes2trk(MidiTrack(), rhand1)
trkr2 = lib.notes2trk(MidiTrack(), rhand2)
trkl1 = lib.notes2trk(MidiTrack(), lhand1)
trkl2 = lib.notes2trk(MidiTrack(), lhand2)
vol = [50 for i in range(32*2-1)]
vol += [65 for i in range(32*3)]
vol += [90 for i in range(32*3+1)]
vol += [65 for i in range(32*3-1)]
vol += [50 for i in range(8*2+1)]

"""
vel_r doestn't work weel FUCK
trkr1 = lib.vel_r(trkr1, velr, 0.1)
trkr2 = lib.vel_r(trkr2, velr, 0.1)
trkl1 = lib.vel_r(trkl1, vell, 0.1)
trkl2 = lib.vel_r(trkl2, vell, 0.1)
"""

n = "valse_amelie"
mid = MidiFile()
mid.ticks_per_beat = b

trkr1 = lib.vel(trkr1, 100, 0.2)
trkr2 = lib.vel(trkr2, 100, 0.2)
trkl1 = lib.vel(trkl1, 50, 0.2)
trkl2 = lib.vel(trkl2, 50, 0.2)
mid = volume(mid, vol)
mid.tracks.append(trkr1)
mid.tracks.append(trkr2)
mid.tracks.append(trkl1)
mid.tracks.append(trkl2)

mid = lib.tempo_r(mid, beats, rs)
mid.save("I" + n + ".mid")
out = lib.mid2aud("I" + n) + 10
out.export("I" + n + ".wav")
play(out)
