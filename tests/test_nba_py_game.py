from nba_py import game

def test():
    gid = '0041400122'
    assert game.BoxscoreSummary(gid)
    assert game.Boxscore(gid)
    assert game.BoxscoreScoring(gid)
    assert game.BoxscoreUsage(gid)
    assert game.BoxscoreMisc(gid)
    assert game.BoxscoreAdvanced(gid)
    assert game.BoxscoreFourFactors(gid)
    assert game.PlayByPlay(gid)
