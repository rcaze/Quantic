from mido import MidiFile, MidiTrack
import lib
import numpy as np
import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play
from importlib import reload
reload(lib)

b = 480
c = int(b/2)
cc = int(c/2)
t = int(b/3)
w = int(2*b)

ppp = [7, 22]
pp = [23, 38]
p = [39, 54]
mp = [55, 70]
mf = [71, 86]
f = [87, 102]
ff = [103, 111]
fff = [112, 127]

mf = mp

def left_motif1(nuance, vel_init=None, second_nuance=None):
    """Make the motif repeat with distinct initial values and min/max"""
    notes = [['e3', b], ['g3', b], ['e3', b], ['g3', b]]
    notes += [['d3', b], ['g3', b], ['d3', b], ['g3', b]]
    notes += [['d3', b], ['f3+', b], ['d3', b], ['f3+', b]]
    notes += [['d3', b], ['f3+', b], ['d3', b], ['f3+', b]]

    if not vel_init:
        vel_init = rd.randint(nuance[0], nuance[1])

    if not second_nuance:
        vel = lib.velocity(vel_init, nuance, [[3, 0], [4, 1], [4, 0], [4, -1]],
                           offset=10)
    else:
        vel = lib.velocity(vel_init, nuance, [[3, 0], [4, 1]],
                           offset=10)
        vel += lib.velocity(vel[-1], second_nuance, [[3, 0], [4, -1]],
                           offset=10)
    lhand1 = [notes[i] + [c_vel] for i, c_vel in enumerate(vel)]

    return lhand1, vel


def left_motif2(nuance, vel_init=None, second_nuance=None):
    """Make the motif repeat with distinct initial values and min/max"""
    notes = 4 * [['e4', c], ['b3', c]]
    notes += 4 * [['d4', c], ['b3', c]]
    notes += 4 * [['d4', c], ['b3', c]]
    notes += 4 * [['d4', c], ['a3', c]]

    if not vel_init:
        vel_init = rd.randint(nuance[0], nuance[1])

    if not second_nuance:
        vel = lib.velocity(vel_init, nuance, [[7, 0], [8, 1], [8, 0], [8, -1]],
                           offset=15)
    else:
        vel = lib.velocity(vel_init, nuance, [[7, 0], [8, 1]],
                           offset=15)
        vel += lib.velocity(vel[-1], second_nuance, [[7, 0], [8, -1]],
                           offset=15)

    lhand2 = [notes[i] + [c_vel] for i, c_vel in enumerate(vel)]

    return lhand2, vel


def right_motif1(nuance, vel_init=None, second=False):
    if not second:
        notes = [['s', c], ['g4', cc], ['f4+', cc], ['g4', c], ['b4', cc], ['c5', cc], ['b4', w],
                 ['s', c], ['f4+', cc], ['g4', cc], ['f4+', c], ['g4', cc], ['a4', cc], ['g4', w],
                 ['s', c], ['f4+', cc], ['e4', cc], ['f4+', c], ['b4', cc], ['c5', cc], ['b4', w],
                 ['s', c], ['f4+', cc], ['e4', cc], ['f4+', w+b]]
    else:
        notes = [['s', c], ['g5', cc], ['f5+', cc], ['g5', c], ['b5', cc], ['c6', cc], ['b5', w],
                 ['s', c], ['f5+', cc], ['g5', cc], ['f5+', c], ['g5', cc], ['a5', cc], ['g5', w],
                 ['s', c], ['f5+', cc], ['e5', cc], ['f5+', c], ['b5', cc], ['c6', cc], ['b5', w],
                 ['s', c], ['f5+', cc], ['e5', cc], ['f5+', w+b]]

    if not vel_init:
        vel_init = rd.randint(nuance[0], nuance[1])
    vel = lib.velocity(vel_init, nuance, [[7, 0], [3, 1], [4, -1], [3, 1],
                                          [4, -1], [3, -1]],
                       acc=[[0, 0], [7, 0], [14, 0], [21, 0]])

    rhand = [notes[i] + [c_vel] for i, c_vel in enumerate(vel)]
    return rhand, vel


