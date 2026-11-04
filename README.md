# mogetopomoge.pl

Lead page Adriana Fabiana Wojtasika: darmowe strony, aplikacje, programy i automatyzacje dla firm z okolic wschodniego Wrocławia (jeden projekt w miesiącu).

## Struktura

- `index.html` – gotowa strona (jeden plik, bez frameworka)
- `img/` – zdjęcia w WebP + `og.jpg` do podglądu linku
- `src/head.html`, `src/body.html` – źródła; po edycji uruchom `python build.py`, żeby odświeżyć `index.html`
- `netlify.toml` – konfiguracja hostingu

## Wdrożenie

Działa na każdym hostingu (Netlify, GitHub Pages, zwykły serwer). Formularz wysyła zgłoszenia przez FormSubmit na adres z `FORM_EMAIL` w `src/body.html`. Przy pierwszym wysłaniu FormSubmit przysyła mail aktywacyjny – kliknij link, od tej pory zgłoszenia przychodzą normalnie.

## Kolejka darmowych projektów

W `src/body.html` zmień `FREE_TAKEN_UNTIL`:
- `-1` – bieżący miesiąc wolny
- `0` – bieżący miesiąc zajęty, następny wolny
- `1` – bieżący i następny zajęte

Miesiące liczą się automatycznie z daty.
