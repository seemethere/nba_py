from nba_py import team
from nba_py.player import get_player
from nba_py.constants import *

# What this will do is get the stats for:
# Spurs vs Tyson Chandler for the 2010-11 season
plyr = get_player('Tyson', 'Chandler', just_id=False)
tvp = team.TeamVsPlayer(team_id=TEAMS['SAS']['id'],
                        vs_player_id=plyr['PERSON_ID'],
                        season='2010-11')
sa_on = tvp.shot_area_on_court()

try:
    r_on = (i for i in sa_on if i["GROUP_VALUE"] == "Restricted Area").__next__()
except AttributeError:
    r_on = next(i for i in sa_on if i["GROUP_VALUE"] == "Restricted Area")
# rest_on = sa_on[sa_on.GROUP_VALUE == 'Restricted Area']
sa_off = tvp.shot_area_off_court()
try:
    r_off = (i for i in sa_off if i["GROUP_VALUE"] == "Restricted Area").__next__()
except AttributeError:
    r_off = next(i for i in sa_off if i["GROUP_VALUE"] == "Restricted Area")
# rest_off = sa_off[sa_off.GROUP_VALUE == 'Restricted Area']
print('Spurs stats vs Tyson Chandler (2010-11)')
print('On court:  {}'.format(float(r_on['FG_PCT'])))
print('Off court: {}'.format(float(r_off['FG_PCT'])))
