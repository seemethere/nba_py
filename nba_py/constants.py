from datetime import datetime

_curr_year = datetime.now().year
if datetime.now().month > 6:
    CURRENT_SEASON = str(_curr_year) + "-" + str(_curr_year + 1)[2:]
else:
    CURRENT_SEASON = str(_curr_year - 1) + "-" + str(_curr_year)[2:]

TEAMS = {
    'ATL': {
        'abbr': 'ATL',
        'city': 'Atlanta',
        'code': 'hawks',
        'conference': 'Eastern',
        'displayAbbr': 'ATL',
        'displayConference': 'Eastern',
        'division': 'Southeast',
        'id': '1610612737',
        'name': 'Hawks',
        'color': 'E2373E',
        'colors': ['E2373E', '002A5C', 'BAC4CA']
    }, 'BOS': {
        'abbr': 'BOS',
        'city': 'Boston',
        'code': 'celtics',
        'conference': 'Eastern',
        'displayAbbr': 'BOS',
        'displayConference': 'Eastern',
        'division': 'Atlantic',
        'id': '1610612738',
        'name': 'Celtics',
        'color': '007239',
        'colors': ['007239', 'AE8445', '982527', '000000']
    }, 'BKN': {
        'abbr': 'BKN',
        'city': 'Brooklyn',
        'code': 'nets',
        'conference': 'Eastern',
        'displayAbbr': 'BKN',
        'displayConference': 'Eastern',
        'division': 'Atlantic',
        'id': '1610612751',
        'name': 'Nets',
        'color': '000000',
        'colors': ['000000', 'FFFFFF']
    }, 'CHA': {
        'abbr': 'CHA',
        'city': 'Charlotte',
        'code': 'hornets',
        'conference': 'Eastern',
        'displayAbbr': 'CHA',
        'displayConference': 'Eastern',
        'division': 'Southeast',
        'id': '1610612766',
        'name': 'Hornets',
        'color': '00848E',
        'colors': ['00848E', '260F54', 'CCCCCC']
    }, 'CHI': {
        'abbr': 'CHI',
        'city': 'Chicago',
        'code': 'bulls',
        'conference': 'Eastern',
        'displayAbbr': 'CHI',
        'displayConference': 'Eastern',
        'division': 'Central',
        'id': '1610612741',
        'name': 'Bulls',
        'color': 'C60033',
        'colors': ['C60033', '000000']
    }, 'CLE': {
        'abbr': 'CLE',
        'city': 'Cleveland',
        'code': 'cavaliers',
        'conference': 'Eastern',
        'displayAbbr': 'CLE',
        'displayConference': 'Eastern',
        'division': 'Central',
        'id': '1610612739',
        'name': 'Cavaliers',
        'color': '860038',
        'colors': ['860038', '002D62', 'FDBA31']
    }, 'DAL': {
        'abbr': 'DAL',
        'city': 'Dallas',
        'code': 'mavericks',
        'conference': 'Western',
        'displayAbbr': 'DAL',
        'displayConference': 'Western',
        'division': 'Southwest',
        'id': '1610612742',
        'name': 'Mavericks',
        'color': '0063AF',
        'colors': ['0063AF', 'BAC4CA', '000000']
    }, 'DEN': {
        'abbr': 'DEN',
        'city': 'Denver',
        'code': 'nuggets',
        'conference': 'Western',
        'displayAbbr': 'DEN',
        'displayConference': 'Western',
        'division': 'Northwest',
        'id': '1610612743',
        'name': 'Nuggets',
        'color': '559FD6',
        'colors': ['559FD6', '006BB7', 'FEA927']
    }, 'DET': {
        'abbr': 'DET',
        'city': 'Detroit',
        'code': 'pistons',
        'conference': 'Eastern',
        'displayAbbr': 'DET',
        'displayConference': 'Eastern',
        'division': 'Central',
        'id': '1610612765',
        'name': 'Pistons',
        'color': 'EC003D',
        'colors': ['EC003D', '0058A6', '001D4A']
    }, 'GSW': {
        'abbr': 'GSW',
        'city': 'Golden State',
        'code': 'warriors',
        'conference': 'Western',
        'displayAbbr': 'GSW',
        'displayConference': 'Western',
        'division': 'Pacific',
        'id': '1610612744',
        'name': 'Warriors',
        'color': '0068B3',
        'colors': ['0068B3', 'FFC423']
    }, 'HOU': {
        'abbr': 'HOU',
        'city': 'Houston',
        'code': 'rockets',
        'conference': 'Western',
        'displayAbbr': 'HOU',
        'displayConference': 'Western',
        'division': 'Southwest',
        'id': '1610612745',
        'name': 'Rockets',
        'color': 'C60033',
        'colors': ['C60033', '000000']
    }, 'IND': {
        'abbr': 'IND',
        'city': 'Indiana',
        'code': 'pacers',
        'conference': 'Eastern',
        'displayAbbr': 'IND',
        'displayConference': 'Eastern',
        'division': 'Central',
        'id': '1610612754',
        'name': 'Pacers',
        'color': '001D4A',
        'colors': ['001D4A', 'FEAC2D', 'B0B2B5']
    }, 'LAC': {
        'abbr': 'LAC',
        'city': 'Los Angeles',
        'code': 'clippers',
        'conference': 'Western',
        'displayAbbr': 'LAC',
        'displayConference': 'Western',
        'division': 'Pacific',
        'id': '1610612746',
        'name': 'Clippers',
        'color': '00559A',
        'colors': ['00559A', 'EC003D']
    }, 'LAL': {
        'abbr': 'LAL',
        'city': 'Los Angeles',
        'code': 'lakers',
        'conference': 'Western',
        'displayAbbr': 'LAL',
        'displayConference': 'Western',
        'division': 'Pacific',
        'id': '1610612747',
        'name': 'Lakers',
        'color': 'FEA927',
        'colors': ['FEA927', '42186E', '000000']
    }, 'MEM': {
        'abbr': 'MEM',
        'city': 'Memphis',
        'code': 'grizzlies',
        'conference': 'Western',
        'displayAbbr': 'MEM',
        'displayConference': 'Western',
        'division': 'Southwest',
        'id': '1610612763',
        'name': 'Grizzlies',
        'color': '182A48',
        'colors': ['182A48', '4C78AD', 'FEA927', 'AAC8E5']
    }, 'MIA': {
        'abbr': 'MIA',
        'city': 'Miami',
        'code': 'heat',
        'conference': 'Eastern',
        'displayAbbr': 'MIA',
        'displayConference': 'Eastern',
        'division': 'Southeast',
        'id': '1610612748',
        'name': 'Heat',
        'color': '98002E',
        'colors': ['98002E', 'F88D1D', '000000']
    }, 'MIL': {
        'abbr': 'MIL',
        'city': 'Milwaukee',
        'code': 'bucks',
        'conference': 'Eastern',
        'displayAbbr': 'MIL',
        'displayConference': 'Eastern',
        'division': 'Central',
        'id': '1610612749',
        'name': 'Bucks',
        'color': 'C41230',
        'colors': ['C41230', '003815', 'BAC4CA']
    }, 'MIN': {
        'abbr': 'MIN',
        'city': 'Minnesota',
        'code': 'timberwolves',
        'conference': 'Western',
        'displayAbbr': 'MIN',
        'displayConference': 'Western',
        'division': 'Northwest',
        'id': '1610612750',
        'name': 'Timberwolves',
        'color': '#003F70',
        'colors': ['003F70', '006F42', 'BAC4CA', 'FFE211', 'DE2032', '000000']
    }, 'NOP': {
        'abbr': 'NOP',
        'city': 'New Orleans',
        'code': 'pelicans',
        'conference': 'Western',
        'displayAbbr': 'NOP',
        'displayConference': 'Western',
        'division': 'Southwest',
        'id': '1610612740',
        'name': 'Pelicans',
        'color': '#002B5C',
        'colors': ['002B5C', 'B4975A', 'E13A3E']
    }, 'NYK': {
        'abbr': 'NYK',
        'city': 'New York',
        'code': 'knicks',
        'conference': 'Eastern',
        'displayAbbr': 'NYK',
        'displayConference': 'Eastern',
        'division': 'Atlantic',
        'id': '1610612752',
        'name': 'Knicks',
        'color': 'F3571F',
        'colors': ['F3571F', '0067B2', 'BAC4CA']
    }, 'OKC': {
        'abbr': 'OKC',
        'city': 'Oklahoma City',
        'code': 'thunder',
        'conference': 'Western',
        'displayAbbr': 'OKC',
        'displayConference': 'Western',
        'division': 'Northwest',
        'id': '1610612760',
        'name': 'Thunder',
        'color': 'FDBB30',
        'colors': ['FDBB30', 'F05133', '007DC3', '002D62']
    }, 'ORL': {
        'abbr': 'ORL',
        'city': 'Orlando',
        'code': 'magic',
        'conference': 'Eastern',
        'displayAbbr': 'ORL',
        'displayConference': 'Eastern',
        'division': 'Southeast',
        'id': '1610612753',
        'name': 'Magic',
        'color': '006BB7',
        'colors': ['006BB7', 'BAC4CA', '000000']
    }, 'PHI': {
        'abbr': 'PHI',
        'city': 'Philadelphia',
        'code': 'sixers',
        'conference': 'Eastern',
        'displayAbbr': 'PHI',
        'displayConference': 'Eastern',
        'division': 'Atlantic',
        'id': '1610612755',
        'name': 'Sixers',
        'color': 'EC003D',
        'colors': ['EC003D', '00559A', 'BAC4CA']
    }, 'PHX': {
        'abbr': 'PHX',
        'city': 'Phoenix',
        'code': 'suns',
        'conference': 'Western',
        'displayAbbr': 'PHX',
        'displayConference': 'Western',
        'division': 'Pacific',
        'id': '1610612756',
        'name': 'Suns',
        'color': 'E45F1F',
        'colors': ['E45F1F', 'F89F1B', 'BAC4CA', '000000']
    }, 'POR': {
        'abbr': 'POR',
        'city': 'Portland',
        'code': 'blazers',
        'conference': 'Western',
        'displayAbbr': 'POR',
        'displayConference': 'Western',
        'division': 'Northwest',
        'id': '1610612757',
        'name': 'Trail Blazers',
        'color': 'DE2032',
        'colors': ['DE2032', 'BAC4CA', '000000']
    }, 'SAC': {
        'abbr': 'SAC',
        'city': 'Sacramento',
        'code': 'kings',
        'conference': 'Western',
        'displayAbbr': 'SAC',
        'displayConference': 'Western',
        'division': 'Pacific',
        'id': '1610612758',
        'name': 'Kings',
        'color': '542E91',
        'colors': ['542E91', 'BAC4CA', '000000']
    }, 'SAS': {
        'abbr': 'SAS',
        'city': 'San Antonio',
        'code': 'spurs',
        'conference': 'Western',
        'displayAbbr': 'SAS',
        'displayConference': 'Western',
        'division': 'Southwest',
        'id': '1610612759',
        'name': 'Spurs',
        'color': '#BA24CA',
        'colors': ['BA24CA', '000000']
    }, 'TOR': {
        'abbr': 'TOR',
        'city': 'Toronto',
        'code': 'raptors',
        'conference': 'Eastern',
        'displayAbbr': 'TOR',
        'displayConference': 'Eastern',
        'division': 'Atlantic',
        'id': '1610612761',
        'name': 'Raptors',
        'color': 'C60033',
        'colors': ['C60033', 'BAC4CA']
    }, 'UTA': {
        'abbr': 'UTA',
        'city': 'Utah',
        'code': 'jazz',
        'conference': 'Western',
        'displayAbbr': 'UTA',
        'displayConference': 'Western',
        'division': 'Northwest',
        'id': '1610612762',
        'name': 'Jazz',
        'color': '#002A5C',
        'colors': ['002A5C', '004812', 'FCB034', 'BACA4CA']
    }, 'WAS': {
        'abbr': 'WAS',
        'city': 'Washington',
        'code': 'wizards',
        'conference': 'Eastern',
        'displayAbbr': 'WAS',
        'displayConference': 'Eastern',
        'division': 'Southeast',
        'id': '1610612764',
        'name': 'Wizards',
        'color': '002A5B',
        'colors': ['002A5B', 'E21836', 'BAC4CA']
    }
}


