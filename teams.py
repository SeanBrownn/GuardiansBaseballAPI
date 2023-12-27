import datetime

import pybaseball


class teams:
    current_year = datetime.datetime.now().year

    @staticmethod
    def get_amateur_draft_by_team(team: str, year: int = current_year, keep_stats: bool = True):
        return pybaseball.amateur_draft_by_team(team, year, keep_stats).to_json(orient='records')

    @staticmethod
    def get_schedule_and_record(season: int, team: str):
        return pybaseball.schedule_and_record(season, team).to_json(orient='records')

    @staticmethod
    def get_team_batting_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_batting_bref(team, start_season, end_season).to_json(orient='records')

    # The column names from the dataframe outputted by pybaseball.team_fielding_bref were not unique. So, I had to use
    # orient='values.'
    @staticmethod
    def get_team_fielding_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_fielding_bref(team, start_season, end_season).to_json(orient='values')

    # log_type: default is getting batting logs
    @staticmethod
    def get_team_game_logs(team: str, season: int = current_year, log_type: str = "batting"):
        return pybaseball.team_game_logs(season, team, log_type).to_json(orient='records')

    @staticmethod
    def get_team_pitching_bref(team: str, start_season: int = current_year, end_season: int = None):
        return pybaseball.team_pitching_bref(team, start_season, end_season).to_json(orient='records')

    @staticmethod
    def get_top_prospects(team: str, player_type: str):
        return pybaseball.top_prospects(team, player_type).to_json(orient='records')
