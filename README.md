# erling

A shot map of Erling Haaland's Premier League 2022-23 shots, built with [mplsoccer](https://mplsoccer.readthedocs.io/).

The script loads Understat shot data from GitHub. It plots each shot on a half pitch, with marker size showing xG and red markers for goals. It also shows total shots, goals, xG, xG per shot and average shot distance.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14+.

```sh
uv sync
```

## Run

```sh
uv run src/athletic_shotmap_erling.py
```

The first run downloads the Arvo font (`Arvo-Regular.ttf`). The chart is saved as `erling_haaland_2022.png` and opens in a window.
