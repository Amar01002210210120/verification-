#!/usr/bin/env bash
set -e
python code/src/download_subset.py
python code/src/train.py
python code/src/eval_conformal.py
pytest -q
