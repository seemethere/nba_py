from nba_py import player

pd = player.PlayerDashboard('203507')
print pd.starting_position()

ap = player.CommonAllPlayers()
print ap.info()

pc = player.PlayerInfoCommon('203507')
print pc.headline_stats()
