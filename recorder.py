import sounddevice as sd
import numpy as np
import lameenc

def recorder(duration=7, filename="89.mp3", sample_rate=44100, channels=1):
    print("🎙️ Recording... Speak now.")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait()
    print("✅ Recording complete.")

    pcm_data = recording.astype(np.int16).tobytes()

    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)

    mp3_data = encoder.encode(pcm_data)
    mp3_data += encoder.flush()

    with open(filename, "wb") as f:
        f.write(mp3_data)

    print(f"📁 Saved ")

if __name__ == "__main__":
    recorder()
