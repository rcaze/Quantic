from mido import MidiFile, MidiTrack
from lib import velocity_r, tempo_r, mid2aud, add_notes, add_couples
# import numpy as np
# import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play


def first_partr(trk, bt):
    bl = bt
    cr = bt/2
    w = bt*2
    r = bt*4
    bl, cr, w, r = int(bl), int(cr), int(w), int(r)

    trk = add_notes(trk, [[-1], [60], [65], [68], [65]],
                    [cr, cr, cr, cr, w + cr])
    trk = add_notes(trk, [[61], [65], [68], [60], [65], [68]],
                    [cr, cr, bl, cr, cr, bl])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, w + cr])
    trk = add_notes(trk, [[56], [61], [65], [60]], [cr, cr, cr, w + cr])
    trk = add_notes(trk, [[65], [68], [65]], [cr, cr, cr + w])
    trk = add_notes(trk, [[-1], [61], [65], [68], [60], [65], [68]],
                    [cr, cr, cr, bl, cr, cr, bl])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, w + cr])
    trk = add_notes(trk, [[56], [61], [65], [60]], [cr, cr, cr, w + cr])
    trk = add_notes(trk, [[65], [68], [65]], [cr, cr, cr + w])
    trk = add_notes(trk, [[60], [65], [68], [65]], [cr, cr, cr, cr + w])
    trk = add_notes(trk, [[61], [65], [68], [60], [65], [68]],
                    [cr, cr, bl, cr, cr, bl])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, cr + w + r])
    trk = add_notes(trk, [[58], [65], [68], [65]], [cr, cr, cr, cr + w + r])
    trk = add_notes(trk, [[58], [63], [67], [63]],
                    [cr, cr, cr, cr + w + r + r])
    return trk


def d_croche(trk, bt, pattern, nb=4):
    """Generate a pattern of double croches"""
    cc = int(bt/4)
    pat = []
    for i in range(nb):
        pat += pattern
    trk = add_notes(trk, pat, [cc for i in range(4*nb)])
    return trk


def d_crochesr(trk, bt):
    """Generate the ddcroches for the right hand"""
    for i in range(2):
        trk = d_croche(trk, bt, [[68], [60], [68-12], [60]])
        trk = d_croche(trk, bt, [[68], [61], [68-12], [61]], nb=2)
        trk = d_croche(trk, bt, [[68], [60], [68-12], [60]], nb=2)
        trk = d_croche(trk, bt, [[67], [60], [67-12], [60]])
        trk = d_croche(trk, bt, [[65], [60], [65-12], [60]])

    for i in range(2):
        trk = d_croche(trk, bt, [[68], [60], [68-12], [60]])
        trk = d_croche(trk, bt, [[68], [61], [68-12], [61]], nb=2)
        trk = d_croche(trk, bt, [[68], [60], [68-12], [60]], nb=2)
        trk = d_croche(trk, bt, [[67], [63], [70-12], [63]])
        trk = d_croche(trk, bt, [[67], [63], [70-12], [63]])

    for i in range(2):
        trk = d_croche(trk, bt, [[65], [70-12], [65-12], [70-12]])
        trk = d_croche(trk, bt, [[65], [70-12], [65-12], [70-12]])
        trk = d_croche(trk, bt, [[67], [63], [70-12], [63]])
        trk = d_croche(trk, bt, [[67], [63], [70-12], [63]])

    return trk


def d_crochesl(trk, bt):
    """Generate the croches for the left hand"""
    for i in range(2):
        trk = d_croche(trk, bt, [[65-24], [60-12], [65-12], [60-12]])
        trk = d_croche(trk, bt, [[65-24], [61-12], [65-12], [61-12]], nb=2)
        trk = d_croche(trk, bt, [[65-24], [60-12], [65-12], [60-12]], nb=2)
        trk = d_croche(trk, bt, [[63-24], [58-12], [63-12], [58-12]])
        trk = d_croche(trk, bt, [[61-24], [56-12], [61-12], [56-12]])

    for i in range(2):
        trk = d_croche(trk, bt, [[65-24], [60-12], [65-12], [60-12]])
        trk = d_croche(trk, bt, [[65-24], [61-12], [65-12], [61-12]], nb=2)
        trk = d_croche(trk, bt, [[65-24], [60-12], [65-12], [60-12]], nb=2)
        trk = d_croche(trk, bt, [[63-24], [58-12], [63-12], [58-12]])
        trk = d_croche(trk, bt, [[63-24], [58-12], [63-12], [58-12]])

    for i in range(2):
        trk = d_croche(trk, bt, [[70-36], [65-24], [70-24], [65-24]])
        trk = d_croche(trk, bt, [[61-24], [68-24], [61-12], [68-24]])
        trk = d_croche(trk, bt, [[63-24], [58-12], [63-12], [58-12]])
        trk = d_croche(trk, bt, [[63-24], [58-12], [63-12], [58-12]])
    return trk


