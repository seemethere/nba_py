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


# What this will do is get the
plyr = get_player('Tyson', 'Chandler', just_id=False)
tvp = team.TeamVsPlayer(team_id=TEAMS['SAS']['id'],
                        vs_player_id=plyr['PERSON_ID'],
                        season='2010-11')
sa_on = tvp.shot_area_on_court()
rest_on = sa_on[sa_on.GROUP_VALUE == 'Restricted Area']
sa_off = tvp.shot_area_off_court()
rest_off = sa_off[sa_off.GROUP_VALUE == 'Restricted Area']
print 'Spurs stats vs Tyson Chandler (2010-11)'
print 'On court:  {}'.format(float(rest_on['FG_PCT']))
print 'Off court: {}'.format(float(rest_off['FG_PCT']))
