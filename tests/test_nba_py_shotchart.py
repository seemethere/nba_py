from nba_py import shotchart
from nba_py.player import get_player

def test():
    pid = get_player('Kevin', 'Durant')
    assert shotchart.ShotChart(pid)