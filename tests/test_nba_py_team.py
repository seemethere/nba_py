from nba_py import team
from nba_py.player import get_player
from nba_py.constants import TEAMS

# tc = team.TeamSummary(TEAMS['ATL']['id'], season='2013-14')
# print tc.info()

# td = team.TeamGeneralSplits(TEAMS['CLE']['id'], season='2012-13')
# print td.overall()
#
# tdo = team.TeamOpponentSplits(TEAMS['SAS']['id'], season='2012-13')
# print tdo.division()

# dash_lineups = team.TeamLineups(
#     TEAMS['MIL']['id'], "0041400122", season='2014-15')
# print dash_lineups.overall()
#
# players = team.TeamPlayers(TEAMS['MIL']['id'], season='2013-14')
# print players.overall()

plyr = get_player('DeRek', 'FiSHer', season='2008-09')
tvp = team.TeamVsPlayer(team_id=TEAMS['SAS']['id'],
                        vs_player_id=plyr,
                        season='2008-09')
sao = tvp.shot_area_overall()
over_40 = sao[sao.FG_PCT > 0.40]
print over_40
