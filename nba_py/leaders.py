from nba_py import _api_scrape, _get_json
from nba_py.constants import *


class LeagueLeaders:
    _endpoint = 'leagueleaders'

    def __init__(self,
                 league_id=League.Default,
                 per_mode=PerMode.Default,
                 stat_category=StatCategory.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 scope=Scope.Default,):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'PerMode': per_mode,
                                      'StatCategory': stat_category,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'Scope': scope})

    def results(self):
        return _api_scrape(self.json, 0)


class LeadersTiles:
    _endpoint = 'leaderstiles'

    def __init__(self,
                 league_id=League.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 game_scope=GameScope.Default,
                 player_scope=PlayerScope.Default,
                 player_or_team=PlayerOrTeam.Default,
                 stat_category=StatCategory.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'Stat': stat_category,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'GameScope': game_scope,
                                      'PlayerScope': player_scope,
                                      'PlayerOrTeam': player_or_team})

    def current_season_high(self):
        return _api_scrape(self.json, 0)

    def alltime_season_high(self):
        return _api_scrape(self.json, 1)

    def last_season_high(self):
        return _api_scrape(self.json, 2)

    def low_season_high(self):
        return _api_scrape(self.json, 3)
