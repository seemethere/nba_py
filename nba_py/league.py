from nba_py import _api_scrape, _get_json
from nba_py import constants


class Leaders:
    _endpoint = 'leagueleaders'

    def __init__(self,
                 league_id=constants.League.Default,
                 per_mode=constants.PerMode.Default,
                 stat_category=constants.StatCategory.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 scope=constants.Scope.Default,):
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
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 game_scope=constants.GameScope.Default,
                 player_scope=constants.PlayerScope.Default,
                 player_or_team=constants.PlayerOrTeam.Default,
                 stat_category=constants.StatCategory.Default):
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


class Lineups:
    _endpoint = 'leaguedashlineups'

    def __init__(self,
                 group_quantity=constants.GroupQuantity.Default,
                 season_type=constants.SeasonType.Default,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.Rank.Default,
                 season=constants.CURRENT_SEASON,
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
                 last_n_games=constants.LastNGames.Default):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'GroupQuantity': group_quantity,
                                      'SeasonType': season_type,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'Season': season,
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
                                      'LastNGames': last_n_games})

    def overall(self):
        return _api_scrape(self.json, 0)


class TeamStats:
    _endpoint = 'leaguedashteamstats'

    def __init__(self,
                 conference=constants.Conference.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 division=constants.Division.Default,
                 game_scope=constants.Game_Scope.Default,
                 game_segment=constants.GameSegment.Default,
                 last_n_games=constants.LastNGames.Default,
                 league_id=constants.League.Default,
                 location=constants.Location.Default,
                 measure_type=constants.MeasureType.Default,
                 month=constants.Month.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 outcome=constants.Outcome.Default,
                 playoff_round=constants.PlayoffRound.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 per_mode=constants.PerMode.Default,
                 period=constants.Period.Default,
                 player_experience=constants.PlayerExperience.Default,
                 player_position=constants.PlayerPosition.Default,
                 plus_minus=constants.PlusMinus.Default,
                 rank=constants.Rank.Default,
                 season=constants.CURRENT_SEASON,
                 season_segment=constants.SeasonSegment.Default,
                 season_type=constants.SeasonType.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 starter_bench=constants.StarterBench.Default,
                 team_id=constants.TeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'SeasonType': season_type,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'Season': season,
                                      'PORound': playoff_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'TeamID': team_id,
                                      'Conference': conference,
                                      'Division': division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'ShotClockRange': shot_clock_range,
                                      'LastNGames': last_n_games,
                                      'GameScope': game_scope,
                                      'PlayerExperience': player_experience,
                                      'PlayerPosition': player_position,
                                      'StarterBench': starter_bench,
                                      })

    def overall(self):
        return _api_scrape(self.json, 0)


class PlayerStats:
    _endpoint = 'leaguedashplayerstats'

    def __init__(self,
                 season_type=constants.SeasonType.Default,
                 measure_type=constants.MeasureType.Default,
                 per_mode=constants.PerMode.Default,
                 plus_minus=constants.PlusMinus.Default,
                 pace_adjust=constants.PaceAdjust.Default,
                 rank=constants.Rank.Default,
                 season=constants.CURRENT_SEASON,
                 playoff_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 team_id=constants.TeamID.Default,
                 conference=constants.Conference.Default,
                 division=constants.Division.Default,
                 game_segment=constants.GameSegment.Default,
                 period=constants.Period.Default,
                 shot_clock_range=constants.ShotClockRange.Default,
                 last_n_games=constants.LastNGames.Default,
                 game_scope=constants.Game_Scope.Default,
                 player_experience=constants.PlayerExperience.Default,
                 player_position=constants.PlayerPosition.Default,
                 starter_bench=constants.StarterBench.Default,
                 draft_year=constants.DraftYear.Default,
                 draft_pick=constants.DraftPick.Default,
                 college=constants.College.Default,
                 country=constants.Country.Default,
                 height=constants.Height.Default,
                 weight=constants.Weight.Default
                 ):
        self.json = _get_json(endpoint=self._endpoint,
                              params={'SeasonType': season_type,
                                      'MeasureType': measure_type,
                                      'PerMode': per_mode,
                                      'PlusMinus': plus_minus,
                                      'PaceAdjust': pace_adjust,
                                      'Rank': rank,
                                      'Season': season,
                                      'PORound': playoff_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'TeamID': team_id,
                                      'Conference': conference,
                                      'Division': division,
                                      'GameSegment': game_segment,
                                      'Period': period,
                                      'ShotClockRange': shot_clock_range,
                                      'LastNGames': last_n_games,
                                      'GameScope': game_scope,
                                      'PlayerExperience': player_experience,
                                      'PlayerPosition': player_position,
                                      'StarterBench': starter_bench,
                                      'DraftYear': draft_year,
                                      'DraftPick': draft_pick,
                                      'College': college,
                                      'Country': country,
                                      'Height': height,
                                      'Weight': weight
                                      })

    def overall(self):
        return _api_scrape(self.json, 0)


