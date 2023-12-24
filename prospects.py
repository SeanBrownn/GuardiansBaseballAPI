import datetime

import pybaseball

class prospects:

    current_year = datetime.datetime.now().year

    @staticmethod
    def amateur_draft(draft_round: int, year: int = current_year, keep_stats: bool = True):
        return pybaseball.amateur_draft(year, draft_round, keep_stats)

    @staticmethod
    def amateur_draft_by_team(team: str, year: int = current_year, keep_stats: bool = True):
        return pybaseball.amateur_draft_by_team(team, year, keep_stats)

    @staticmethod
    def top_prospects(team, player_type):
        return pybaseball.top_prospects(team, player_type)