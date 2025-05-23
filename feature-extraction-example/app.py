import librosa
import numpy as np
import json
import os
from glob import glob

# Directory containing audio files
audio_dir = '../audio'
audio_files = glob(os.path.join(audio_dir, '*.wav')) + glob(os.path.join(audio_dir, '*.mp3'))

# Collect summaries for each file
all_summaries = []

for audio_path in audio_files:
    try:
        # Load audio
        y, sr = librosa.load(audio_path)

        # Beat tracking
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)

        # Chroma features
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_shifted = np.roll(chroma, shift=2, axis=0)
        avg_chroma = float(np.mean(chroma_shifted))

        # MFCCs
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        avg_mfcc = float(np.mean(mfcc))

        # Summarize this file
        feature_summary = {
            "file": os.path.basename(audio_path),
            "tempo": float(tempo),
            "avg_chroma_intensity": avg_chroma,
            "avg_mfcc_value": avg_mfcc
        }

        all_summaries.append(feature_summary)
        print(f"Processed: {audio_path}")

    except Exception as e:
        print(f"Error processing {audio_path}: {e}")

# Write all summaries to a JSON file
with open('audio_feature_summary.json', 'w') as f:
    json.dump(all_summaries, f, indent=2)

print("All average audio features written to audio_feature_summary.json")
