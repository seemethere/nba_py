from nba_py import _api_scrape, _get_json
from nba_py import constants


class ShotChart:
    _endpoint = 'shotchartdetail'

    def __init__(self,
                 player_id,
                 team_id=constants.TeamID.Default,
                 game_id=constants.GameID.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conf=constants.VsConference.Default,
                 vs_div=constants.VsDivision.Default,
                 position=constants.PlayerPosition.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 last_n_games=constants.LastNGames.Default,
                 ahead_behind=constants.AheadBehind.Default,
                 context_measure=constants.ContextMeasure.Default,
                 clutch_time=constants.ClutchTime.Default,
                 rookie_year=constants.RookieYear.Default):

        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'TeamID': team_id,
                                      'GameID': game_id,
                                      'LeagueID': league_id,
                                      'Season':  season,
                                      'SeasonType': season_type,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom':  date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conf,
                                      'VsDivision': vs_div,
                                      'PlayerPosition': position,
                                      'GameSegment': game_segment,
                                      'Period':  period,
                                      'LastNGames': last_n_games,
                                      'AheadBehind': ahead_behind,
                                      'ContextMeasure': context_measure,
                                      'ClutchTime': clutch_time,
                                      'RookieYear': rookie_year})

    def shot_chart(self):
        return _api_scrape(self.json, 0)

    def league_average(self):
        return _api_scrape(self.json, 1)
