import datetime

import pybaseball


class teams:

    current_year=datetime.datetime.now().year

    # ind: default is returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_batting(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_batting(start_season, end_season, league, ind).to_json(orient='records')

    @staticmethod
    def get_team_batting_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_batting_bref(team, start_season, end_season).to_json(orient='records')

    # ind: default is returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_fielding(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_fielding(start_season, end_season, league, ind).to_json(orient='records')

    # The column names from the dataframe outputted by pybaseball.team_fielding_bref were not unique. So, I had to use
    # orient='values.'
    @staticmethod
    def get_team_fielding_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_fielding_bref(team, start_season, end_season).to_json(orient='values')

    # log_type: default is getting batting logs
    @staticmethod
    def get_team_game_logs(team: str, season: int = current_year, log_type: str = "batting"):
        return pybaseball.team_game_logs(season, team, log_type).to_json(orient='records')

    # ind: defaults to returning one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_pitching(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_pitching(start_season, end_season, league, ind).to_json(orient='records')

    @staticmethod
    def get_team_pitching_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_pitching_bref(team, start_season, end_season).to_json(orient='records')

    # returns a mapping (empty) dataframe
    @staticmethod
    def get_team_ids(season: int = None, league: str = None):
        return pybaseball.team_ids(season, league).to_json(orient='records')