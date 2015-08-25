from nba_py import _api_scrape, _get_json, CURRENT_SEASON, NBA_ID


class CommonAllPlayers:

    def __init__(self,
                 league_id=NBA_ID,
                 season=CURRENT_SEASON,
                 only_current=1):
        self.json = _get_json(endpoint='commonallplayers',
                              params={'LeagueID': league_id,
                                      'Season': season,
                                      'IsOnlyCurrentSeason': only_current})

    def info(self):
        return _api_scrape(self.json, 0)


class PlayerInfoCommon:

    def __init__(self,
                 player_id):
        self.json = _get_json(endpoint='commonplayerinfo',
                              params={'PlayerID': player_id})

    def info(self):
        return _api_scrape(self.json, 0)

    def headline_stats(self):
        return _api_scrape(self.json, 1)


class PlayerDashboard:

    def __init__(self,
                 player_id,
                 measure_type='Base',
                 per_mode='PerGame',
                 plus_minus='N',
                 pace_adjust='N',
                 rank='N',
                 league_id=NBA_ID,
                 season=CURRENT_SEASON,
                 season_type='Regular Season',
                 po_round='',
                 outcome='',
                 location='',
                 month=0,
                 season_segment='',
                 date_from='',
                 date_to='',
                 opponent_team_id=0,
                 vs_conference='',
                 vs_division='',
                 game_segment='',
                 period=0,
                 shot_clock_range='',
                 last_n_games=0):
        self.json = _get_json(endpoint='playerdashboardbygeneralsplits',
                              params={'PlayerID': player_id,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'PORound': po_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'ShotClockRange': shot_clock_range,
                                      'LastNGames': last_n_games})

    def overall_dashboard(self):
        return _api_scrape(self.json, 0)

    def location_dashboard(self):
        return _api_scrape(self.json, 1)

    def win_losses_dashboard(self):
        return _api_scrape(self.json, 2)

    def pre_post_all_star_dashboard(self):
        return _api_scrape(self.json, 3)

    def starting_position(self):
        return _api_scrape(self.json, 4)

    def days_rest_dashboard(self):
        return _api_scrape(self.json, 5)
