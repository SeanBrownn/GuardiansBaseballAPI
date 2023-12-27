import datetime
from typing import Annotated
from typing import Union

import uvicorn
from fastapi import FastAPI, Query

from mlb import mlb
from players import players
from teams import teams

app = FastAPI()

current_year = datetime.datetime.now().year


# Teams functions
@app.get("/amateur_draft_by_team", tags=["teams"])
def read_amateur_draft_by_team(team: str, year: int = current_year, keep_stats: bool = True):
    return teams.get_amateur_draft_by_team(team, year, keep_stats)


@app.get("/team_batting_bref", tags=["teams"])
def read_team_batting_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_batting_bref(team, start_season, end_season)


@app.get("/team_fielding_bref", tags=["teams"])
def read_team_fielding_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_fielding_bref(team, start_season, end_season)


@app.get("/team_game_logs", tags=["teams"])
def read_team_game_logs(team: str, season: int = current_year, log_type: str = "batting"):
    return teams.get_team_game_logs(team, season, log_type)


@app.get("/team_pitching_bref", tags=["teams"])
def read_team_pitching_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_pitching_bref(team, start_season, end_season)


@app.get("/schedule_and_record", tags=["teams"])
def read_schedule_and_record(season: int, team: str):
    return teams.get_schedule_and_record(season, team)


@app.get("/top_prospects", tags=["teams"])
def read_top_prospects(team: str = None, player_type: str = None):
    return teams.get_top_prospects(team, player_type)


# Players functions
@app.get("/player_id_lookup", tags=["players"])
def read_player_id_lookup(last: str, first: str = None, fuzzy: bool = False):
    return players.get_player_id_lookup(last, first, fuzzy)


@app.get("/player_id_reverse_lookup", tags=["players"])
def read_player_id_reverse_lookup(player_ids: Annotated[list[int], Query()], key_type: str = 'mlbam'):
    return players.get_player_id_reverse_lookup(player_ids, key_type)


@app.get("/splits", tags=["players"])
def read_splits(playerid: str, year: int = None, player_info: bool = None, pitching_splits: bool = None):
    return players.get_splits(playerid, year, player_info, pitching_splits)


@app.get("/statcast_batter", tags=["players"])
def read_statcast_batter(player_id: int, start_dt: str = None, end_dt: str = None):
    return players.get_statcast_batter(player_id, start_dt, end_dt)


@app.get("/statcast_pitcher", tags=["players"])
def read_statcast_pitcher(start_dt: str, end_dt: str, player_id: int):
    return players.get_statcast_pitcher(start_dt, end_dt, player_id)


# MLB functions
@app.get("/amateur_draft", tags=["mlb"])
def read_amateur_draft(draft_round: int, year: int = current_year, keep_stats: bool = True):
    return mlb.get_amateur_draft(draft_round, year, keep_stats)


@app.get("/batting_stats_bref", tags=["mlb"])
def read_batting_stats_bref(season: int = current_year):
    return mlb.get_batting_stats_bref(season)


@app.get("/batting_stats_range", tags=["mlb"])
def read_batting_stats_range(start_dt: str, end_dt: str = None):
    return mlb.get_batting_stats_range(start_dt, end_dt)


@app.get("/bwar_bat", tags=["mlb"])
def read_bwar_bat(return_all: bool = False):
    return mlb.get_bwar_bat(return_all)


@app.get("/bwar_pitch", tags=["mlb"])
def read_bwar_pitch(return_all: bool = False):
    return mlb.get_bwar_pitch(return_all)


@app.get("/chadwick_register", tags=["mlb"])
def read_chadwick_register(save: bool = False):
    return mlb.get_chadwick_register(save)


@app.get("/pitching_stats", tags=["mlb"])
def read_pitching_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None,
                        ind: int = 1):
    return mlb.get_pitching_stats(start_season, end_season, league, qual, ind)


@app.get("/pitching_stats_bref", tags=["mlb"])
def read_pitching_stats_bref(start_season: int = current_year):
    return mlb.get_pitching_stats_bref(start_season)


@app.get("/pitching_stats_range", tags=["mlb"])
def read_pitching_stats_range(start_dt: str, end_dt: str = None):
    return mlb.get_pitching_stats_range(start_dt, end_dt)


@app.get("/standings", tags=["mlb"])
def read_standings(season: int = current_year):
    return mlb.get_standings(season)


@app.get("/statcast", tags=["mlb"])
def read_statcast(start_dt: str = None, end_dt: str = None, team: str = None, verbose: bool = True,
                  parallel: bool = True):
    return mlb.get_statcast(start_dt, end_dt, team, verbose, parallel)


@app.get("/statcast_outs_above_average", tags=["mlb"])
def read_statcast_outs_above_average(year: int, pos: Union[int, str], min_att: Union[int, str] = "q",
                                     view: str = "Fielder"):
    return mlb.get_statcast_outs_above_average(year, pos, min_att, view)


