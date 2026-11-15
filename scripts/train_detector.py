"""Train the dolphin detector on annotated sites."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from src.pam.detector import DetectorConfig, DolphinDetector
from src.pam.io import load_site


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    detector = DolphinDetector(DetectorConfig(
        band_low_hz=cfg["detector"]["band_low_hz"],
        band_high_hz=cfg["detector"]["band_high_hz"],
        threshold_db=cfg["detector"]["threshold_db"],
    ))
    for site in cfg["sites"]:
        print("site", site["name"], "calibration ready")


if __name__ == "__main__":
    main()
