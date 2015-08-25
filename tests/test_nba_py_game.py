from nba_py import game

pbp = game.PlayByPlay('0041400122')
print pbp.info()
bs = game.Boxscore('0041400122')
print bs.game_summary()
