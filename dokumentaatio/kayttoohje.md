# Käyttöohje

Lataa pelin viimeisimmän [releasen](https://github.com/HYTApio/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa _.env_-tiedostossa. Tiedostot luodaan automaattisesti _data_-hakemistoon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```
SCORES_FILENAME=scores.csv
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelin aloitus

Sovellus käynnistyy main menu näkymään:

Siinä painamalla mitä tahansa nappia Tetris peli alkaa

## Pelaaminen

Peliä pelataan nuoli näppäimillä.

Painamalla ylöspäin nuolea alas tippuva pala kääntyy 90 astetta.

Painamalla alaspäin nuolea alas tippuva pala menee 1 neliön alaspäin.

Painamalla oikeaa tai vasenta nuolta, pala liikkuu nuolen suuntaan yhden neliön.

## Pelin tarkoitus

Pelin tarkoitus on tyhjentää pelialueen rivejä mahdollisimman paljon. Rivejä tyhjennetään täyttämällä kokonainen vaaka rivi paloilla. Peli loppuu kun tippuva pala ei enää mahdu pelialueelle. 
