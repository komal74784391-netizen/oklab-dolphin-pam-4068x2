"""Spectrogram and band-energy features used by the detector."""
from __future__ import annotations

import numpy as np


def frame_signal(audio: np.ndarray, win: int = 1024, hop: int = 512) -> np.ndarray:
    if len(audio) < win:
        audio = np.pad(audio, (0, win - len(audio)))
    count = 1 + (len(audio) - win) // hop
    idx = np.arange(win)[None, :] + hop * np.arange(count)[:, None]
    return audio[idx]


def spectrogram(audio: np.ndarray, win: int = 1024, hop: int = 512) -> np.ndarray:
    frames = frame_signal(audio, win, hop) * np.hanning(win)
    spec = np.abs(np.fft.rfft(frames, axis=1)) ** 2
    return 10.0 * np.log10(spec + 1e-12)


def band_energy(spec: np.ndarray, rate: int, low: float, high: float, win: int = 1024) -> np.ndarray:
    freqs = np.fft.rfftfreq(win, d=1.0 / rate)
    mask = (freqs >= low) & (freqs <= high)
    return spec[:, mask].mean(axis=1) if mask.any() else np.zeros(spec.shape[0])
