import datetime
from typing import Annotated

import pybaseball
from fastapi import Query


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

    @staticmethod
    def get_pitching_stats_bref(start_season: int = current_year):
        return pybaseball.pitching_stats_bref(start_season).to_json(orient='records')

    # string formats: 'YYYY-MM-DD'
    @staticmethod
    def get_pitching_stats_range(start_dt: str, end_dt: str = None):
        return pybaseball.pitching_stats_range(start_dt, end_dt).to_json(orient='records')

    # last, first (last and first name) are case-insensitive
    # fuzzy: if true, searches for inexact name matches, returns 5 closest players
    @staticmethod
    def get_player_id_lookup(last: str, first: str = None, fuzzy: bool = False):
        return pybaseball.playerid_lookup(last, first, fuzzy).to_json(orient='records')

    @staticmethod
    def get_player_id_reverse_lookup(player_ids: Annotated[list[int], Query()], key_type: str = 'mlbam'):
        return pybaseball.playerid_reverse_lookup(player_ids, key_type).to_json(orient='records')

    @staticmethod
    def get_splits(playerid: str, year: int = None, player_info: bool = None, pitching_splits: bool = None):
        result = pybaseball.get_splits(playerid, year, player_info, pitching_splits)
        if player_info:
            splits_df, player_info_dict = result
            return splits_df.to_json(orient='records'), player_info_dict
        else:
            return result.to_json(orient='records')

    @staticmethod
    def get_statcast_batter(player_id: int, start_dt: str = None, end_dt: str = None):
        return pybaseball.statcast_batter(start_dt, end_dt, player_id).to_json(orient='records')
