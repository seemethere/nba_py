# from enum import Enum


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
