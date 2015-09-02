# *nba_py - [stats.nba.com](http://stats.nba.com) API for python*

## Summary
A python facing API for stats.nba.com (Still in heavy development)

Originally based off <https://github.com/bradleyfay/NBAStats>

`Current Version = 0.1a1`
[![Build Status](https://travis-ci.org/seemethere/nba_py.svg?branch=master)](https://travis-ci.org/seemethere/nba_py)

## Dependencies
  * [pandas](http://pandas.pydata.org/) [(Installation Help)](https://github.com/seemethere/nba_py/wiki/Installing-pandas)


## Things that are currently finished
#### 1. Main Package
| Class Name                |  Endpoint                             |
|:--------------------------|:--------------------------------------|
| Scoreboard                | Scoreboard                            |

#### 2. Game
| Class Name                |  Endpoint                             |
|:--------------------------|:--------------------------------------|
| Boxscore                  | boxscore                              |
| BoxscoreScoring           | boxscorescoring                       |
| BoxscoreUsage             | boxscoreusage                         |
| BoxscoreMisc              | boxscoremisc                          |
| BoxscoreAdvanced          | boxscoreadvanced                      |
| BoxscoreFourFactors       | boxscorefourfactors                   |
| PlayByPlay                | playbyplay                            |

#### 3. Player (All endpoints mapped)
| Class Name                |  Endpoint                             |
|:--------------------------|:--------------------------------------|
| PlayerList                | commonallplayers                      |
| PlayerSummary             | commonplayerinfo                      |
| PlayerProfile             | playerprofilev2                       |
| PlayerGeneralSplits       | playerdashboardbygeneralsplits        |
| PlayerOpponenetSplits     | playeropponentsplits                  |
| PlayerLastNGamesSplits    | playerdashboardbylastngames           |
| PlayerInGameSplits        | playerdashboardbygamesplits           |
| PlayerClutchSplits        | playerdashboardbyclutch               |
| PlayerShootingSplits      | playerdashboardbyshootingsplits       |
| PlayerPerformanceSplits   | playerdashboardbyplayerperformance    |
| PlayerYearOverYearSplits  | playerdashboardbyyearoveryear         |
| PlayerCareer              | playercareerstats                     |
| PlayerGameLogs            | playergamelog                         |
| PlayerShotTracking        | playerdashptshots                     |
| PlayerReboundTracking     | playerdashptreb                       |
| PlayerPassTracking        | playerdashptpass                      |
| PlayerDefenseTracking     | playerdashptshotdefend                |
| PlayerShotLogTracking     | playerdashptshotlog                   |
| PlayerReboundLogTracking  | playerdashptreboundlogs               |
| PlayerVsPlayer            | playervsplayer                        |

#### 4. Team (All endpoints mapped)
| Class Name                |  Endpoint                             |
|:--------------------------|:--------------------------------------|
| TeamSummary               | commoninfocommon                      |
| TeamList                  | commonteamyears                       |
| TeamCommonRoster          | commonteamroster                      |
| TeamGeneralSplits         | teamdashboardbygeneralsplits          |
| TeamOpponenetSplits       | teamdashboardbyopponent               |
| TeamLastNGamesSplits      | teamdashboardbylastngames             |
| TeamInGameSplits          | teamdashboardbygamesplits             |
| TeamClutchSplits          | teamdashboardbyclutch                 |
| TeamShootingSplits        | teamdashboardbyshootingsplits         |
| TeamPerformanceSplits     | teamdashboardbyteamperformance        |
| TeamYearOverYearSplits    | teamdashboardbyyearoveryear           |
| TeamLineups               | teamdashlineups                       |
| TeamPlayers               | teamplayerdashboard                   |
| TeamPlayersOnOffDetail    | teamplayeronoffdetails                |
| TeamPlayerOnOffSummary    | teamplayeronoffsummary                |
| TeamGameLogs              | teamgamelog                           |
| TeamSeasons               | teamyearbyyearstats                   |
| TeamShotTracking          | teamdashptshots                       |
| TeamReboundTracking       | teamdashptreb                         |
| TeamPassTracking          | teamdashptpass                        |
| TeamVsPlayer              | teamvsplayer                          |

## Planned development
#### 1. Documentation
  * All around documentation not only of nba_py but also stats.nba.com (it's pretty nonexistent)

#### ~~2. Map rest of API~~ (Completed)
