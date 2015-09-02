from nba_py import game

# pbp = game.PlayByPlay('0041400122')
# print pbp.info()
bs = game.Boxscore('0041400122')
print bs.game_summary()
bss = game.BoxscoreScoring('0041400122')
print bss.sql_team_scoring()
bsu = game.BoxscoreUsage('0041400122')
print bss.sql_team_usage()
bsa = game.BoxscoreAdvanced('0041400122')
print bss.sql_team_advanced()
bsf = game.BoxscoreFourFactors('0041400122')
print bss.sql_team_four_factors()
