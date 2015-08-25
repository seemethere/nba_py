from nba_py import _api_scrape, _get_json, CURRENT_SEASON, NBA_ID


class TeamInfoCommon:

    def __init__(self,
                 team_id,
                 season=CURRENT_SEASON,
                 league_id=NBA_ID,
                 season_type='Regular Season'):
        self.json = _get_json(endpoint='teaminfocommon',
                              params={'TeamID': team_id,
                                      'Season': season,
                                      'LeagueID': league_id,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)

    def season_ranks(self):
        return _api_scrape(self.json, 1)
