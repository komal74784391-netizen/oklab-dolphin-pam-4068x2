"""Click/whistle detector with bandwidth-aware thresholding."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .features import band_energy, spectrogram


@dataclass
class DetectorConfig:
    band_low_hz: float = 2000.0
    band_high_hz: float = 16000.0
    threshold_db: float = 12.0


class DolphinDetector:
    def __init__(self, cfg: DetectorConfig | None = None) -> None:
        self.cfg = cfg or DetectorConfig()

    def activities(self, audio: np.ndarray, rate: int) -> np.ndarray:
        spec = spectrogram(audio)
        energy = band_energy(
            spec, rate, self.cfg.band_low_hz, self.cfg.band_high_hz
        )
        baseline = np.median(energy)
        return (energy - baseline) > self.cfg.threshold_db

    def activity_budget(self, audio: np.ndarray, rate: int) -> float:
        flags = self.activities(audio, rate)
        return float(flags.mean()) if flags.size else 0.0
