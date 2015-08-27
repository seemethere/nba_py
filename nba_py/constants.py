# from enum import Enum

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


class League:
    NBA = '00'


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


class SeasonType:
    Regular = 'Regular Season'
    Playoffs = 'Playoffs'


class MeasureType:
    Base = 'Base'
    Advanced = 'Advanced'
    Misc = 'Misc'
    FourFactors = 'Four Factors'
    Scoring = 'Scoring'
    Opponent = 'Opponent'
    Usage = 'Usage'
