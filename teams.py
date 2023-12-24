import datetime

import pybaseball


class teams:

    current_year=datetime.datetime.now().year

    # default behaviors:
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    # league: returns data from all leagues
    # ind: returns one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_batting(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_batting(start_season, end_season, league, ind).to_dict(orient='records')

    # default behaviors:
    # team: no default behavior, team must be provided
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    @staticmethod
    def get_team_batting_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_batting_bref(team, start_season, end_season).to_dict(orient='records')

    # default behaviors:
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    # league: returns data from all leagues
    # ind: returns one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_fielding(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_fielding(start_season, end_season, league, ind).to_dict(orient='records')

    # default behaviors:
    # team: no default behavior, team must be provided
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    @staticmethod
    def get_team_fielding_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_fielding_bref(team, start_season, end_season).to_dict(orient='records')

    # default behaviors:
    # team: no default behavior, team must be provided
    # season: gets logs from current year
    # log_type: gets batting logs
    @staticmethod
    def get_team_game_logs(team: str, season: int = current_year, log_type: str = "batting"):
        return pybaseball.team_game_logs(season, team, log_type)

    # default behaviors:
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    # league: returns data from all leagues
    # ind: returns one row per team per year (doesn't aggregate)
    @staticmethod
    def get_team_pitching(start_season: int = current_year, end_season: int = None, league: str = 'all', ind: int = 1):
        return pybaseball.team_pitching(start_season, end_season, league, ind)

    # default behaviors:
    # team: no default behavior, team must be provided
    # start_season: starts from current year
    # end_season: if not provided, only returns data from start_season
    @staticmethod
    def get_team_pitching_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_pitching_bref(team, start_season, end_season)

    # default behaviors:
    # season: returns all seasons if not provided
    # league: returns data from all leagues
    @staticmethod
    def get_team_ids(season: int = None, league: str = None):
        return pybaseball.team_ids(season, league)
