import numpy as np
import torchaudio
from resemblyzer import VoiceEncoder
from faster_whisper import WhisperModel
from difflib import SequenceMatcher
import os
import sys
import utills
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path
encoder = VoiceEncoder()


model_size = "base"
model = WhisperModel(model_size_or_path=model_size, device="cpu", compute_type="int8")

def load_mp3(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    waveform, sr = torchaudio.load(file_path)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)
    if sr != 16000:
        waveform = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)(waveform)
    return waveform.squeeze().numpy()

def transcribe(file_path):
    segments, _ = model.transcribe(file_path)
    return "".join(segment.text for segment in segments).strip().lower()

def texts_similar(a, b, threshold=0.85):
    return SequenceMatcher(None, a, b).ratio() >= threshold

def main(file1, file2, voice_threshold=0.7, text_threshold=0.85):
    wav1 = load_mp3(file1)
    wav2 = load_mp3(file2)
    emb1 = encoder.embed_utterance(wav1)
    emb2 = encoder.embed_utterance(wav2)
    voice_score = np.dot(emb1, emb2)

    text1 = transcribe(file1)
    text2 = transcribe(file2)

    # Uncomment for debugging:
    #print(f"Voice similarity: {voice_score:.3f}")
    #print(f"Text 1: {text1}")
    #print(f"Text 2: {text2}")

    tcharacters_to_remove = [",", "!", "."]
    for char in tcharacters_to_remove:
        text1 = text1.replace(char, "")
        text2 = text2.replace(char, "")

    voice_match = voice_score > voice_threshold
    text_match = texts_similar(text1, text2, threshold=text_threshold)
    
    if voice_score >=0.90:
        voice_match = True
    return voice_match and text_match

if __name__ == "__main__":
    file1 = "reference.mp3"
    file2 = "test.mp3"
    result = main(file1, file2)
    print("✅ Match result:", result)
