"""Site-level precision/recall evaluation table."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from src.pam.detector import DetectorConfig, DolphinDetector


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    detector = DolphinDetector(DetectorConfig(**cfg["detector"]))
    for site in cfg["sites"]:
        print(f"{site['name']}: precision=0.0 recall=0.0 (placeholder report)")
    print("detector", type(detector).__name__)


if __name__ == "__main__":
    main()
