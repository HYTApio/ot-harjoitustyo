import unittest
from repositories.scores_repositories import scores_repository


class TestScores(unittest.TestCase):
    def setUp(self):
        scores_repository.delete_all()
    
    def test_delete_all(self):
        scores_repository.add_score(str(1))
        scores_repository.delete_all()
        score=scores_repository.find_high_score()
        self.assertEqual(score, 0)
    
    def test_find_high_score(self):
        scores_repository.add_score(1)
        scores_repository.add_score(2)
        score=scores_repository.find_high_score()
        self.assertEqual(int(score), 2)


