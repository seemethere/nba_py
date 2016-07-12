from nba_py import draftcombine
try:
    # python 2 compatability
    from future_builtins import filter
except ImportError:
    pass


class TestSummary:

    def setup(self):
        self.player_name = 'Devin Booker'
        self.season = '2015-16'

    def test_overall(self):
        results = draftcombine.Summary(season=self.season)
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
        self.season = '2015-16'

    def test_overall(self):
        results = draftcombine.DrillResults(season=self.season)
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


class TestSpotShooting:

    def setup(self):
        self.player_name = 'Devin Booker'
        self.season = '2015-16'

    def test_overall(self):
        results = draftcombine.SpotShooting(season=self.season)
        assert results

        overall = results.overall()
        assert overall

        stats = next(filter(lambda d: d['PLAYER_NAME'] == self.player_name, overall))
        assert stats

        assert stats['PLAYER_NAME'] == self.player_name
        assert stats['COLLEGE_BREAK_LEFT_MADE'] == None
        assert stats['COLLEGE_BREAK_LEFT_PCT'] == None
        assert stats['COLLEGE_BREAK_RIGHT_ATTEMPT'] == None
        assert stats['COLLEGE_BREAK_RIGHT_MADE'] == None
        assert stats['COLLEGE_BREAK_RIGHT_PCT'] == None
        assert stats['COLLEGE_CORNER_LEFT_ATTEMPT'] == None
        assert stats['COLLEGE_CORNER_LEFT_MADE'] == None
        assert stats['COLLEGE_CORNER_LEFT_PCT'] == None
        assert stats['COLLEGE_CORNER_RIGHT_ATTEMPT'] == None
        assert stats['COLLEGE_CORNER_RIGHT_MADE'] == None
        assert stats['COLLEGE_CORNER_RIGHT_PCT'] == None
        assert stats['COLLEGE_TOP_KEY_ATTEMPT'] == None
        assert stats['COLLEGE_TOP_KEY_MADE'] == None
        assert stats['COLLEGE_TOP_KEY_PCT'] == None
        assert stats['FIFTEEN_BREAK_LEFT_ATTEMPT'] == None
        assert stats['FIFTEEN_BREAK_LEFT_MADE'] == None
        assert stats['FIFTEEN_BREAK_LEFT_PCT'] == None
        assert stats['FIFTEEN_BREAK_RIGHT_ATTEMPT'] == None
        assert stats['FIFTEEN_BREAK_RIGHT_MADE'] == None
        assert stats['FIFTEEN_BREAK_RIGHT_PCT'] == None
        assert stats['FIFTEEN_CORNER_LEFT_ATTEMPT'] == None
        assert stats['FIFTEEN_CORNER_LEFT_MADE'] == None
        assert stats['FIFTEEN_CORNER_LEFT_PCT'] == None
        assert stats['FIFTEEN_CORNER_RIGHT_ATTEMPT'] == None
        assert stats['FIFTEEN_CORNER_RIGHT_MADE'] == None
        assert stats['FIFTEEN_CORNER_RIGHT_PCT'] == None
        assert stats['FIFTEEN_TOP_KEY_ATTEMPT'] == None
        assert stats['FIFTEEN_TOP_KEY_MADE'] == None
        assert stats['FIFTEEN_TOP_KEY_PCT'] == None
        assert stats['NBA_BREAK_LEFT_ATTEMPT'] == None
        assert stats['NBA_BREAK_LEFT_MADE'] == None
        assert stats['NBA_BREAK_LEFT_PCT'] == None
        assert stats['NBA_BREAK_RIGHT_ATTEMPT'] == None
        assert stats['NBA_BREAK_RIGHT_MADE'] == None
        assert stats['NBA_BREAK_RIGHT_PCT'] == None
        assert stats['NBA_CORNER_LEFT_ATTEMPT'] == None
        assert stats['NBA_CORNER_LEFT_MADE'] == None
        assert stats['NBA_CORNER_LEFT_PCT'] == None
        assert stats['NBA_CORNER_RIGHT_ATTEMPT'] == None
        assert stats['NBA_CORNER_RIGHT_MADE'] == None
        assert stats['NBA_CORNER_RIGHT_PCT'] == None
        assert stats['NBA_TOP_KEY_ATTEMPT'] == None
        assert stats['NBA_TOP_KEY_MADE'] == None
        assert stats['NBA_TOP_KEY_PCT'] == None
        assert stats['PLAYER_ID'] == None
