# Passive acoustic monitoring of coastal dolphin foraging activity

Reference implementation and analysis pipeline for the paper
"Passive acoustic monitoring of coastal dolphin foraging activity"
(*Journal of Marine Acoustics*, 2019, DOI 10.7744/jma.2019.0142).

## Repository status

Released. The complete pipeline, trained detector weights and site-level
evaluation code are included in this repository.

## Layout

- `src/pam/io.py` - WAV/annotation loading helpers
- `src/pam/features.py` - spectrogram and band-energy features
- `src/pam/detector.py` - click and whistle detector with threshold calibration
- `scripts/train_detector.py` - train the detector on annotated sites
- `scripts/evaluate_sites.py` - site-level precision/recall table
- `configs/coastal_sites.yaml` - deployment configuration
- `tests/test_features.py`

## Quick start

```bash
pip install -r requirements.txt
python scripts/train_detector.py --config configs/coastal_sites.yaml
python scripts/evaluate_sites.py --config configs/coastal_sites.yaml
```

Code released under the MIT license. If you use it, please cite the paper.
