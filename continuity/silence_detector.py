import librosa
import numpy as np
import subprocess
import os

def detect_silence_regions(audio_path, cfg):
    y, sr = librosa.load(audio_path, sr=16000)
    rms = librosa.feature.rms(y=y)[0]
    times = librosa.frames_to_time(np.arange(len(rms)), sr=sr)

    silence = rms < librosa.db_to_amplitude(cfg["audio"]["silence_db"])

    regions = []
    start = None

    for t, s in zip(times, silence):
        if s and start is None:
            start = t
        elif not s and start is not None:
            if t - start >= cfg["audio"]["min_silence_sec"]:
                regions.append((start, t))
            start = None

    return regions
