import datetime
from typing import Union

import pybaseball


class mlb:

    current_year = datetime.datetime.now().year

    @staticmethod
    def get_standings(season: int = current_year):
        json_string = [df.to_json(orient='records') for df in pybaseball.standings(season)]
        return json_string

    # for start_dt and end_dt, format = 'YYYY-MM-DD'
    # to get data for only 1 date, enter a start date but not an end date
    @staticmethod
    def get_statcast(start_dt: str = None, end_dt: str = None, team: str = None, verbose: bool = True, parallel: bool = True):
        return pybaseball.statcast(start_dt, end_dt, team, verbose, parallel).to_json(orient='records')

    # can enter position by number or name
    @staticmethod
    def get_statcast_outs_above_average(year: int, pos: Union[int, str], min_att: Union[int, str] = "q", view: str = "Fielder"):
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