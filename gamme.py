from mido import Message, MidiFile, MidiTrack
from lib import mid2aud, interpret
from pydub.playback import play
from pydub import AudioSegment


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
        croche = int(mid.ticks_per_beat/2)
        track_l.append(Message('note_on', note=n-12, velocity=100, time=0))
        track_l.append(Message('note_off', note=n-12, velocity=64,
                               time=croche))
        track_l.append(Message('note_on', note=n-12, velocity=100, time=0))
        track_l.append(Message('note_off', note=n-12, velocity=64,
                               time=croche))
    mid.tracks.append(track_r)
    mid.tracks.append(track_l)
    return mid


n = "scale"
silence = AudioSegment.silent(duration=1000)
out = silence
for i in range(5):
    mid = scale_Cmaj_mid()
    beat_ints = [600000 for i in range(15)]
    rs = [0.2 for i in range(15)]
    vols = [100 for i in range(15)]
    mid = interpret(mid, beat_ints, rs, vols)
    mid.save("I" + n + ".mid")
    out += mid2aud("I" + n) + silence

play(out)
