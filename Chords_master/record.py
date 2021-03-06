"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import variables as var

CHUNK = var.CHUNK
FORMAT = pyaudio.paInt16
CHANNELS = var.CHANNELS
RATE = var.RATE

RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "AudioFiles/G_m.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()