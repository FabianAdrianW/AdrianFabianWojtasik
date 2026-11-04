# mogetopomoge.pl

Lead page Adriana Fabiana Wojtasika: darmowe strony, aplikacje, programy i automatyzacje dla firm z okolic wschodniego Wrocławia (jeden projekt w miesiącu).

## Struktura

- `index.html` – gotowa strona (jeden plik, bez frameworka)
- `img/` – zdjęcia w WebP + `og.jpg` do podglądu linku
- `src/head.html`, `src/body.html` – źródła; po edycji uruchom `python build.py`, żeby odświeżyć `index.html`
- `netlify.toml` – konfiguracja hostingu

## Wdrożenie

Strona stoi na Netlify (projekt `mogetopomoge`). Formularz działa przez Netlify Forms (`name="kontakt"`); zgłoszenia widać w panelu Netlify: Forms → kontakt. Powiadomienie e-mail ustawia się raz: Forms → Form notifications → Add notification → Email.

Na innych hostingach (np. GitHub Pages) formularz wysyła przez FormSubmit na adres z `FORM_EMAIL` w `src/body.html`.

## Kolejka darmowych projektów

W `src/body.html` zmień `FREE_TAKEN_UNTIL`:
- `-1` – bieżący miesiąc wolny
- `0` – bieżący miesiąc zajęty, następny wolny
- `1` – bieżący i następny zajęte

Miesiące liczą się automatycznie z daty.
