from requests import get
from pandas import DataFrame
from datetime import datetime
from nba_py.constants import League

# Constants
TODAY = datetime.today()
BASE_URL = 'http://stats.nba.com/stats/{endpoint}/'
HEADER = {'User-Agent' : 'Mozilla/5.0'}

def _api_scrape(json_inp, ndx):
    """
    Internal method to streamline the getting of data from the json

    Args:
        json_inp (json): json input from our caller
        ndx (int): index where the data is located in the api

    Returns:
        DataFrame (pandas.DataFrame): data set from ndx within the API's json
    """
    return DataFrame(json_inp['resultSets'][ndx]['rowSet'],
                     columns=json_inp['resultSets'][ndx]['headers'])


def _get_json(endpoint, params):
    """
    Internal method to streamline our requests / json getting

    Args:
        endpoint (str): endpoint to be called from the API
        params (dict): parameters to be passed to the API

    Raises:
        HTTPError: if requests hits a status code != 200

    Returns:
        json (json): json object for selected API call
    """
    _get = get(BASE_URL.format(endpoint=endpoint), params=params, headers=HEADER)
    # print _get.url
    _get.raise_for_status()
    return _get.json()


class Scoreboard:
    _endpoint = 'scoreboard'
    """
    Displays current games plus info for a given day
    """

    def __init__(self,
                 month=TODAY.month,
                 day=TODAY.day,
                 year=TODAY.year,
                 league_id=League.NBA,
                 offset=0):
        self._game_date = '{month:02d}/{day:02d}/{year}'.format(month=month,
                                                                day=day,
                                                                year=year)
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'GameDate': self._game_date,
                                      'DayOffset': offset})

    def game_header(self):
        return _api_scrape(self.json, 0)

    def line_score(self):
        return _api_scrape(self.json, 1)

    def series_standings(self):
        return _api_scrape(self.json, 2)

    def last_meeting(self):
        return _api_scrape(self.json, 3)

    def east_conf_standings_by_day(self):
        return _api_scrape(self.json, 4)

    def west_conf_standings_by_day(self):
        return _api_scrape(self.json, 5)

    def available(self):
        return _api_scrape(self.json, 6)
