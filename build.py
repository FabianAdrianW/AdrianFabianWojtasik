"""Skleja src/head.html + src/body.html w index.html (wersja produkcyjna) i preview.html (podgląd artefaktu)."""
from pathlib import Path
root = Path(__file__).parent
head = (root / "src/head.html").read_text(encoding="utf-8")
body = (root / "src/body.html").read_text(encoding="utf-8")
(root / "index.html").write_text(
    '<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html gotowy")