class _PlayerTrackingStats:
    """
    Args:
        :league_id: ID for the league to look in (Default is 00)
        :season_type: Season type to consider (Regular or Playoffs)
        :player_or_team: Filter by (Player or Team)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :season: Season given to look up
        :playoff_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :team_id: ID of the team to look up
        :conference: Filter by conference
        :division: Filter by division
        :last_n_games: Filter by number of games specified in N
        :game_scope: Filter by GameScope (Yesterday, Last 10)
        :player_experience: Player experience (Rookie, Sophomore, Veteran)
        :player_position: Filter by position (Forward, Center, Guard)
        :starter_bench: Filter by Starters or Bench
        :draft_year: Filter by draft year
        :draft_pick: Filter by draft pick (1st+Round, Lottery+Pick, etc.)
        :college: Filter by college
        :country: Filter by country
        :height: Filter by player's height
        :weight: Filter by player's weight

    Attributes:
        :json: Contains the full json dump to play around with
    """
    _endpoint = 'leaguedashptstats'
    _pt_measure_type = ''

    def __init__(self,
                 league_id=constants.League.Default,
                 season_type=constants.SeasonType.Default,
                 player_or_team=constants.PlayerOrTeam.Default,
                 per_mode=constants.PerMode.Default,
                 season=constants.CURRENT_SEASON,
                 playoff_round=constants.PlayoffRound.Default,
                 outcome=constants.Outcome.Default,
                 location=constants.Location.Default,
                 month=constants.Month.Default,
                 season_segment=constants.SeasonSegment.Default,
                 date_from=constants.DateFrom.Default,
                 date_to=constants.DateTo.Default,
                 opponent_team_id=constants.OpponentTeamID.Default,
                 vs_conference=constants.VsConference.Default,
                 vs_division=constants.VsDivision.Default,
                 team_id=constants.TeamID.Default,
                 conference=constants.Conference.Default,
                 division=constants.Division.Default,
                 last_n_games=constants.LastNGames.Default,
                 game_scope=constants.Game_Scope.Default,
                 player_experience=constants.PlayerExperience.Default,
                 player_position=constants.PlayerPosition.Default,
                 starter_bench=constants.StarterBench.Default,
                 draft_year=constants.DraftYear.Default,
                 draft_pick=constants.DraftPick.Default,
                 college=constants.College.Default,
                 country=constants.Country.Default,
                 height=constants.Height.Default,
                 weight=constants.Weight.Default
                 ):

        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'PtMeasureType': self._pt_measure_type,
                                      'SeasonType': season_type,
                                      'PlayerOrTeam': player_or_team,
                                      'PerMode': per_mode,
                                      'Season': season,
                                      'PORound': playoff_round,
                                      'Outcome': outcome,
                                      'Location': location,
                                      'Month': month,
                                      'SeasonSegment': season_segment,
                                      'DateFrom': date_from,
                                      'DateTo': date_to,
                                      'OpponentTeamID': opponent_team_id,
                                      'VsConference': vs_conference,
                                      'VsDivision': vs_division,
                                      'TeamID': team_id,
                                      'Conference': conference,
                                      'Division': division,
                                      'LastNGames': last_n_games,
                                      'GameScope': game_scope,
                                      'PlayerExperience': player_experience,
                                      'PlayerPosition': player_position,
                                      'StarterBench': starter_bench,
                                      'DraftYear': draft_year,
                                      'DraftPick': draft_pick,
                                      'College': college,
                                      'Country': country,
                                      'Height': height,
                                      'Weight': weight
                                      })

    def overall(self):
        return _api_scrape(self.json, 0)


class PlayerSpeedDistanceTracking(_PlayerTrackingStats):
    """
    Statistics that measure the distance covered and the average speed of all
    movements (sprinting, jogging, standing, walking, backwards and forwards)
    by a player while on the court.
    """
    _pt_measure_type = constants.PtMeasureType.SpeedDistance


class GameLog:
    _endpoint = 'leaguegamelog'

    def __init__(self,
                 league_id=constants.League.Default,
                 season=constants.CURRENT_SEASON,
                 season_type=constants.SeasonType.Default,
                 player_or_team=constants.Player_or_Team.Default,
                 counter=constants.Counter.Default,
                 sorter=constants.Sorter.Default,
                 direction=constants.Direction.Default,
                 ):

        self.json = _get_json(endpoint=self._endpoint,
                              params={'LeagueID': league_id,
                                      'Season': season,
                                      'SeasonType': season_type,
                                      'PlayerOrTeam': player_or_team,
                                      'Counter': counter,
                                      'Sorter': sorter,
                                      'Direction': direction
                                      })

    def overall(self):
        return _api_scrape(self.json, 0)
