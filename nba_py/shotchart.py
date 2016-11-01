from nba_py import _api_scrape, _get_json
from nba_py.constants import *

class ShotChart:
    _endpoint = 'shotchartdetail'

    def __init__(self,
                 player_id,
                 team_id=TeamID.Default,
                 game_id=GameID.Default,
                 league_id=League.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 outcome=Outcome.Default,
                 location=Location.Default,
                 month=Month.Default,
                 season_segment=SeasonSegment.Default,
                 date_from=DateFrom.Default,
                 date_to=DateTo.Default,
                 opponent_team_id=OpponentTeamID.Default,
                 vs_conf = VsConference.Default,
                 vs_div = VsDivision.Default,
                 position = PlayerPosition.Default,
                 game_segment=GameSegment.Default,
                 period=Period.Default,
                 last_n_games=LastNGames.Default,
                 ahead_behind=AheadBehind.Default,
                 context_measure=ContextMeasure.Default,
                 clutch_time=ClutchTime.Default,
                 rookie_year=RookieYear.Default):

        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID' : player_id,
                                      'TeamID' : team_id,
                                      'GameID' : game_id,
                                      'LeagueID': league_id,
                                      'Season' :  season,
                                      'SeasonType' : season_type,
                                      'Outcome' : outcome,
                                      'Location' : location,
                                      'Month' : month,
                                      'SeasonSegment' : season_segment,
                                      'DateFrom' :  date_from,
                                      'DateTo' : date_to,
                                      'OpponentTeamID' : opponent_team_id,
                                      'VsConference' : vs_conf,
                                      'VsDivision' : vs_div,
                                      'PlayerPosition' : position,
                                      'GameSegment' : game_segment,
                                      'Period' :  period,
                                      'LastNGames' : last_n_games,
                                      'AheadBehind' : ahead_behind,
                                      'ContextMeasure' : context_measure,
                                      'ClutchTime' : clutch_time,
                                      'RookieYear' : rookie_year})

    def shot_chart(self):
        return _api_scrape(self.json, 0)

    def league_average(self):
        return _api_scrape(self.json, 1)
