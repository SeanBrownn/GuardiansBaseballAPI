import datetime
from typing import Annotated

import pybaseball
from fastapi import Query


class players:
    current_year = datetime.datetime.now().year

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

    @staticmethod
    def get_statcast_pitcher(start_dt: str, end_dt: str, player_id: int):
        return pybaseball.statcast_pitcher(start_dt, end_dt, player_id).to_json(orient='records')
