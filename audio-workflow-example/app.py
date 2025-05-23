import librosa
import numpy as np
import json
import os
from glob import glob

# === Workflow Step 1: Gather all audio files ===
audio_dir = '../audio'
audio_files = glob(os.path.join(audio_dir, '*.mp3')) + glob(os.path.join(audio_dir, '*.wav'))

if not audio_files:
    print("No audio files found in the directory.")
    exit()

# Store summaries for all audio files
all_summaries = []

# === Workflow Step 2: Process each audio file ===
for audio_path in audio_files:
    try:
        # Load audio
        y, sr = librosa.load(audio_path)

        # Beat tracking
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)
        avg_beat_time = float(np.mean(beat_times)) if len(beat_times) > 0 else 0.0

        # Chroma features (shifted)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_shifted = np.roll(chroma, shift=2, axis=0)
        avg_chroma = float(np.mean(chroma_shifted))

        # MFCCs
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        avg_mfcc = float(np.mean(mfcc))

        # === Workflow Step 3: Structure the data ===
        summary = {
            "file": os.path.basename(audio_path),
            "tempo": float(tempo),
            "avg_beat_time": avg_beat_time,
            "avg_chroma_intensity": avg_chroma,
            "avg_mfcc_value": avg_mfcc
        }

        all_summaries.append(summary)
        print(f"Processed: {os.path.basename(audio_path)}")

    except Exception as e:
        print(f"Error processing {audio_path}: {e}")

# === Workflow Step 4: Export summary data for D3 visualization ===
with open('audio_feature_summary.json', 'w') as f:
    json.dump(all_summaries, f, indent=2)

print("\nAll features exported to 'audio_feature_summary.json'")
