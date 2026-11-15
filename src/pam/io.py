"""Audio and annotation loading helpers."""
from __future__ import annotations

import wave
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy as np


@dataclass
class Segment:
    path: Path
    audio: np.ndarray
    sample_rate: int


def read_wav(path: Path) -> Tuple[np.ndarray, int]:
    with wave.open(str(path), "rb") as handle:
        rate = handle.getframerate()
        frames = handle.readframes(handle.getnframes())
        audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32)
    return audio / 32768.0, rate


def load_site(path: Path, max_minutes: int = 60) -> List[Segment]:
    segments: List[Segment] = []
    for wav in sorted(path.glob("*.wav")):
        audio, rate = read_wav(wav)
        audio = audio[: rate * 60 * max_minutes]
        segments.append(Segment(path=wav, audio=audio, sample_rate=rate))
    return segments
