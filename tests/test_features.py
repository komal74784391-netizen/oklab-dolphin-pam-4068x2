import numpy as np

from src.pam.features import band_energy, spectrogram


def test_spectrogram_shape():
    audio = np.zeros(48000, dtype=np.float32)
    spec = spectrogram(audio)
    assert spec.ndim == 2


def test_band_energy_positive():
    audio = np.random.randn(48000).astype(np.float32)
    spec = spectrogram(audio)
    energy = band_energy(spec, 48000, 2000, 16000)
    assert energy.shape[0] == spec.shape[0]
