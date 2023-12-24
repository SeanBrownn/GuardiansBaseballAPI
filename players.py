import datetime

import pybaseball

class players:

    current_year = datetime.datetime.now().year

    @staticmethod
    def get_batting_stats(start_season: int = current_year, end_season: int = None, league: str = 'all',
                          qual: int = None, split_seasons: bool = False):
        return pybaseball.batting_stats(start_season, end_season, league, qual, split_seasons).to_json(orient='records')
    #def get_batting_stats(start_season: int = current_year, end_season: int = None, league: str = 'ALL',
     #                    stat_columns = 'ALL', qual: int = None, split_seasons: bool = False, month: str = 'ALL',
      #                   on_active_roster: bool = False, minimum_age: int = 0, maximum_age: int = 100,
       #                  team: str = None, position: str = 'ALL', max_results: int = 1000000):
       # return pybaseball.batting_stats(start_season, end_season, league, stat_columns, qual, split_seasons, month,
        #                               on_active_roster, minimum_age, maximum_age, team, position,
         #                              max_results).to_json(orient='records')

    @staticmethod
    def get_batting_stats_bref(season: int = current_year):
        return pybaseball.batting_stats_bref(season).to_json(orient='records')

    # string formats: 'YYYY-MM-DD'
    @staticmethod
    def get_batting_stats_range(start_dt: str, end_dt: str = None):
        return pybaseball.batting_stats_range(start_dt, end_dt).to_json(orient='records')

    @staticmethod
    def get_bwar_bat(return_all: bool = False):
        return pybaseball.bwar_bat(return_all).to_json(orient='records')

    @staticmethod
    def get_bwar_pitch(return_all: bool = False):
        return pybaseball.bwar_pitch(return_all).to_json(orient='records')

    @staticmethod
    def get_chadwick_register(save: bool = False):
        return pybaseball.chadwick_register(save).to_json(orient='records')

    @staticmethod
    def get_pitching_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None, ind: int = 1):
        return pybaseball.pitching_stats(start_season, end_season, league, qual, ind).to_json(orient='records')