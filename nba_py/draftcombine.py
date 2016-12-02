from nba_py import _api_scrape, _get_json
from nba_py import constants


class Summary:
    _endpoint = 'draftcombinestats'

    def __init__(
            self,
            league_id=constants.League.Default,
            season=constants.CURRENT_SEASON):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season})

    def overall(self):
        return _api_scrape(self.json, 0)


class DrillResults:
    _endpoint = 'draftcombinedrillresults'

    def __init__(
            self,
            league_id=constants.League.Default,
            season=constants.CURRENT_SEASON):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season})

    def overall(self):
        return _api_scrape(self.json, 0)


class SpotShooting:
    _endpoint = 'draftcombinespotshooting'

    def __init__(
            self,
            league_id=constants.League.Default,
            season=constants.CURRENT_SEASON):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonYear': season})

    def overall(self):
        return _api_scrape(self.json, 0)
