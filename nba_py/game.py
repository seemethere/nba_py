from nba_py import _api_scrape, _get_json


class Boxscore:

    def __init__(self,
                 game_id,
                 range_type=0,
                 start_period=0,
                 end_period=0,
                 start_range=0,
                 end_range=0):
        self.json = _get_json(endpoint='boxscore',
                              params={'GameID': game_id,
                                      'RangeType': range_type,
                                      'StartPeriod': start_period,
                                      'EndPeriod': end_period,
                                      'StartRange': start_range,
                                      'EndRange': end_range})

    def game_summary(self):
        return _api_scrape(self.json, 0)

    def line_score(self):
        return _api_scrape(self.json, 1)

    def season_series(self):
        return _api_scrape(self.json, 2)

    def last_meeting(self):
        return _api_scrape(self.json, 3)

    def player_stats(self):
        return _api_scrape(self.json, 4)

    def team_stats(self):
        return _api_scrape(self.json, 5)

    def other_stats(self):
        return _api_scrape(self.json, 6)

    def officials(self):
        return _api_scrape(self.json, 7)

    def game_info(self):
        return _api_scrape(self.json, 8)

    def inactive_players(self):
        return _api_scrape(self.json, 9)

    def available_video(self):
        return _api_scrape(self.json, 10)

    def player_track(self):
        return _api_scrape(self.json, 11)

    def player_track_team(self):
        return _api_scrape(self.json, 12)


class BoxscoreScoring(Boxscore):

    def sql_players_scoring(self):
        return _api_scrape(self.json, 13)

    def sql_team_scoring(self):
        return _api_scrape(self.json, 14)


class BoxscoreUsage(Boxscore):

    def sql_players_usage(self):
        return _api_scrape(self.json, 13)

    def sql_team_usage(self):
        return _api_scrape(self.json, 14)


class BoxscoreMisc(Boxscore):

    def sql_players_misc(self):
        return _api_scrape(self.json, 13)

    def sql_team_misc(self):
        return _api_scrape(self.json, 14)


class BoxscoreAdvanced(Boxscore):

    def sql_players_advanced(self):
        return _api_scrape(self.json, 13)

    def sql_team_advanced(self):
        return _api_scrape(self.json, 14)


class BoxscoreFourFactors(Boxscore):

    def sql_players_four_factors(self):
        return _api_scrape(self.json, 13)

    def sql_team_four_factors(self):
        return _api_scrape(self.json, 14)


class PlayByPlay:

    def __init__(self,
                 game_id,
                 start_period=0,
                 end_period=0):
        self.json = _get_json(endpoint='playbyplay',
                              params={'GameID': game_id,
                                      'StartPeriod': start_period,
                                      'EndPeriod': end_period})

    def info(self):
        return _api_scrape(self.json, 0)

    def available_video(self):
        return _api_scrape(self.json, 1)
