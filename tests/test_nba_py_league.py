from nba_py import league
try:
    # python 2 compatability
    from future_builtins import filter
except ImportError:
    pass

class TestPlayerSpeedDistanceTracking:

    def test_overall(self):
        speed = league.PlayerSpeedDistanceTracking(date_from='03/05/2016',
                                                   date_to='03/05/2016', season="2015-16")
        assert speed
        overall = speed.overall()
        assert overall
        iter = filter(lambda d: d['PLAYER_NAME'] == 'Derrick Rose', overall)
        stats = next(iter)
        assert stats
        assert stats['GP'] == 1
        assert stats['MIN'] == 29.25
        assert stats['DIST_MILES'] == 2.24
        assert stats['DIST_FEET'] == 11827.0
        assert stats['DIST_MILES_OFF'] == 1.29
        assert stats['DIST_MILES_DEF'] == 0.95
        assert stats['AVG_SPEED'] == 4.52
        assert stats['AVG_SPEED_OFF'] == 4.94
        assert stats['AVG_SPEED_DEF'] == 4.42
