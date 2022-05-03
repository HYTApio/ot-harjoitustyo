# Arkkitehtuurikuvaus
## Rakenne
Ohjelman koodin pakkausrakenne:

Luo kuva :
ui -> services -> repositories -> objects
                  objects
Pakkaus ui sisältää käyttöliittymän koodia, services sisältää sovelluslogiikkaa, repositories tiedon tallennusta vastaavaa koodia. Objects sisältää pelin eri palaset.

## Käyttöliittymä
Pelissä on kolme eri ruutua:
* Aloitus näkymä
* Peli
* Häviönäyttö

## Sovelluslogiikka
Sovelluksen tietomallin muodostaa luokka Pieces. Pieces kuvaa jokaista palaa
```mermaid
 classDiagram
      class Pieces{
        x_row
        y_row
        rotation
        shape
        color
      }
```
Peli kulkee GameLoop luokan kautta josta kutsutaan eri funktioita.

## Tietojen pysyväistallennus
Pakkauksen _repositories_ `ScoreRepository` toteuttaa tiedon tallettamisen. Tieto tallennetaan CSV-tiedostoon. 
Sovelluksen juuressa on on tiedosto [konfiguraatiotiedosto .env](https://github.com/HYTApio/ot-harjoitustyo/blob/master/.env) joka määrittelee tallennetun tiedoston nimen
CSV-tiedostoon tallennetaan vain ainoastaan pelaajan suurin pistemäärä.


### Pelin painallukset
Kun peliä pelataan käyttäjä voi painaa eri näppäimiä ja vaikuttaa peliin. 

```mermaid
sequenceDiagram
  actor User
  participant main_menu
  participant gameloop
  User->>main_menu: click "any key"
  main_menu->>gameloop: start(window, highscore)
```
Main menussa kun käyttäjä painaa mitä tahansa näppäintä, niin peli alkaa.

```mermaid
sequenceDiagram
  actor User
  participant gameloop_a
  participant gameloop_b
  participant pieces
  User->>gameloop_a: click "Right-key"
  gameloop_a->>gameloop_b: _free_space(self, change)
  gameloop_b->>pieces: free_space(piece, grid)
  pieces-->>gameloop_b: boolean
```
Pelin sisällä kun käyttäjä painaa jotakin näppäintä niin pelissä jotkut arvot yrittää muuttua. Tämä menee gameloopin sisällä, josta tarkistetaan ensin voiko arvo muuttua ja tämän jälkeen arvoa muutetaan. Kaikki käyttäjän tekemä pelin sisällä noudottaa tätä kaavaa. 
