import sounddevice
from scipy.io.wavfile import write

fs = 44100
second = 10

print("RECORDING....")

record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("Recorded.wav",fs,record_voice)