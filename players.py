import datetime

import pybaseball

class players:

    current_year = datetime.datetime.now().year

    @staticmethod
    def get_batting_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None, ind: int = 1):
        return pybaseball.batting_stats(start_season, end_season, league, qual, ind)

    @staticmethod
    def get_batting_stats_bref(season: int = current_year):
        return pybaseball.batting_stats_bref(season)

    # string formats: 'YYYY-MM-DD'
    @staticmethod
    def get_batting_stats_range(start_dt: str, end_dt: str = None):
        return pybaseball.batting_stats_range(start_dt, end_dt)

    @staticmethod
    def get_bwar_bat(return_all: bool = False):
        return pybaseball.bwar_bat(return_all)

    @staticmethod
    def get_bwar_pitch(return_all: bool = False):
        return pybaseball.bwar_pitch(return_all)

    @staticmethod
    def get_chadwick_register(save: bool = False):
        return pybaseball.chadwick_register(save)

    @staticmethod
    def get_pitching_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None, ind: int = 1):
        return pybaseball.pitching_stats(start_season, end_season, league, qual, ind)