def motif0(trk, n, bt, l):
    trk = add_notes(trk, [[n]], [2*bt])
    trk = add_couples(trk, [n-12], [[-1]] + [[n] for i in range(l-1)],
                      [bt for i in range(l)])
    return trk


def motif1(trk, bt, notes, nb):
    """Produce the first motif"""
    c = int(bt/2)
    cc = int(bt/4)
    for i in range(nb):
        trk = add_notes(trk, notes, [c, cc, cc, cc, cc, c])
    return trk


def motif1r(trk, bl):
    for i in range(2):
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [60+12]], nb=2)
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [61+12]], nb=1)
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [60+12]], nb=1)
        trk = motif1(trk, bl, [[63], [63], [67], [-1], [67], [60+12]], nb=2)
        trk = motif1(trk, bl, [[61], [61], [65], [-1], [65], [60+12]], nb=2)

    for i in range(2):
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [60+12]], nb=2)
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [61+12]], nb=1)
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [60+12]], nb=1)
        trk = motif1(trk, bl, [[63], [63], [67], [-1], [67], [60+12]], nb=4)

    for i in range(2):
        trk = motif1(trk, bl, [[65], [65], [70], [-1], [70], [60+12]], nb=4)
        trk = motif1(trk, bl, [[63], [63], [70], [-1], [70], [61+12]], nb=4)

    return trk


def motif2(trk, bt, ns, nb):
    """Produce the first motif"""
    c = int(bt/2)
    cc = int(bt/4)
    for i in range(nb):
        trk = add_notes(trk, [ns[0], ns[0], ns[1], ns[0], ns[1], ns[2]],
                        [c, cc, c, cc, cc, cc])
    return trk


def motif2r(trk, bl):
    for i in range(2):
        trk = motif2(trk, bl, [[65], [70], [60+12]], nb=2)
        trk = motif2(trk, bl, [[65], [70], [61+12]], nb=1)
        trk = motif2(trk, bl, [[65], [70], [60+12]], nb=1)
        trk = motif2(trk, bl, [[63], [67], [60+12]], nb=2)
        trk = motif2(trk, bl, [[61], [65], [60+12]], nb=2)

    for i in range(2):
        trk = motif2(trk, bl, [[65], [70], [60+12]], nb=2)
        trk = motif2(trk, bl, [[65], [70], [61+12]], nb=1)
        trk = motif2(trk, bl, [[65], [70], [60+12]], nb=1)
        trk = motif2(trk, bl, [[63], [70], [61+12]], nb=4)

    for i in range(2):
        trk = motif2(trk, bl, [[65], [70], [60+12]], nb=4)
        trk = motif2(trk, bl, [[63], [70], [61+12]], nb=4)

    return trk


def motifl(trk, bt, notes, nb):
    """Produce the first motif"""
    c = int(bt/2)
    for i in range(nb):
        trk = add_notes(trk, notes, [c, c])
    return trk


def motifls(trk, bt):
    for j in range(2):
        trk = motifl(trk, bt, [[65-24], [60-12, 65-12]], nb=4)
        trk = motifl(trk, bt, [[65-24], [61-12, 65-12]], nb=2)
        trk = motifl(trk, bt, [[65-24], [60-12, 65-12]], nb=2)
        trk = motifl(trk, bt, [[63-24], [70-24, 63-12]], nb=4)
        trk = motifl(trk, bt, [[61-24], [68-24, 61-12]], nb=4)

    for j in range(2):
        trk = motifl(trk, bt, [[65-24], [60-12, 65-12]], nb=4)
        trk = motifl(trk, bt, [[65-24], [61-12, 65-12]], nb=2)
        trk = motifl(trk, bt, [[65-24], [60-12, 65-12]], nb=2)
        trk = motifl(trk, bt, [[63-24], [70-24, 63-12]], nb=8)

    for j in range(2):
        trk = motifl(trk, bt, [[70-36], [65-24, 70-24]], nb=4)
        trk = motifl(trk, bt, [[61-24], [68-24, 61-12]], nb=4)
        trk = motifl(trk, bt, [[63-24], [70-24, 63-12]], nb=8)

    return trk


