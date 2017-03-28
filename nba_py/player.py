from nba_py import _api_scrape, _get_json, HAS_PANDAS
from nba_py import constants


class PlayerNotFoundException(Exception):
    pass


def get_player(first_name,
               last_name=None,
               season=constants.CURRENT_SEASON,
               only_current=0,
               just_id=True):
    """
    Calls our PlayerList class to get a full list of players and then returns
    just an id if specified or the full row of player information

    Args:
        :first_name: First name of the player
        :last_name: Last name of the player
        (this is None if the player only has first name [Nene])
        :only_current: Only wants the current list of players
        :just_id: Only wants the id of the player

    Returns:
        Either the ID or full row of information of the player inputted

    Raises:
        :PlayerNotFoundException::
    """
    if last_name is None:
        name = first_name.lower()
    else:
        name = '{}, {}'.format(last_name, first_name).lower()
    pl = PlayerList(season=season, only_current=only_current).info()
    hdr = 'DISPLAY_LAST_COMMA_FIRST'
    if HAS_PANDAS:
        item = pl[pl.DISPLAY_LAST_COMMA_FIRST.str.lower() == name]
    else:
        item = next(plyr for plyr in pl if str(plyr[hdr]).lower() == name)
    if len(item) == 0:
        raise PlayerNotFoundException
    elif just_id:
        return item['PERSON_ID']
    else:
        return item


class PlayerList:
    """
    Contains a list of all players for a season, if specified, and will only
    contain current players if specified as well

    Args:
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :only_current: Restrict lookup to only current players

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'commonallplayers'

    def __init__(self,
                 league_id=constants.League.NBA,
                 season=constants.CURRENT_SEASON,
                 only_current=1):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'Season': season,
                                      'IsOnlyCurrentSeason': only_current})

    def info(self):
        return _api_scrape(self.json, 0)


class PlayerSummary:
    """
    Contains common player information like headline stats, weight, etc.

    Args:
        :player_id: ID of the player to look up

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'commonplayerinfo'

    def __init__(self,
                 player_id):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id})

    def info(self):
        return _api_scrape(self.json, 0)

    def headline_stats(self):
        return _api_scrape(self.json, 1)


class _PlayerDashboard:
    """
    Has all the basic arguments for all of the Player Dashboard type objects

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyyearoveryear'

    def __init__(self,
                 player_id,
                 team_id=0,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.PaceAdjust.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 po_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'TeamID': team_id,
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
                                      'LastNGames': last_n_games},
                              referer='player')

    def overall(self):
        return _api_scrape(self.json, 0)


class PlayerGeneralSplits(_PlayerDashboard):
    """

    Contains stats pertaining to location, wins and losses, pre/post all star
    break, starting position, and numbers of days rest

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbygeneralsplits'

    def location(self):
        return _api_scrape(self.json, 1)

    def win_losses(self):
        return _api_scrape(self.json, 2)

    def month(self):
        return _api_scrape(self.json, 3)

    def pre_post_all_star(self):
        return _api_scrape(self.json, 4)

    def starting_position(self):
        return _api_scrape(self.json, 5)

    def days_rest(self):
        return _api_scrape(self.json, 6)


class PlayerOpponentSplits(_PlayerDashboard):
    """

    Contains stats pertaining to player stats vs certain opponents by division,
    conference, and by specific team opponent

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyopponent'

    def by_conference(self):
        return _api_scrape(self.json, 1)

    def by_division(self):
        return _api_scrape(self.json, 2)

    def by_opponent(self):
        return _api_scrape(self.json, 3)


class PlayerLastNGamesSplits(_PlayerDashboard):
    """
    Contains players stats per last 5, 10, 15, and 20 games, or specified
    number of games.

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbylastngames'

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


class PlayerInGameSplits(_PlayerDashboard):
    """
    Contains player stats by half, by quarter, by score margin, and by actual
    margins.

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbygamesplits'

    def by_half(self):
        return _api_scrape(self.json, 1)

    def by_period(self):
        return _api_scrape(self.json, 2)

    def by_score_margin(self):
        return _api_scrape(self.json, 3)

    def by_actual_margin(self):
        return _api_scrape(self.json, 4)


class PlayerClutchSplits(_PlayerDashboard):
    """
    Contains a lot of methods for last n minutes with a deficit of x points

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyclutch'

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
        return _api_scrape(self.json, 9)


class PlayerShootingSplits(_PlayerDashboard):
    """

    Shooting stats based on distance, area, assisted to, shot types, and
    assisted by.

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyshootingsplits'

    def shot_5ft(self):
        return _api_scrape(self.json, 1)

    def shot_8ft(self):
        return _api_scrape(self.json, 2)

    def shot_areas(self):
        return _api_scrape(self.json, 3)

    def assisted_shots(self):
        return _api_scrape(self.json, 4)

    def shot_types_summary(self):
        return _api_scrape(self.json, 5)

    def shot_types_detail(self):
        return _api_scrape(self.json, 6)

    def assisted_by(self):
        return _api_scrape(self.json, 7)


class PlayerPerformanceSplits(_PlayerDashboard):
    """
    Player stats by different performance metrics such as score differntial,
    points scored, and points scored against

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyteamperformance'

    def score_differential(self):
        return _api_scrape(self.json, 1)

    def points_scored(self):
        return _api_scrape(self.json, 2)

    def points_against(self):
        return _api_scrape(self.json, 3)