@app.get("/statcast_outfield_directional_oaa", tags=["mlb"])
def read_statcast_outfield_directional_oaa(year: int, min_opp: Union[int, str] = "q"):
    return mlb.get_statcast_outfield_directional_oaa(year, min_opp)


@app.get("/statcast_outfield_catch_prob", tags=["mlb"])
def read_statcast_outfield_catch_prob(year: int, min_opp: Union[int, str] = "q"):
    return mlb.get_statcast_outfield_catch_prob(year, min_opp)


@app.get("/statcast_outfielder_jump", tags=["mlb"])
def read_statcast_outfielder_jump(year: int, min_att: Union[int, str] = "q"):
    return mlb.get_statcast_outfielder_jump(year, min_att)


@app.get("/statcast_catcher_poptime", tags=["mlb"])
def read_statcast_catcher_poptime(year: int, min_2b_att: int = 5, min_3b_att: int = 0):
    return mlb.get_statcast_catcher_poptime(year, min_2b_att, min_3b_att)


@app.get("/statcast_catcher_framing", tags=["mlb"])
def read_statcast_catcher_framing(year: int, min_called_p: Union[int, str] = "q"):
    return mlb.get_statcast_catcher_framing(year, min_called_p)


@app.get("/statcast_batter_exitvelo_barrels", tags=["mlb"])
def read_statcast_batter_exitvelo_barrels(year: int, minBBE: int = None):
    return mlb.get_statcast_batter_exitvelo_barrels(year, minBBE)


@app.get("/statcast_batter_expected_stats", tags=["mlb"])
def read_statcast_batter_expected_stats(year: int, minPA: int = None):
    return mlb.get_statcast_batter_expected_stats(year, minPA)


@app.get("/statcast_batter_percentile_ranks", tags=["mlb"])
def read_statcast_batter_percentile_ranks(year: int):
    return mlb.get_statcast_batter_percentile_ranks(year)


@app.get("/statcast_batter_pitch_arsenal", tags=["mlb"])
def read_statcast_batter_pitch_arsenal(year: int, minPA: int = 25):
    return mlb.get_statcast_batter_pitch_arsenal(year, minPA)


@app.get("/statcast_pitcher_exitvelo_barrels", tags=["mlb"])
def read_statcast_pitcher_exitvelo_barrels(year: int, minBBE: int):
    return mlb.get_statcast_pitcher_exitvelo_barrels(year, minBBE)


@app.get("/statcast_pitcher_expected_stats", tags=["mlb"])
def read_statcast_pitcher_expected_stats(year: int, minPA: int = None):
    return mlb.get_statcast_pitcher_expected_stats(year, minPA)


@app.get("/statcast_pitcher_pitch_arsenal", tags=["mlb"])
def read_statcast_pitcher_pitch_arsenal(year: int, minP: int, arsenal_type: str = "avg_speed"):
    return mlb.get_statcast_pitcher_pitch_arsenal(year, minP, arsenal_type)


@app.get("/statcast_pitcher_arsenal_stats", tags=["mlb"])
def read_statcast_pitcher_arsenal_stats(year: int, minPA: int = 25):
    return mlb.get_statcast_pitcher_arsenal_stats(year, minPA)


@app.get("/statcast_pitcher_percentile_ranks", tags=["mlb"])
def read_statcast_pitcher_percentile_ranks(year: int):
    return mlb.get_statcast_pitcher_percentile_ranks(year)


@app.get("/statcast_pitcher_spin_direction_comparison", tags=["mlb"])
def read_statcast_pitcher_spin_direction_comparison(year: int, pitch_a: str = "4-Seamer", pitch_b: str = "Changeup",
                                                    minP: int = 100, pitcher_pov: bool = None):
    return mlb.get_statcast_pitcher_spin_direction_comparison(year, pitch_a, pitch_b, minP, pitcher_pov)


@app.get("/statcast_sprint_speed", tags=["mlb"])
def read_statcast_sprint_speed(year: int, min_opp: int = 10):
    return mlb.get_statcast_sprint_speed(year, min_opp)


@app.get("/statcast_running_splits", tags=["mlb"])
def read_statcast_running_splits(year: int, min_opp: int = 5, raw_splits: bool = True):
    return mlb.get_statcast_running_splits(year, min_opp, raw_splits)


@app.get("/statcast_single_game", tags=["mlb"])
def read_statcast_single_game(game_pk: int):
    return mlb.get_statcast_single_game(game_pk)


@app.get("/team_batting", tags=["mlb"])
def read_team_batting(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return mlb.get_team_batting(start_season, end_season, league, ind)


@app.get("/team_fielding", tags=["mlb"])
def read_team_fielding(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return mlb.get_team_fielding(start_season, end_season, league, ind)


@app.get("/team_ids", tags=["mlb"])
def read_team_ids(season: int = None, league: str = None):
    return mlb.get_team_ids(season, league)


@app.get("/team_pitching", tags=["mlb"])
def read_team_pitching(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return mlb.get_team_pitching(start_season, end_season, league, ind)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
