from nba_py import _api_scrape, _get_json, CURRENT_SEASON
from nba_py.constants import League, MeasureType, PerMode, SeasonType


class TeamList:
    _endpoint = 'commonteamtears'

    def __init__(self,
                 league_id=League.NBA):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id})

    def info(self):
        return _api_scrape(self.json, 0)


class TeamSummary:
    _endpoint = 'teaminfocommon'

    def __init__(self,
                 team_id,
                 season=CURRENT_SEASON,
                 league_id=League.NBA,
                 season_type='Regular Season'):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'Season': season,
                                      'LeagueID': league_id,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)

    def season_ranks(self):
        return _api_scrape(self.json, 1)


class TeamCommonRoster:
    _endpoint = 'commonteamroster'

    def __init__(self,
                 team_id,
                 season=CURRENT_SEASON):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
                                      'Season': season})

    def roster(self):
        return _api_scrape(self.json, 0)

    def coaches(self):
        return _api_scrape(self.json, 1)


class _TeamDashboard:
    _endpoint = ''

    def __init__(self,
                 team_id,
                 measure_type=MeasureType.Base,
                 per_mode=PerMode.PerGame,
                 plus_minus='N',
                 pace_adjust='N',
                 rank='N',
                 league_id=League.NBA,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Regular,
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
        self.json = _get_json(endpoint=self._endpoint,
                              params={'TeamID': team_id,
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

    def overall(self):
        return _api_scrape(self.json, 0)


class TeamGeneralSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbygeneralsplits'

    def location(self):
        return _api_scrape(self.json, 1)

    def wins_losses(self):
        return _api_scrape(self.json, 2)

    def monthly(self):
        return _api_scrape(self.json, 3)

    def pre_post_all_star(self):
        return _api_scrape(self.json, 4)

    def days_rest(self):
        return _api_scrape(self.json, 5)


class TeamOpponentSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyopponent'

    def division(self):
        return _api_scrape(self.json, 1)

    def opponent(self):
        return _api_scrape(self.json, 2)


class TeamLastNGamesSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbylastngames'

    def last5(self):
        return _api_scrape(self.json, 1)

    def last10(self):
        return _api_scrape(self.json, 2)

    def last15(self):
        return _api_scrape(self.json, 3)

    def last20(self):
        return _api_scrape(self.json, 4)

    def gamenumber(self):
        return _api_scrape(self.json, 5)


class TeamInGameSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbygamesplits'

    def by_half(self):
        return _api_scrape(self.json, 1)

    def by_period(self):
        return _api_scrape(self.json, 2)

    def by_score_margin(self):
        return _api_scrape(self.json, 3)

    def by_actual_margin(self):
        return _api_scrape(self.json, 4)


class TeamClutchSplits(_TeamDashboard):
    """
    This is a weird endpoint, to be honest.
    It's got a lot of cool little stats and there are two extra
    fields in the json that I have no idea what they do.

    If you know please tell me.
        * Last30Sec3Point2TeamDashboard
        * Last10Sec3Point2TeamDashboard
    """
    _endpoint = 'teamdashboardbyclutch'

    def last5min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 1)

    def last3min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 2)

    def last1min_deficit_5point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 3)

    def last30sec_deficit_3point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 4)

    def last10sec_deficit_3point(self):
        """
        Results in last 5 minutes <= 5 points
        """
        return _api_scrape(self.json, 5)

    def last5min_plusminus_5point(self):
        """
        Last 5 minutes +/= 5 points
        """
        return _api_scrape(self.json, 6)

    def last3min_plusminus_5point(self):
        """
        Last 3 minutes +/= 5 points
        """
        return _api_scrape(self.json, 7)

    def last1min_plusminus_5point(self):
        """
        Last 1 minutes +/= 5 points
        """
        return _api_scrape(self.json, 8)

    def last30sec_plusminus_5point(self):
        """
        Last 30 seconds +/= 3 points
        """
        return _api_scrape(self.json, 7)


class TeamShootingSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyshootingsplits'

    def shot_5ft(self):
        return _api_scrape(self.json, 1)

    def shot_8ft(self):
        return _api_scrape(self.json, 2)

    def shot_areas(self):
        return _api_scrape(self.json, 3)

    def assisted_shots(self):
        return _api_scrape(self.json, 4)

    def shot_types(self):
        return _api_scrape(self.json, 5)

    def assissted_by(self):
        return _api_scrape(self.json, 6)


class TeamPerformanceSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyteamperformance'

    def score_differential(self):
        return _api_scrape(self.json, 1)

    def points_scored(self):
        return _api_scrape(self.json, 2)

    def points_against(self):
        return _api_scrape(self.json, 3)


class TeamYearOverYearSplits(_TeamDashboard):
    _endpoint = 'teamdashboardbyyearoveryear'

    def by_year(self):
        return _api_scrape(self.json, 1)
