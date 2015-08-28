# *nba_py - [stats.nba.com](http://stats.nba.com) API for python*

## Summary
A python facing API for stats.nba.com (Still in heavy development)

Originally based off <https://github.com/bradleyfay/NBAStats>

`Current Version = 0.1a1`

## Dependencies
  * [pandas](http://pandas.pydata.org/)


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

#### 3. Player
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

#### 2. Map rest of API
  * This is gonna be a little tough but I've devised a way to map the rest of the api and hopefully within a couple of weeks most, if not all, of the api will be mapped.
