from nba_py import team
from nba_py.player import get_player
from nba_py.constants import TEAMS

def test():
    team_id = TEAMS['ATL']['id']
    player_id = get_player('Lebron', 'James')
    assert team.TeamList()
    assert team.TeamSummary(team_id)
    team_details = team.TeamDetails(team_id)
    assert team_details
    assert team_details.background()
    assert team_details.history()
    assert team.TeamCommonRoster(team_id)
    assert team.TeamGeneralSplits(team_id)
    assert team.TeamOpponentSplits(team_id)
    assert team.TeamLastNGamesSplits(team_id)
    assert team.TeamInGameSplits(team_id)
    assert team.TeamClutchSplits(team_id)
    assert team.TeamShootingSplits(team_id)
    assert team.TeamPerformanceSplits(team_id)
    assert team.TeamLineups(team_id)
    assert team.TeamPlayers(team_id)
    assert team.TeamPlayerOnOffDetail(team_id)
    assert team.TeamPlayerOnOffSummary(team_id)
    assert team.TeamGameLogs(team_id)
    assert team.TeamShotTracking(team_id)
    assert team.TeamReboundTracking(team_id)
    assert team.TeamPassTracking(team_id)
    assert team.TeamVsPlayer(team_id, player_id)
