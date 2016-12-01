from nba_py import _api_scrape, _get_json
from nba_py.constants import *


class BoxscoreSummary:
    _endpoint = 'boxscoresummaryv2'

    def __init__(self,
                 game_id,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 range_type=RangeType.Default,
                 start_period=StartPeriod.Default,
                 end_period=EndPeriod.Default,
                 start_range=StartRange.Default,
                 end_range=EndRange.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GameID': game_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'RangeType': range_type,
                                      'StartPeriod': start_period,
                                      'EndPeriod': end_period,
                                      'StartRange': start_range,
                                      'EndRange': end_range})

    def game_summary(self):
        return _api_scrape(self.json, 0)

    def other_stats(self):
        return _api_scrape(self.json, 1)

    def officials(self):
        return _api_scrape(self.json, 2)

    def inactive_players(self):
        return _api_scrape(self.json, 3)

    def game_info(self):
        return _api_scrape(self.json, 4)

    def line_score(self):
        return _api_scrape(self.json, 5)

    def last_meeting(self):
        return _api_scrape(self.json, 6)

    def season_series(self):
        return _api_scrape(self.json, 7)

    def available_video(self):
        return _api_scrape(self.json, 8)

class _BaseBoxcore:

    def __init__(self,
                 game_id,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 range_type=RangeType.Default,
                 start_period=StartPeriod.Default,
                 end_period=EndPeriod.Default,
                 start_range=StartRange.Default,
                 end_range=EndRange.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GameID': game_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'RangeType': range_type,
                                      'StartPeriod': start_period,
                                      'EndPeriod': end_period,
                                      'StartRange': start_range,
                                      'EndRange': end_range})


class Boxscore(_BaseBoxcore):
    _endpoint = 'boxscoretraditionalv2'

    def player_stats(self):
        return _api_scrape(self.json, 0)

    def team_stats(self):
        return _api_scrape(self.json, 1)

    def team_starter_bench_stats(self):
        return _api_scrape(self.json, 2)


class BoxscoreScoring(_BaseBoxcore):
    _endpoint = 'boxscorescoringv2'

    def sql_players_scoring(self):
        return _api_scrape(self.json, 0)

    def sql_team_scoring(self):
        return _api_scrape(self.json, 1)


class BoxscoreUsage(_BaseBoxcore):
    _endpoint = 'boxscoreusagev2'

    def sql_players_usage(self):
        return _api_scrape(self.json, 0)

    def sql_team_usage(self):
        return _api_scrape(self.json, 1)


class BoxscoreMisc(_BaseBoxcore):
    _endpoint = 'boxscoremiscv2'

    def sql_players_misc(self):
        return _api_scrape(self.json, 0)

    def sql_team_misc(self):
        return _api_scrape(self.json, 1)


class BoxscoreAdvanced(_BaseBoxcore):
    _endpoint = 'boxscoreadvancedv2'

    def sql_players_advanced(self):
        return _api_scrape(self.json, 0)

    def sql_team_advanced(self):
        return _api_scrape(self.json, 1)


class BoxscoreFourFactors(_BaseBoxcore):
    _endpoint = 'boxscorefourfactorsv2'

    def sql_players_four_factors(self):
        return _api_scrape(self.json, 0)

    def sql_team_four_factors(self):
        return _api_scrape(self.json, 1)


class PlayerTracking:
    _endpoint = 'boxscoreplayertrackv2'

    def __init__(self,
                 game_id):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GameID': game_id})

    def info(self):
        return _api_scrape(self.json, 0)


class PlayByPlay:
    _endpoint = 'playbyplay'

    def __init__(self,
                 game_id,
                 start_period=StartPeriod.Default,
                 end_period=EndPeriod.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GameID': game_id,
                                      'StartPeriod': start_period,
                                      'EndPeriod': end_period})

    def info(self):
        return _api_scrape(self.json, 0)

    def available_video(self):
        return _api_scrape(self.json, 1)
