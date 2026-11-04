# mogetopomoge.pl

Lead page Adriana Fabiana Wojtasika: darmowe strony, aplikacje, programy i automatyzacje dla firm z okolic wschodniego Wrocławia (jeden projekt w miesiącu).

## Struktura

- `index.html` – gotowa strona (jeden plik, bez frameworka)
- `img/` – zdjęcia w WebP + `og.jpg` do podglądu linku
- `src/head.html`, `src/body.html` – źródła; po edycji uruchom `python build.py`, żeby odświeżyć `index.html`
- `netlify.toml` – konfiguracja hostingu

## Wdrożenie

Netlify: podłącz repo, katalog publikacji `.`. Formularz kontaktowy działa przez Netlify Forms (`name="kontakt"`), zgłoszenia przychodzą na e-mail ustawiony w panelu Netlify (Forms → Notifications).

## Kolejka darmowych projektów

W `src/body.html` zmień `FREE_TAKEN_UNTIL`:
- `0` – bieżący miesiąc zajęty, następny wolny
- `1` – bieżący i następny zajęte

Miesiące liczą się automatycznie z daty.