def right_motif2(nuance1, nuance2, vel_init=None ,second=False):
    if not second:
        notes = [['e5', b+c], ['b4', c+w], ['d5', b+c], ['b4', w+c],
                       ['f5+', b+c], ['b4', c+w], ['f5+', b+c], ['a4', w+c]]
        notes += [['b4 g5', b+c], ['g4 e5', c+w], ['b4 g5', b+c], ['g4 d5', w+c],
                        ['b4 f5+', b+c], ['f4+ d5', c+w], ['a4 f5+', b+c], ['f4+ d5', w+c]]
    else:
        notes = [['e6', b+c], ['b5', c+w], ['d6', b+c], ['b5', w+c],
                       ['f6+', b+c], ['b5', c+w], ['f6+', b+c], ['a5', w+c]]
        notes += [['b5 g6', b+c], ['g5 e6', c+w], ['b5 g6', b+c], ['g5 d6', w+c],
                        ['b5 f6+', b+c], ['f5+ d6', c+w], ['a5 f6+', b+c], ['f5+ d6', w+c]]
    if not vel_init:
        vel_init = rd.randint(nuance1[0], nuance1[1])
    vel = lib.velocity(vel_init, nuance1, [[1, 0], [2, 1], [2, 0], [2, -1]])
    vel_init = rd.randint(nuance2[0], nuance2[1])
    vel += lib.velocity(vel_init, nuance2, [[1, 0], [2, 1], [2, 0], [2, -1]])

    rhand = [notes[i] + [c_vel] for i, c_vel in enumerate(vel)]
    return rhand, vel


def right_motif3(nuance, vel_init=None, rep=False, first=True, second_nuance=None):
    if first:
        notes = 4*['b4', 'e5', 'b5'] + ['b4', 'e5', 'c5', 'e5']
        notes += 4*['b4', 'd5', 'b5'] + ['b4', 'd5', 'a4', 'd5']
        notes += 4*['f4+', 'b4', 'f5+'] + ['f4+', 'b4', 'g4', 'b4']
        if rep:
            notes += 4*['a4', 'd5', 'a5'] + ['a4', 'd5', 'a5']
        else:
            notes += 4*['a4', 'd5', 'a5'] + ['a4', 'd5', 'g4', 'd5']
    else:
        notes = 4*['b5', 'e6', 'b6'] + ['b5', 'e6', 'c6', 'e6']
        notes += 4*['b5', 'd6', 'b6'] + ['b5', 'd6', 'a5', 'd6']
        notes += 4*['f5+', 'b5', 'f6+'] + ['f5+', 'b5', 'g5', 'b5']
        if not rep:
            notes += 4*['a5', 'd6', 'a6'] + ['a5', 'd6', 'g5', 'd6']
        else:
            notes += 4*['a5', 'd6', 'a6'] + ['a5', 'd6', 'a6', 'g6']

    if not vel_init:
        vel_init = rd.randint(nuance[0], nuance[1])

    acc = np.array([0, 12, 14])
    if rep:
        acc_t = acc.tolist() + (acc + 16).tolist() + (acc + 32).tolist() + (acc + 48).tolist()
    else:
        acc_t = acc.tolist() + (acc + 16).tolist() + (acc + 32).tolist() + [48]

    if second_nuance:
        if rep:
            acc_t = acc.tolist() + (acc + 16).tolist()
        else:
            acc_t = acc.tolist() + [16]

    acc = [[a , int(rd.randint(nuance[1], nuance[1]+10))] for a in acc_t]

    if first:
        if rep:
            vel = lib.velocity(vel_init, nuance, [[15, 0], [16, 1], [16, 0],
                                              [15, -1]], acc=acc)
        else:
            vel = lib.velocity(vel_init, nuance, [[15, 0], [16, 1], [16, 0],
                                                  [16, -1]], acc=acc)
    else:
        vel = lib.velocity(vel_init, nuance, [[15, 0], [16, 1]],
                           acc=acc)
        vel += lib.velocity(vel[-1], second_nuance, [[15, 0], [16, -1]], acc=acc)


    rhand = [[notes[i], cc] + [c_vel] for i, c_vel in enumerate(vel)]
    if rep and first:
        rhand[-1][1] = c
    return rhand, vel



