# MIP 2027 · Iowa City Local Guide

Interactive local guide for the Mixed Integer Programming Workshop, University of Iowa, May 25–28, 2027.

**Live guide:** https://mip2027-iowa-city-guide.qiluo-email.chatgpt.site

## Explore

- Conference venues: **Tippie College of Business (Pappajohn Business Building)** and **Graduate by Hilton Iowa City**.
- 42 places and event listings, including 18 restaurants and 10 cafés.
- Numbered, colored map pins synchronized with place lists.
- Category, neighborhood, cuisine, and text filters.
- Directions, official information, and a dining table that stacks on phones.

The 10 restaurant and café additions were checked directly on Google Maps on November 12, 2026. Their ratings were 4.4–4.9, above the requested 3.5 threshold. Rating links, review counts, and check dates appear in the guide. Ratings and event schedules may change; unconfirmed programs remain labeled.

## Run locally

No build or dependency installation is required. From the project directory:

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000 in a browser. Map tiles require an internet connection.

## Validate

Requires Python 3 and Node.js:

```sh
python3 check_guide.py
```

The check covers data and list consistency, venue labels, coordinates, Google rating evidence for the additions, unique IDs, links, and JavaScript syntax. Browser checks covered map rendering, category and combined filters, search and reset, event details, rating popups, and 390px/320px layouts without horizontal page overflow.

## Files

- `dist/index.html`: complete static guide, including Leaflet, styles, place data, map interactions, list, and dining table.
- `dist/assets/mip-2027.jpg`: supplied MIP 2027 logo.
- `restaurant-rating-sources.json`: direct Google Maps rating sources for the 10 additions.
- `check_guide.py`: runnable consistency and syntax checks.

The public GitHub project is a source copy. Its files do not configure GitHub Pages or change the existing hosted guide automatically.

## Credits

Visual style follows https://www.mixedinteger.org/2027/ (logo yellow, black navigation, Arial typography, and gray/white sections). Logo design © Julia Silbermann; font credits: Cornerstone by Zac Freeland. Leaflet 1.9.4 retains its embedded license notice. Map tiles are supplied by Esri with attribution in the guide. Directions open Google Maps. No visitor information is stored by the guide.