class _DefaultN:
    Default = 'N'


class _DefaultBlank:
    Default = ''


class _DefaultZero:
    Default = '0'


class League:
    NBA = '00'
    Default = NBA


class PerMode:
    Totals = 'Totals'
    PerGame = 'PerGame'
    MinutesPer = 'MinutesPer'
    Per48 = 'Per48'
    Per40 = 'Per40'
    Per36 = 'Per36'
    PerMinute = 'PerMinute'
    PerPossession = 'PerPossession'
    PerPlay = 'PerPlay'
    Per100Possessions = 'Per100Possessions'
    Per100Plays = 'Per100Plays'
    Default = PerGame


class SeasonType:
    Regular = 'Regular Season'
    Playoffs = 'Playoffs'
    Default = Regular


class MeasureType:
    Base = 'Base'
    Advanced = 'Advanced'
    Misc = 'Misc'
    FourFactors = 'Four Factors'
    Scoring = 'Scoring'
    Opponent = 'Opponent'
    Usage = 'Usage'
    Default = Base


class PtMeasureType:
    SpeedDistance = 'SpeedDistance'


class GroupQuantity:
    Default = 5


class Outcome(_DefaultBlank):
    Win = 'W'
    Loss = 'L'


class Location(_DefaultBlank):
    Home = 'Home'
    Away = 'Away'