def left(mid):
    lh1, vl1 = left_motif1(p)
    lh2, vl2 = left_motif2(p)
    for i in range(2):
        lhand1, vl1 = left_motif1(mf)
        lhand2, vl2 = left_motif2(mf)
        lh1 += lhand1
        lh2 += lhand2
    lhand1, vl1 = left_motif1(p)
    lhand2, vl2 = left_motif2(p)
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(mf)
    lhand2, vl2 = left_motif2(mf)
    lh1 += lhand1
    lh2 += lhand2
    for i in range(2):
        lhand1, vl1 = left_motif1(mf, vel_init=vl1[-1])
        lhand2, vl2 = left_motif2(mf, vel_init=vl2[-1])
        lh1 += lhand1
        lh2 += lhand2
    lhand1, vl1 = left_motif1(p)
    lhand2, vl2 = left_motif2(p)
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(p, vl1[-1])
    lhand2, vl2 = left_motif2(p, vl2[-1])
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(p, vl1[-1])
    lhand2, vl2 = left_motif2(p, vl2[-1])
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(mf)
    lhand2, vl2 = left_motif2(mf)
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(p, vel_init=vl1[-1], second_nuance=mf)
    lhand2, vl2 = left_motif2(p, vel_init=vl2[-1], second_nuance=mf)
    lh1 += lhand1
    lh2 += lhand2
    lhand1, vl1 = left_motif1(p, vel_init=vl1[-1], second_nuance=mf)
    lhand2, vl2 = left_motif2(p, vel_init=vl2[-1], second_nuance=mf)
    lhand1[-2][1] = w
    lh1 += lhand1[:-1] + [["e3 b3 e4", w, rd.randint(pp[0], pp[1])]]
    lhand2[-2][1] = b
    lh2 += lhand2[:-1]
    trkl1 = lib.notes2trk(lh1)
    trkl2 = lib.notes2trk(lh2)
    mid.tracks.append(trkl1)
    mid.tracks.append(trkl2)
    return mid


def right(mid):
    rh = [['s', 8*w]]
    rh_t, vel = right_motif1(mf)
    rh += rh_t
    rh_t, vel = right_motif1(mf, vel_init=vel[-1])
    rh += rh_t
    rh_t, vel = right_motif2(p, mf, vel_init=vel[-1])
    rh += rh_t
    rh_t, vel = right_motif3(mf, vel_init=vel[-1], first=True, rep=False)
    rh += rh_t
    rh_t, vel = right_motif3(mf, vel_init=vel[-1], first=True, rep=True)
    rh += rh_t
    rh_t, vel = right_motif1(p, vel_init=vel[-1], second=True)
    rh += rh_t
    rh_t, vel = right_motif1(p, vel_init=vel[-1], second=True)
    rh += rh_t
    rh_t, vel = right_motif2(p, mp, vel_init=vel[-1], second=True)
    rh += rh_t
    rh_t, vel = right_motif3(p, vel_init=vel[-1], first=False, rep=False,
                             second_nuance=mf)
    rh += rh_t
    rh_t, vel = right_motif3(p, vel_init=vel[-1], first=False, rep=True,
                             second_nuance=mf)
    rh += rh_t + [["g5 b5 e6", w, rd.randint(pp[0], pp[1])]]
    trkr = lib.notes2trk(rh)
    mid.tracks.append(trkr)
    return mid


def tempo(mid):
    beats = [rd.randint(600000, 700000)]
    beats += lib.rand_ev(600000, 700000, 6*16+11, 10000, seed=beats[-1])
    beats += lib.rand_ev(650000, 700000, 4, 10000, seed=beats[-1], dec=False)
    beats += [rd.randint(600000, 700000)]
    beats += lib.rand_ev(600000, 700000, 5*16+11, 10000, seed=beats[-1])
    beats += lib.rand_ev(1800000, 2500000, 4, 100000, seed=beats[-1], dec=False)
    trk_tempo = lib.tempo(beats)
    mid.tracks.append(trk_tempo)
    return mid


def song(n="Comptine1", ticks_per_beat=b):
    """Create the Audiosegment"""
    mid = MidiFile()
    mid.ticks_per_beat = ticks_per_beat
    mid = left(mid)
    mid = right(mid)
    mid = tempo(mid)
    mid.save("I" + n + ".mid")
    return lib.mid2aud("I" + n) + 10


silence = AudioSegment.silent(duration=2000)
out = silence

for i in range(5):
    out += song(n) + silence

out.export("Comptine.wav")
