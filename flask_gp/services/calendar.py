# Python
import requests
from lxml import html


class CalendarService:
    """Service class to get results from MotoGP.com"""

    MAIN_RACE_RESULTS_URL = 'https://www.motogp.com/en/calendar'

    @property
    def circuits(self):
        try:
            return requests.get(self.MAIN_RACE_RESULTS_URL).text
        except Exception:
            return ''

    def get_circuits(self) -> dict:
        """Find circuits list in response.
        :returns: dictionary with list of race circuits."""
        results = html.fromstring(self.circuits).getroottree().xpath(
            '//div[@class="calendar_events container"]//div[contains(@class, "counter") and not(contains(@class, "hidden"))]//a[@class="event_name"]'
        )
        return {'results': results}
