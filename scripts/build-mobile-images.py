"""Regenerate mobile crops and posters after changing the website artwork."""
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'docs/media-manifest.json').read_text())
for slide in manifest['hero']:
    source = ROOT / slide['asset']
    with Image.open(source) as original:
        # Same centered cover composition as the portrait hero, without
        # transmitting the sides of a landscape frame that the phone clips.
        width = min(600, round(800 * original.width / original.height))
        crop = ImageOps.fit(original, (width, 800), method=Image.Resampling.LANCZOS)
        crop.save(source.with_stem(source.stem + '-mobile'), quality=77, method=6)

for source in sorted((ROOT / 'assets/media/film-convert').glob('*-[0-9][0-9].webp')):
    with Image.open(source) as poster:
        poster.thumbnail((720, 960), Image.Resampling.LANCZOS)
        poster.save(source.with_stem(source.stem + '-mobile'), quality=81, method=6)
