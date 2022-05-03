from pathlib import Path
from config import SCORES_FILE_PATH

class ScoresRepository:
    """Luokka, jossa käsitellään pistetiedostoa

    Attributes:
        file_path: Tiedostoon reitti
    """
    def __init__(self, file_path):
        """Luokan konstruktori, joka luo uuden etsinnän

        args:
            file_path: Tiedostoon johtava reitti
        """
        self._file_path = file_path

    def _file_exist(self):
        """Tarkistaa, että tiedosto on olemassa
        """
        Path(self._file_path).touch()

    def find_high_score(self):
        """Etsii suurimman pistemäärän tiedostosta

        returns:
            suurimman pistemäärän tiedostosta
        """
        self._file_exist()
        score = 0
        with open (self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                if int(row) > score:
                    score = row
        return score

    def add_score(self, score):
        """Lisää uuden pistemäärän, jos on suurempi kuin edellinen

        args:
            score: Pstemäärä, joka voidaan lisätä
        """
        highscore = self.find_high_score()
        if score == "":
            with open(self._file_path, "w", encoding="utf-8") as file:
                file.write("")
        elif int(score) > int(highscore):
            self._file_exist()
            with open(self._file_path, "w", encoding="utf-8") as file:
                file.write(str(score)+"\n")

    def delete_all(self):
        """Poistaa kaiken tiedon tiedostosta
        """
        self.add_score("")

scores_repository = ScoresRepository(SCORES_FILE_PATH)