class SeasonSegment(_DefaultBlank):
    EntireSeason = ''
    PreAllStar = 'Pre All-Star'
    PostAllStar = 'Post All-Star'


class DateFrom(_DefaultBlank):
    pass


class DateTo(_DefaultBlank):
    pass


class VsConference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'


class VsDivision(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'


class GameSegment(_DefaultBlank):
    EntireGame = ''
    FirstHalf = 'First Half'
    SecondHalf = 'Second Half'
    Overtime = 'Overtime'


class ClutchTime(_DefaultBlank):
    Last5Min = 'Last 5 Minutes'
    Last4Min = 'Last 4 Minutes'
    Last3Min = 'Last 3 Minutes'
    Last2Min = 'Last 2 Minutes'
    Last1Min = 'Last 1 Minutes'
    Last30Sec = 'Last 30 Seconds'
    Last10Sec = 'Last 10 Seconds'


class ShotClockRange(_DefaultBlank):
    AllRanges = ''
    # I honestly don't know anytime the shot clock would be off
    ShotClockOff = 'ShotClock Off'

    def get(self, n):
        if n > 24 or n < 0:
            return ''
        elif 22 <= n <= 24:
            return '24-22'
        elif 18 <= n < 22:
            return '22-18 Very Early'
        elif 15 <= n < 18:
            return '18-15 Early'
        elif 7 <= n < 15:
            return '15-7 Average'
        elif 4 <= n < 7:
            return '7-4 Late'
        elif 0 <= n < 4:
            return '4-0 Very Late'


class AheadBehind(_DefaultBlank):
    AheadOrBehind = 'Ahead or Behind'
    AheadOrTied = 'Ahead or Tied'
    BehindOrTied = 'Behind or Tied'


class PlusMinus(_DefaultN):
    pass


class PaceAdjust(_DefaultN):
    pass


class Rank(_DefaultN):
    pass


class OpponentTeamID(_DefaultZero):
    pass


class Period(_DefaultZero):
    AllQuarters = '0'
    FirstQuarter = '1'
    SecondQuarter = '2'
    ThirdQuarter = '3'
    FourthQuarter = '4'

    def Overtime(self, n):
        return str(4 + n)


class LastNGames(_DefaultZero):
    pass


class PlayoffRound(_DefaultZero):
    All = '0'
    QuarterFinals = '1'
    SemiFinals = '2'
    ConferenceFinals = '3'
    Finals = '4'


class Month(_DefaultZero):
    All = '0'
    October = '1'
    November = '2'
    December = '3'
    January = '4'
    February = '5'
    March = '6'
    April = '7'
    May = '8'
    June = '9'
    July = '10'
    August = '11'
    September = '12'


class RangeType(_DefaultZero):
    pass


class StartRange(_DefaultZero):
    pass


class EndRange(_DefaultZero):
    pass


class StartPeriod(Period):
    pass


class EndPeriod(Period):
    pass


class StatCategory:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG%'
    FG3M = '3PM'
    FG3A = '3PA'
    FG3_PCT = '3P%'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT%'
    OREB = 'OREB'
    DREB = 'DREB'
    REB = 'REB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    EFF = 'EFF'
    AST_TOV = 'AST/TO'
    STL_TOV = 'STL/TOV'
    PF = 'PF'
    Default = PTS


class ContextMeasure:
    # Not sure if this is mapped correctly. Source:
    # https://github.com/bradleyfay/NBAStats
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG_PCT'
    FG3M = 'FG3m'
    FG3A = 'FG3A'
    FG3_PCT = 'FG3_PCT'
    PF = 'PF'
    EFG_PCT = 'EFG_PCT'
    TS_PCT = 'TS_PCT'
    PTS_FB = 'PTS_FB'
    PTS_OFF_TOV = 'PTS_OFF_TOV'
    PTS_2ND_CHANCE = 'PTS_2ND_CHANCE'
    Default = FGM


class Scope:
    AllPlayers = 'S'
    Rookies = 'Rookies'
    Default = AllPlayers


class PlayerScope:
    # ugh this is so similar to Scope, why does it have its own
    AllPlayers = 'All Players'
    Rookies = 'Rookie'
    Default = AllPlayers


class PlayerOrTeam:
    Player = 'Player'
    Team = 'Team'
    Default = Player


class GameScope:
    Season = 'Season'
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'
    Finals = 'Finals'
    Default = Season


class Game_Scope(_DefaultBlank):
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'


class Player_or_Team:
    Player = 'P'
    Team = 'T'
    Default = Player


class Conference(VsConference):
    pass


class Division(VsDivision):
    pass


class TeamID(_DefaultZero):
    pass


class GameID(_DefaultBlank):
    pass


class RookieYear(_DefaultBlank):
    pass


class PlayerExperience(_DefaultBlank):
    Rookie = 'Rookie'
    Sophomore = 'Sophomore'
    Veteran = 'Veteran'


class PlayerPosition(_DefaultBlank):
    Forward = 'F'
    Center = 'C'
    Guard = 'G'


class StarterBench(_DefaultBlank):
    Starters = 'Starters'
    Bench = 'Bench'


class DraftYear(_DefaultBlank):
    pass


class DraftPick(_DefaultBlank):
    FirstRound = '1st+Round'
    SecondRound = '2nd+Round'
    FirstPick = '1st+Pick'
    Lottery = 'Lottery+Pick'
    Top5 = 'Top+5+Pick'
    Top10 = 'Top+10+Pick'
    Top15 = 'Top+15+Pick'
    Top20 = 'Top+20+Pick'
    Top25 = 'Top+25+Pick'
    Picks11Thru20 = 'Picks+11+Thru+20'
    Picks21Thru30 = 'Picks+21+Thru+30'
    Undrafted = 'Undrafted'


class College(_DefaultBlank):
    pass


class Country(_DefaultBlank):
    pass


class Height(_DefaultBlank):
    '''
    Example:
    for greater than 6ft8 api call should be GT+6-8
    for lower than 7ft3 api call should be LT+7-3
    '''


class Weight(_DefaultBlank):
    '''
    Example:
    for greater than 225lbs api call should be GT+225lbs
    '''


class Counter:
    Default = '1000'


class Sorter:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG_PCT'
    FG3M = 'FG3M'
    FG3A = 'FG3A'
    FG3_PCT = 'FG3_PCT'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT_PCT'
    OREB = 'OREB'
    DREB = 'DREB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    REB = 'REB'
    Default = PTS


class Direction:
    DESC = 'DESC'
    ASC = 'ASC'
    Default = DESC
