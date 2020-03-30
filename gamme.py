from mido import Message, MidiFile, MidiTrack
from lib import mid2aud, interpret
from pydub.playback import play
from pydub import AudioSegment
import numpy as np
import numpy.random as rd

def velocity_r(trk, t_vel, r, on=True):
    """Randomly change the velocity of a note in a track"""
    time = 0
    j = 0
    c_t_vel = t_vel[j][0]
    if on:
        msg_t = "note_on"
    else:
        msg_t = "note_off"
    for msg in trk:
        if msg.type == msg_t:
            r_mod = c_t_vel*r
            msg.velocity = rd.randint(max(c_t_vel - r_mod, 0),
                                          min(c_t_vel + r_mod, 127))
            if time > t_vel[j][1]:
                j += 1
                time = 0
            c_t_vel = t_vel[j][0]
        time += msg.time
    return trk



def scale_Cmaj_mid():
    """Build the Cmaj Scale midi file with two tracks right and left hand"""
    mid = MidiFile()
    track_r = MidiTrack()
    track_l = MidiTrack()
    gamme_n = [60, 62, 64, 65, 67, 69, 71, 72]
    gamme_rev = [i for i in gamme_n]
    gamme_rev.reverse()
    gamme_n += gamme_rev
    for n in gamme_n:
        track_r.append(Message('note_on', note=n, velocity=100, time=0))
        track_r.append(Message('note_off', note=n, velocity=64,
                               time=mid.ticks_per_beat))
    for n in gamme_n:
        track_l.append(Message('note_on', note=n-12, velocity=100, time=0))
        track_l.append(Message('note_off', note=n-12, velocity=64,
                               time=mid.ticks_per_beat
))
    mid.tracks.append(track_r)
    mid.tracks.append(track_l)
    return mid


n = "scale"
silence = AudioSegment.silent(duration=1000)
out = silence
for i in range(1):
    mid = scale_Cmaj_mid()
    beat_ints = [600000 for i in range(15)]
    rs = [0.2 for i in range(15)]
    t_vel = [(int(i), mid.ticks_per_beat) for i in np.linspace(10, 125, 15)]
    vols = [100 for i in range(15)]
    mid.tracks[0] = velocity_r(mid.tracks[0], t_vel, 0.1, on=True)
    #mid.tracks[0] = velocity_r(mid.tracks[0], t_vel, 0.1, on=False)
    mid.tracks[1] = velocity_r(mid.tracks[1], t_vel, 0.1, on=True)
    #mid.tracks[1] = velocity_r(mid.tracks[1], t_vel, 0.1, on=False)
    #mid = interpret(mid, beat_ints, rs, vols)
    mid.save("I" + n + ".mid")
    out += mid2aud("I" + n) + silence

play(out)
