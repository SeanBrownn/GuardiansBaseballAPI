import datetime
from typing import Annotated

import pybaseball
import uvicorn
from fastapi import FastAPI, Query

from prospects import prospects
from teams import teams
from players import players

app = FastAPI()

current_year=datetime.datetime.now().year


# Teams methods
@app.get("/team_batting", tags=["team"])
def read_team_batting(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return teams.get_team_batting(start_season, end_season, league, ind)

@app.get("/team_batting_bref", tags=["team"])
def read_team_batting_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_batting_bref(team, start_season, end_season)

@app.get("/team_fielding", tags=["team"])
def read_team_fielding(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return teams.get_team_fielding(start_season, end_season, league, ind)

@app.get("/team_fielding_bref", tags=["team"])
def read_team_fielding_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_fielding_bref(team, start_season, end_season)

@app.get("/team_game_logs", tags=["team"])
def read_team_game_logs(team: str, season: int = current_year, log_type: str = "batting"):
    return teams.get_team_game_logs(team, season, log_type)

@app.get("/team_pitching", tags=["team"])
def read_team_pitching(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
    return teams.get_team_pitching(start_season, end_season, league, ind)

@app.get("/team_pitching_bref", tags=["team"])
def read_team_pitching_bref(team: str, start_season: int = current_year, end_season: int = None):
    return teams.get_team_pitching_bref(team, start_season, end_season)

@app.get("/team_ids", tags=["team"])
def read_team_ids(season: int = None, league: str = None):
    return teams.get_team_ids(season, league)

# Players methods
#@app.get("/batting_stats", tags=["players"])
#def read_batting_stats(start_season: int = current_year, end_season: int = None, league: str = 'ALL',
   #                      stat_columns = 'ALL', qual: int = None, split_seasons: bool = False, month: str = 'ALL',
  #                       on_active_roster: bool = False, minimum_age: int = 0, maximum_age: int = 100,
 #                        team: str = None, position: str = 'ALL', max_results: int = 1000000):
#    return players.get_batting_stats(start_season, end_season, league, stat_columns, qual, split_seasons, month,
    #                                   on_active_roster, minimum_age, maximum_age, team, position,
     #                                  max_results)

@app.get("/batting_stats", tags=["players"])
def read_batting_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None,
                       split_seasons: bool = False):
    return players.get_batting_stats(start_season, end_season, league, qual, split_seasons)

@app.get("/batting_stats_bref", tags=["players"])
def read_batting_stats_bref(season: int = current_year):
    return players.get_batting_stats_bref(season)

@app.get("/batting_stats_range", tags=["players"])
def read_batting_stats_range(start_dt: str, end_dt: str = None):
    return players.get_batting_stats_range(start_dt, end_dt)

@app.get("/bwar_bat", tags=["players"])
def read_bwar_bat(return_all: bool = False):
    return players.get_bwar_bat(return_all)

@app.get("/bwar_pitch", tags=["players"])
def read_bwar_pitch(return_all: bool = False):
    return players.get_bwar_pitch(return_all)

@app.get("/chadwick_register", tags=["players"])
def read_chadwick_register(save: bool = False):
    return players.get_chadwick_register(save)

@app.get("/pitching_stats", tags=["players"])
def read_pitching_stats(start_season: int = current_year, end_season: int = None, league: str = 'all', qual: int = None, ind: int = 1):
    return players.get_pitching_stats(start_season, end_season, league, qual, ind)

# Prospects methods
@app.get("/amateur_draft", tags=["prospects"])
def read_amateur_draft(draft_round: int, year: int = current_year, keep_stats: bool = True):
    return prospects.amateur_draft(draft_round, year, keep_stats)

@app.get("/amateur_draft_by_team", tags=["prospects"])
def read_amateur_draft_by_team(team: str, year: int = current_year, keep_stats: bool = True):
    return prospects.amateur_draft_by_team(team, year, keep_stats)

@app.get("/top_prospects", tags=["prospects"])
def read_top_prospects(team: str = None, player_type: str = None):
    return prospects.top_prospects(team, player_type)

@app.get("/pitching_stats_bref", tags=["players"])
def read_pitching_stats_bref(start_season: int = current_year):
    return players.get_pitching_stats_bref(start_season)

@app.get("/pitching_stats_range", tags=["players"])
def read_pitching_stats_range(start_dt: str, end_dt: str = None):
    return players.get_pitching_stats_range(start_dt, end_dt)

@app.get("/player_id_lookup", tags=["players"])
def read_player_id_lookup(last: str, first: str = None, fuzzy: bool = False):
    return players.get_player_id_lookup(last, first, fuzzy)

@app.get("/player_id_reverse_lookup", tags=["players"])
def read_player_id_reverse_lookup(player_ids: Annotated[list[int], Query()], key_type: str = 'mlbam'):
    return players.get_player_id_reverse_lookup(player_ids, key_type)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)