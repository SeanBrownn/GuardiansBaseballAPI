import datetime
from typing import Union

import pybaseball


class mlb:
    current_year = datetime.datetime.now().year

    @staticmethod
    def get_amateur_draft(draft_round: int, year: int = current_year, keep_stats: bool = True):
        return pybaseball.amateur_draft(year, draft_round, keep_stats).to_json(orient='records')

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
    def get_pitching_stats(start_season: int = current_year, end_season: int = None, league: str = 'all',
                           qual: int = None, ind: int = 1):
        return pybaseball.pitching_stats(start_season, end_season, league, qual, ind).to_json(orient='records')

    @staticmethod
    def get_pitching_stats_bref(start_season: int = current_year):
        return pybaseball.pitching_stats_bref(start_season).to_json(orient='records')

    # string formats: 'YYYY-MM-DD'
    @staticmethod
    def get_pitching_stats_range(start_dt: str, end_dt: str = None):
        return pybaseball.pitching_stats_range(start_dt, end_dt).to_json(orient='records')

    @staticmethod
    def get_standings(season: int = current_year):
        json_string = [df.to_json(orient='records') for df in pybaseball.standings(season)]
        return json_string

    # for start_dt and end_dt, format = 'YYYY-MM-DD'
    # to get data for only 1 date, enter a start date but not an end date
    @staticmethod
    def get_statcast(start_dt: str = None, end_dt: str = None, team: str = None, verbose: bool = True,
                     parallel: bool = True):
        return pybaseball.statcast(start_dt, end_dt, team, verbose, parallel).to_json(orient='records')

    # can enter position by number or name
    @staticmethod
    def get_statcast_outs_above_average(year: int, pos: Union[int, str], min_att: Union[int, str] = "q",
                                        view: str = "Fielder"):
        return pybaseball.statcast_outs_above_average(year, pos, min_att, view).to_json(orient='records')

    @staticmethod
    def get_statcast_outfield_directional_oaa(year: int, min_opp: Union[int, str] = "q"):
        return pybaseball.statcast_outfield_directional_oaa(year, min_opp).to_json(orient='records')

    @staticmethod
    def get_statcast_outfield_catch_prob(year: int, min_opp: Union[int, str] = "q"):
        return pybaseball.statcast_outfield_catch_prob(year, min_opp).to_json(orient='records')

    @staticmethod
    def get_statcast_outfielder_jump(year: int, min_att: Union[int, str] = "q"):
        return pybaseball.statcast_outfielder_jump(year, min_att).to_json(orient='records')

    @staticmethod
    def get_statcast_catcher_poptime(year: int, min_2b_att: int = 5, min_3b_att: int = 0):
        return pybaseball.statcast_catcher_poptime(year, min_2b_att, min_3b_att).to_json(orient='records')

    @staticmethod
    def get_statcast_catcher_framing(year: int, min_called_p: Union[int, str] = "q"):
        return pybaseball.statcast_catcher_framing(year, min_called_p).to_json(orient='records')

    @staticmethod
    def get_statcast_batter_exitvelo_barrels(year: int, minBBE: int = None):
        return pybaseball.statcast_batter_exitvelo_barrels(year, minBBE).to_json(orient='records')

    @staticmethod
    def get_statcast_batter_expected_stats(year: int, minPA: int = None):
        return pybaseball.statcast_batter_expected_stats(year, minPA).to_json(orient='records')

    @staticmethod
    def get_statcast_batter_percentile_ranks(year: int):
        return pybaseball.statcast_batter_percentile_ranks(year).to_json(orient='records')

    @staticmethod
    def get_statcast_batter_pitch_arsenal(year: int, minPA: int = 25):
        return pybaseball.statcast_batter_pitch_arsenal(year, minPA).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_exitvelo_barrels(year: int, minBBE: int):
        return pybaseball.statcast_pitcher_exitvelo_barrels(year, minBBE).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_expected_stats(year: int, minPA: int = None):
        return pybaseball.statcast_pitcher_expected_stats(year, minPA).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_pitch_arsenal(year: int, minP: int, arsenal_type: str = "avg_speed"):
        return pybaseball.statcast_pitcher_pitch_arsenal(year, minP, arsenal_type).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_arsenal_stats(year: int, minPA: int = 25):
        return pybaseball.statcast_pitcher_arsenal_stats(year, minPA).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_percentile_ranks(year: int):
        return pybaseball.statcast_pitcher_percentile_ranks(year).to_json(orient='records')

    @staticmethod
    def get_statcast_pitcher_spin_direction_comparison(year: int, pitch_a: str = "4-Seamer", pitch_b: str = "Changeup",
                                                       minP: int = 100, pitcher_pov: bool = None):
        return pybaseball.statcast_pitcher_spin_dir_comp(year, pitch_a, pitch_b, minP,
                                                         pitcher_pov).to_json(orient='records')

    @staticmethod
    def get_statcast_sprint_speed(year: int, min_opp: int = 10):
        return pybaseball.statcast_sprint_speed(year, min_opp).to_json(orient='records')

    @staticmethod
    def get_statcast_running_splits(year: int, min_opp: int = 5, raw_splits: bool = True):
        return pybaseball.statcast_running_splits(year, min_opp, raw_splits).to_json(orient='records')

    @staticmethod
    def get_statcast_single_game(game_pk: int):
        return pybaseball.statcast_single_game(game_pk).to_json(orient='records')

    # ind: default is returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_batting(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_batting(start_season, end_season, league, ind).to_json(orient='records')

    # ind: default is returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_fielding(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_fielding(start_season, end_season, league, ind).to_json(orient='records')

    # returns a mapping (empty) dataframe
    @staticmethod
    def get_team_ids(season: int = None, league: str = None):
        return pybaseball.team_ids(season, league).to_json(orient='records')

    # ind: defaults to returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_pitching(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_pitching(start_season, end_season, league, ind).to_json(orient='records')
