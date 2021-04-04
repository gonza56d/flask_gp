# Python
import requests


class RaceResults:
    """Service class to get results from MotoGP.com"""

    MAIN_RACE_RESULTS_URL = 'https://www.motogp.com/en/Results+Statistics'

    def __init__(self):
        self.response = requests.get(self.MAIN_RACE_RESULTS_URL)

    def get_race_results(self):
        print(self.response.content)
        return {'hola': 'xD', 'chau': 'jaja'}
