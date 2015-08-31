from nba_py import _api_scrape, _get_json, CURRENT_SEASON
from nba_py.constants import *


def get_player(first_name,
               last_name,
               season=CURRENT_SEASON,
               only_current=0,
               just_id=True):
    name = '{}, {}'.format(last_name, first_name).lower()
    pl = PlayerList(season=season, only_current=only_current).info()
    if just_id:
        return pl[pl.DISPLAY_LAST_COMMA_FIRST.str.lower() == name]['PERSON_ID']
    else:
        return pl[pl.DISPLAY_LAST_COMMA_FIRST.str.lower() == name]


class PlayerList:
    _endpoint = 'commonallplayers'

    def __init__(self,
                 league_id=League.NBA,
                 season=CURRENT_SEASON,
                 only_current=1):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'Season': season,
                                      'IsOnlyCurrentSeason': only_current})

    def info(self):
        return _api_scrape(self.json, 0)


class PlayerSummary:
    _endpoint = 'commonplayerinfo'

    def __init__(self,
                 player_id):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id})

    def info(self):
        return _api_scrape(self.json, 0)

    def headline_stats(self):
        return _api_scrape(self.json, 1)


class PlayerGeneralSplits:
    _endpoint = 'playerdashboardbygeneralsplits'

    def __init__(self,
                 player_id,
                 measure_type=MeasureType.Default,
                 per_mode=PerMode.Default,
                 plus_minus=PlusMinus.Default,
                 pace_adjust=PaceAdjust.Default,
                 rank=PaceAdjust.Default,
                 league_id=League.Default,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Default,
                 po_round=PlayoffRound.Default,
                 outcome=Outcome.Default,
                 location=Location.Default,
                 month=Month.Default,
                 season_segment=SeasonSegment.Default,
                 date_from=DateFrom.Default,
                 date_to=DateTo.Default,
                 opponent_team_id=OpponentTeamID.Default,
                 vs_conference=VsConference.Default,
                 vs_division=VsDivision.Default,
                 game_segment=GameSegment.Default,
                 period=Period.Default,
                 shot_clock_range=ShotClockRange.Default,
                 last_n_games=LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
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


class PlayerCareer:
    _endpoint = 'playercareerstats'

    def __init__(self,
                 player_id,
                 per_mode=PerMode.PerGame,
                 league_id=League.NBA):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'LeagueID': league_id,
                                      'PerMode': per_mode})

    def regular_season_totals(self):
        return _api_scrape(self.json, 0)

    def regular_season_career_totals(self):
        return _api_scrape(self.json, 1)

    def post_season_totals(self):
        return _api_scrape(self.json, 2)

    def post_season_career_totals(self):
        return _api_scrape(self.json, 3)

    def all_star_season_totals(self):
        return _api_scrape(self.json, 4)

    def career_all_star_season_totals(self):
        return _api_scrape(self.json, 5)

    def college_season_totals(self):
        return _api_scrape(self.json, 6)

    def career_college_season_totals(self):
        return _api_scrape(self.json, 7)

    def regular_season_rankings(self):
        return _api_scrape(self.json, 8)

    def post_season_rankings(self):
        return _api_scrape(self.json, 9)


class PlayerProfile(PlayerCareer):
    _endpoint = 'playerprofilev2'

    def season_highs(self):
        return _api_scrape(self.json, 10)

    def career_highs(self):
        return _api_scrape(self.json, 11)

    def next_game(self):
        return _api_scrape(self.json, 12)


class PlayerGameLogs:
    _endpoint = 'playergamelog'

    def __init__(self,
                 player_id,
                 league_id=League.NBA,
                 season=CURRENT_SEASON,
                 season_type=SeasonType.Regular):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)
