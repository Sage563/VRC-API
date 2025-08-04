import torchaudio
from transformers import pipeline

# Load the detector pipeline (only once)
detector = pipeline("audio-classification", model="MattyB95/AST-VoxCelebSpoof-Synthetic-Voice-Detection")

def isai(audio_path: str, threshold: float = 0.5) -> bool:
    try:
        waveform, sr = torchaudio.load(audio_path)
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)
        required_sr = detector.feature_extractor.sampling_rate
        if sr != required_sr:
            resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=required_sr)
            waveform = resampler(waveform)
        audio_input = waveform.squeeze().numpy()
        result = detector(audio_input)[0]
        is_ai = result["score"] >= threshold and result["label"].lower().startswith("synthetic")

        return is_ai 

    except Exception as e:
        print(f"❌ Error detecting voice type: {e}")
        return False  