def struggle_r(trk, bt):
    """Generate the first part of the right hand"""
    bl = bt
    cr = bt/2
    w = bt*2
    r = bt*4
    bl, cr, w, r = int(bl), int(cr), int(w), int(r)

    trk = add_notes(trk, [[60], [65], [68], [65]], [cr, cr, cr, cr + w])
    trk = add_notes(trk, [[61], [65], [68], [60], [65], [68]],
                    [cr, cr, bl, cr, cr, bl])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, cr + w + cr])
    trk = add_notes(trk, [[56], [61], [65], [60]], [cr, cr, cr, cr + w])
    trk = add_notes(trk, [[65], [68], [65]], [cr, cr, cr + w])
    trk = add_notes(trk, [[61], [65], [68], [60], [65], [68]],
                    [cr, cr, bl, cr, cr, bl])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, cr + w + r])
    trk = add_notes(trk, [[58], [65], [68], [65]], [cr, cr, cr, cr + w + r])
    trk = add_notes(trk, [[58], [63], [67], [63]], [cr, cr, cr, cr + w + r])

    trk = first_partr(trk, bt)

    trk = d_crochesr(trk, bt)

    trk = motif1r(trk, bt)

    trk = motif2r(trk, bt)

    trk = first_partr(trk, bt)

    trk = d_crochesr(trk, bt)

    return trk


def struggle_l(trk, bt):
    """Generate the first part of the right hand"""
    bl = bt
    cr = bt/2
    w = bt*2
    r = bt*4
    bl, cr, w, r = int(bl), int(cr), int(w), int(r)

    trk = add_notes(trk, [[-1] for i in range(12)], [r for i in range(12)])

    trk = add_notes(trk, [[65-12] for i in range(36)], [bl for i in range(36)])
    trk = motif0(trk, 65-12, bt, 6)
    trk = motif0(trk, 63-12, bt, 6)
    trk = motif0(trk, 70-24, bt, 6)
    trk = motif0(trk, 63-24, bt, 10)

    trk = d_crochesl(trk, bt)

    trk = motifls(trk, bt)

    trk = motifls(trk, bt)

    trk = add_notes(trk, [[53]], [bl])
    trk = add_couples(trk, [53-12], [[-1]] + [[53] for i in range(14)],
                      [bl for i in range(15)])
    trk = add_notes(trk, [[53]], [bl])
    trk = add_couples(trk, [53-12], [[-1]] + [[53], [53]],
                      [bl for i in range(3)])
    trk = add_couples(trk, [53-12], [[53] for i in range(12)],
                      [bl for i in range(12)])
    trk = add_notes(trk, [[53]], [bl])
    trk = add_couples(trk, [53-12], [[-1]] + [[53], [53]],
                      [bl for i in range(3)])
    trk = add_notes(trk, [[53]], [bl])
    trk = add_couples(trk, [53-12], [[-1]] + [[53] for i in range(6)],
                      [bl for i in range(7)])
    trk = add_notes(trk, [[63-12]], [bl])
    trk = add_couples(trk, [63-24], [[-1]] + [[63-12] for i in range(6)],
                      [bl for i in range(7)])
    trk = add_notes(trk, [[70-24]], [bl])
    trk = add_couples(trk, [70-24], [[-1]] + [[70-12] for i in range(6)],
                      [bl for i in range(7)])
    trk = add_notes(trk, [[63-12]], [bl])
    trk = add_couples(trk, [63-24], [[-1]] + [[63-12] for i in range(10)],
                      [bl for i in range(11)])

    trk = d_crochesl(trk, bt)

    return trk


n = "struggle"
beats = [530000 for i in range(12*4)]
beats += [490000 for i in range(8*4)]
beats += [470000 for i in range(8*4)]
beats += [450000 for i in range((148-28)*4)]
out = AudioSegment.silent(duration=1000)
for i in range(1, 4):
    mid = MidiFile()
    bt = mid.ticks_per_beat
    trkr = MidiTrack()
    trkl = MidiTrack()
    trkr = struggle_r(trkr, bt)
    trkl = struggle_l(trkl, bt)
    trkr = velocity_r(trkr, 100, 0.1)
    trkl = velocity_r(trkl, 80, 0.1)
    rs = [0.08*i for j in range(148*4)]  # Given my count there are 144 meas
    mid.tracks.append(trkr)
    mid.tracks.append(trkl)
    mid = tempo_r(mid, beats, rs)
    mid.save("I" + n + ".mid")
    out += mid2aud("I" + n)

out.export("I" + n + ".wav")
play(out)
