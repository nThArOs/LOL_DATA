import pandas as pd
import os
from riotwatcher import LolWatcher, ApiError

from constants import api_key, region
from riotwatcher import LolWatcher, ApiError
from leadboard import *
from data_processing.db import *

if __name__ == '__main__':
    # Open_Conn()
    lol_watcher = LolWatcher(api_key)
    # df_leaderboard, list_summoner = leadboard.get_all_leaderboard_api(queue_type, region, lol_watcher)
    # insert_leaderboard(df_leaderboard)
    #leaderboard_summonerId, leaderboard_summonerName = get_db_leaderboard()
    #get_leaderboard_puuid(leaderboard_summonerName, lol_watcher)
    insert_db_puuid_csv()
    #list_puuid, list_name= get_db_puuid()
    #get_matchlist_bypuuid(list_puuid, lol_watcher)

