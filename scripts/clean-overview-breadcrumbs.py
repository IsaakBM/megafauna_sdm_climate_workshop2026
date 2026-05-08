#!/usr/bin/env python3
from pathlib import Path
import re


ROOT = Path("/Users/ibrito/Desktop/megafauna_sdm_climate_workshop2026/docs")
TARGETS = [
    ROOT / "agenda" / "index.html",
    ROOT / "agenda" / "index_es.html",
    ROOT / "resources" / "materials.html",
    ROOT / "resources" / "materials_es.html",
]

PATTERN = re.compile(
    r'(\s*<nav class="quarto-page-breadcrumbs" aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item">.*?</li></ol></nav>\s*)',
    re.DOTALL,
)


def clean_file(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = PATTERN.sub("", text, count=1)
    path.write_text(text, encoding="utf-8")


for target in TARGETS:
    clean_file(target)
