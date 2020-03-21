from mido import MidiFile, MidiTrack
from lib import velocity_r, tempo_r, mid2aud
# import numpy as np
# import numpy.random as rd
from pydub import AudioSegment
from pydub.playback import play

n = "test"
mid_in = MidiFile(n + ".mid")
trkr = mid_in.tracks[1]
trkl = mid_in.tracks[2]

beats = [700000 for i in range(200)]
rs = [0.08*1 for j in range(200)] # Given my count there are 144 measures
mid = MidiFile()
mid.ticks_per_beat = mid_in.ticks_per_beat
trkr = velocity_r(trkr, 80, 0.1)
trkl = velocity_r(trkl, 70, 0.1)
mid.tracks.append(trkr)
mid.tracks.append(trkl)
mid = tempo_r(mid, beats, rs)
mid.save("I" + n + ".mid")
out = mid2aud("I" + n)
out.export("I" + n + ".wav")
play(out)
