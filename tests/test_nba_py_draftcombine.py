from nba_py import draftcombine
try:
    # python 2 compatability
    from future_builtins import filter
except ImportError:
    pass


class TestSummary:

    def setup(self):
        self.player_name = 'Devin Booker'

    def test_overall(self):
        results = draftcombine.Summary(season='2015-16')
        assert results

        overall = results.overall()
        assert overall

        stats = next(filter(lambda d: d['PLAYER_NAME'] == self.player_name, overall))
        assert stats

        assert stats['POSITION'] == 'SG'
        assert stats['MAX_VERTICAL_LEAP'] == 34.5
        assert stats['MODIFIED_LANE_AGILITY_TIME'] == 2.75
        assert stats['STANDING_REACH'] == 102.5
        assert stats['HEIGHT_WO_SHOES'] == 76.5
        assert stats['WINGSPAN'] == 80.25
        assert stats['STANDING_VERTICAL_LEAP'] == 27.5
        assert stats['BENCH_PRESS'] == 8
        assert stats['HAND_WIDTH'] == 9.0
        assert stats['HEIGHT_W_SHOES'] == 77.75
        assert stats['THREE_QUARTER_SPRINT'] == 3.28
        assert stats['HAND_LENGTH'] == 8.75
        assert stats['LANE_AGILITY_TIME'] == 10.27
        assert stats['BODY_FAT_PCT'] == 8.3


class TestDrillResults:

    def setup(self):
        self.player_name = 'Devin Booker'

    def test_overall(self):
        results = draftcombine.DrillResults(season='2015-16')
        assert results

        overall = results.overall()
        assert overall

        stats = next(filter(lambda d: d['PLAYER_NAME'] == self.player_name, overall))
        assert stats

        assert stats['POSITION'] == 'SG'
        assert stats['MAX_VERTICAL_LEAP'] == 34.5
        assert stats['MODIFIED_LANE_AGILITY_TIME'] == 2.75
        assert stats['STANDING_VERTICAL_LEAP'] == 27.5
        assert stats['THREE_QUARTER_SPRINT'] == 3.28