class PlayerYearOverYearSplits(_PlayerDashboard):
    """
    Displays player stats over the given season and over all seasons in the
    given league

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashboardbyyearoveryear'

    def by_year(self):
        return _api_scrape(self.json, 1)


class PlayerCareer:
    """
    Contains stats based on several parameters such as career regular season
    totals, post season career totals, all star season careers totals, college
    season career totals, etc.

    Args:
        :player_id: Player ID to look up
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :league_id: ID for the league to look in (Default is 00)

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playercareerstats'

    def __init__(self,
                 player_id,
                 per_mode=constants.PerMode.PerGame,
                 league_id=constants.League.NBA):
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

    def college_season_career_totals(self):
        return _api_scrape(self.json, 7)

    def preseason_season_totals(self):
        return _api_scrape(self.json, 8)

    def preseason_career_totals(self):
        return _api_scrape(self.json, 9)

    def regular_season_rankings(self):
        return _api_scrape(self.json, 10)

    def post_season_rankings(self):
        return _api_scrape(self.json, 11)


class PlayerProfile(PlayerCareer):
    """
    Contains a more in depth version of player career stats with season highs,
    career highs, and when the player's next game is

    Args:
        :player_id: Player ID to look up
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :league_id: ID for the league to look in (Default is 00)

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerprofilev2'

    def season_highs(self):
        return _api_scrape(self.json, 12)

    def career_highs(self):
        return _api_scrape(self.json, 13)

    def next_game(self):
        return _api_scrape(self.json, 14)


class PlayerGameLogs:
    """
    Contains a full log of all the games for a player for a given season

    Args:
        :player_id: ID of the player to look up
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playergamelog'

    def __init__(self,
                 player_id,
                 league_id=constants.League.NBA,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Regular):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type})

    def info(self):
        return _api_scrape(self.json, 0)


class PlayerShotTracking(_PlayerDashboard):
    """

    Tracking data for shooting for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptshots'

    def general_shooting(self):
        return _api_scrape(self.json, 1)

    def shot_clock_shooting(self):
        return _api_scrape(self.json, 2)

    def dribble_shooting(self):
        return _api_scrape(self.json, 3)

    def closest_defender_shooting(self):
        return _api_scrape(self.json, 4)

    def closest_defender_shooting_long(self):
        return _api_scrape(self.json, 5)

    def touch_time_shooting(self):
        return _api_scrape(self.json, 6)


class PlayerReboundTracking(_PlayerDashboard):
    """

    Tracking data for rebounding for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptreb'

    def shot_type_rebounding(self):
        return _api_scrape(self.json, 1)

    def num_contested_rebounding(self):
        return _api_scrape(self.json, 2)

    def shot_distance_rebounding(self):
        return _api_scrape(self.json, 3)

    def rebound_distance_rebounding(self):
        return _api_scrape(self.json, 4)


class PlayerPassTracking(_PlayerDashboard):
    """
    Tracking data for passing for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptpass'

    def passes_made(self):
        return _api_scrape(self.json, 0)

    def passes_received(self):
        return _api_scrape(self.json, 1)


class PlayerDefenseTracking(_PlayerDashboard):
    """
    Tracking data for defense for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptshotdefend'


class PlayerShotLogTracking(_PlayerDashboard):
    """
    Contains a log for every shot for a given season for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptshotlog'


class PlayerReboundLogTracking(_PlayerDashboard):
    """
    Contains a log for every rebound for a given season for a given player

    Args:
        :player_id: ID of the player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'playerdashptreboundlogs'


class PlayerVsPlayer:
    """
    Contains general stats that pertain to players going against other players

    Args:
        :player_id: ID of the player to look up
        :vs_player_id: ID of the vs player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        json: Contains the full json dump to play around with
    """
    _endpoint = 'playervsplayer'

    def __init__(self,
                 player_id,
                 vs_player_id,
                 team_id=0,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.PaceAdjust.Default,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 po_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'PlayerID': player_id,
                                      'VsPlayerID': vs_player_id,
                                      'TeamID': team_id,
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

    def on_off_court(self):
        return _api_scrape(self.json, 1)

    def shot_distance_overall(self):
        return _api_scrape(self.json, 2)

    def shot_distance_on_court(self):
        return _api_scrape(self.json, 3)

    def shot_distance_off_court(self):
        return _api_scrape(self.json, 4)

    def shot_area_overall(self):
        return _api_scrape(self.json, 5)

    def shot_area_on_court(self):
        return _api_scrape(self.json, 6)

    def shot_area_off_court(self):
        return _api_scrape(self.json, 7)

    def player_info(self):
        return _api_scrape(self.json, 8)

    def vs_player_info(self):
        return _api_scrape(self.json, 9)
