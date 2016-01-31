from nba_py import player
from nba_py.player import get_player


def test():
    pid = get_player('Tim', 'Duncan')
    vs_pid = get_player('Stephen', 'Curry')
    assert player.PlayerList()
    assert player.PlayerSummary(pid)
    # assert player.PlayerGeneralSplits(pid)
    # assert player.PlayerOpponentSplits(pid)
    assert player.PlayerLastNGamesSplits(pid)
    assert player.PlayerInGameSplits(pid)
    assert player.PlayerClutchSplits(pid)
    # assert player.PlayerShootingSplits(pid)
    assert player.PlayerPerformanceSplits(pid)
    assert player.PlayerYearOverYearSplits(pid)
    assert player.PlayerCareer(pid)
    assert player.PlayerProfile(pid)
    assert player.PlayerGameLogs(pid)
    assert player.PlayerShotTracking(pid)
    assert player.PlayerReboundTracking(pid)
    assert player.PlayerPassTracking(pid)
    assert player.PlayerDefenseTracking(pid)
    # assert player.PlayerShotLogTracking(pid)
    # assert player.PlayerReboundLogTracking(pid)
    assert player.PlayerVsPlayer(pid, vs_pid)
