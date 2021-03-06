# Ohjelmistotekniika, harjoitustyö

## Tetris

### Dokumentaatio ###
[Vaativuusmäärittely](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/HYTApio/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)



### Ohjelman asentaminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```

### Ohjelman aloittaminen

Ohjelman pystyy aloittamaan komennolla:

```bash
poetry run invoke start
```

### Ohjelman testaus

Testit pystyy suorittamaan komennolla:

```bash
poetry run invoke test
```

### Ohjelman testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti tulee _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
