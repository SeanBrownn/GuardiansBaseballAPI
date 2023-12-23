import datetime
from typing import Union

import uvicorn
from fastapi import FastAPI

from team import Team

app = FastAPI()




#Team methods

@app.get("/team_batting", tags=["team"])
def read_team_batting(start_season, end_season, league, ind):
    return Team.get_team_batting(start_season, end_season, league, ind)

@app.get("/team_batting_bref", tags=["team"])
def read_team_batting_bref(team, start_season, end_season):
    return Team.get_team_batting_bref(team, start_season, end_season)

@app.get("/team_fielding", tags=["team"])
def read_team_fielding(start_season, end_season, league, ind):
    return Team.get_team_fielding(start_season, end_season, league, ind)

@app.get("/team_fielding_bref", tags=["team"])
def read_team_fielding_bref(team, start_season, end_season):
    return Team.get_team_fielding_bref(team, start_season, end_season)

@app.get("/team_game_logs", tags=["team"])
def read_team_game_logs(team, season, log_type):
    return Team.get_team_game_logs(team, season, log_type)

@app.get("/team_pitching", tags=["team"])
def read_team_pitching(start_season, end_season, league, ind):
    return Team.get_team_pitching(start_season, end_season, league, ind)

@app.get("/team_pitching_bref", tags=["team"])
def read_team_pitching_bref(team, start_season, end_season):
    return Team.get_team_pitching_bref(team, start_season, end_season)

@app.get("/team_ids", tags=["team"])
def read_team_ids(season, league):
    return Team.get_team_ids(season, league)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)