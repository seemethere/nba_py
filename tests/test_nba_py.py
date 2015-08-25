import nba_py
# from pandas import DataFrame

sc = nba_py.Scoreboard(month=2, day=21, year=2015)
print sc.game_header()
