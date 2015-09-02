from nba_py import player

pd = player.PlayerDashboard('203507')
print pd.starting_position()

ap = player.CommonAllPlayers()
print ap.info()

pc = player.PlayerInfoCommon('203507')
print pc.headline_stats()

p_cstats = player.PlayerCareerStats('201939')
print p_cstats.regular_season_career_totals()
