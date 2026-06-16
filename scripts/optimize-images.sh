#!/bin/bash
# Regenerate WebP assets in assets/imgs/opt/ after replacing source PNGs.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/assets/imgs"
OUT="$SRC/opt"
mkdir -p "$OUT"

hero_files=(
  "样片_全能400_01.png:hero-01.webp"
  "样片_全能400_02.png:hero-02.webp"
  "样片_全能400_03.png:hero-03.webp"
  "样片_Lomo800_01.png:hero-04.webp"
  "样片_Lomo800_02.png:hero-05.webp"
  "样片_Lomo800_03.png:hero-06.webp"
  "样片_5219_01.png:hero-07.webp"
  "样片_5219_02.png:hero-08.webp"
  "样片_5219_03.png:hero-09.webp"
  "样片_5207_01.png:hero-10.webp"
  "样片_5207_02.png:hero-11.webp"
  "样片_5207_03.png:hero-12.webp"
  "样片_欠曝样片_01.png:hero-13.webp"
  "样片_欠曝样片_02.png:hero-14.webp"
)

for entry in "${hero_files[@]}"; do
  IFS=: read -r src dst <<< "$entry"
  cwebp -quiet -q 80 -resize 1400 0 "$SRC/$src" -o "$OUT/$dst"
done

cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-positive.png" -o "$OUT/feature-positive.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-negative.png" -o "$OUT/feature-negative.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-hasselblad-1.png" -o "$OUT/feature-hasselblad-1.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-hasselblad-3.png" -o "$OUT/feature-hasselblad-3.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-border-no-margin.png" -o "$OUT/feature-border-no-margin.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-border-with-margin.png" -o "$OUT/feature-border-with-margin.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-keyboard.png" -o "$OUT/feature-keyboard.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-exif-hdr.png" -o "$OUT/feature-exif-hdr.webp"
cwebp -quiet -q 82 -resize 1600 0 "$SRC/feature-copy-paste.png" -o "$OUT/feature-copy-paste.webp"
cwebp -quiet -q 80 -resize 1920 0 "$SRC/downloadbg.png" -o "$OUT/downloadbg.webp"
cwebp -quiet -q 90 -resize 128 0 "$SRC/icon_128x128@2x.png" -o "$OUT/icon.webp"

echo "Done. Output: $OUT ($(du -sh "$OUT" | cut -f1))"
