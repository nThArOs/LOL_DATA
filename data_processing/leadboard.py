from riotwatcher import LolWatcher, ApiError
import pandas as pd
from constants import *
from riotwatcher import LolWatcher, ApiError


def get_challenger_leaderboard(queue_type, player_region, lol_watcher):
    # GET THE DATA OF THE API TO A DATAFRAME

    # print(lol_watcher.league.challenger_by_queue(region=player_region, queue=queue_type))

    challenger_player = pd.DataFrame.from_dict(lol_watcher.league.challenger_by_queue(region=player_region,
                                                                                      queue=queue_type)['entries'])
    # Organise leadbord by LeaguePoint
    challenger_player = challenger_player[
        ['leaguePoints', 'rank', 'summonerName', 'wins', 'losses', 'hotStreak', 'veteran', 'freshBlood', 'inactive',
         'summonerId']]

    challenger_player = challenger_player.sort_values(by="leaguePoints", ascending=False)
    # Reset index to match the previous sorting
    challenger_player.reset_index(drop=True, inplace=True)
    summoner_names = challenger_player['summonerName'].tolist()

    return challenger_player, summoner_names


def get_grandmaster_leaderboard(queue_type, player_region, lol_watcher):
    # GET THE DATA OF THE API TO A DATAFRAME

    grandmaster_player = pd.DataFrame.from_dict(lol_watcher.league.grandmaster_by_queue(region=player_region,
                                                                                        queue=queue_type)['entries'])
    # Organise leadbord by LeaguePoint
    grandmaster_player = grandmaster_player[
        ['leaguePoints', 'rank', 'summonerName', 'wins', 'losses', 'hotStreak', 'veteran', 'freshBlood', 'inactive',
         'summonerId']]

    grandmaster_player = grandmaster_player.sort_values(by="leaguePoints", ascending=False)
    # Reset index to match the previous sorting
    grandmaster_player.reset_index(drop=True, inplace=True)
    summoner_names = grandmaster_player['summonerName'].tolist()

    return grandmaster_player, summoner_names


def get_master_leaderboard(queue_type, player_region, lol_watcher):
    # GET THE DATA OF THE API TO A DATAFRAME

    master_player = pd.DataFrame.from_dict(lol_watcher.league.masters_by_queue(region=player_region,
                                                                               queue=queue_type)['entries'])
    # Organise leadbord by LeaguePoint
    master_player = master_player[
        ['leaguePoints', 'rank', 'summonerName', 'wins', 'losses', 'hotStreak', 'veteran', 'freshBlood', 'inactive',
         'summonerId']]

    master_player = master_player.sort_values(by="leaguePoints", ascending=False)
    # Reset index to match the previous sorting
    master_player.reset_index(drop=True, inplace=True)

    summoner_names = master_player['summonerName'].tolist()

    return master_player, summoner_names


def get_all_leaderboard_api(queue_type, player_region, lol_wacteher):
    df_challenger, list_challenger_player = get_challenger_leaderboard(queue_type, region, lol_wacteher)
    df_grandmaster, list_grandmaster_player = get_grandmaster_leaderboard(queue_type, region, lol_wacteher)
    df_master, list_master_player = get_master_leaderboard(queue_type, region, lol_wacteher)
    list_df = [df_challenger, df_grandmaster, df_master]
    leaderboard = pd.concat(list_df)
    leaderboard_summoner = list_challenger_player + list_grandmaster_player + list_master_player

    return leaderboard, leaderboard_summoner


def get_leaderboard_puuid(leaderboard, lol_watcher):
    list_summoner_puuid = list()
    list_summoner_name = list()
    for summonerName in leaderboard:
        print(summonerName[0])
        try:
            summoner = lol_watcher.summoner.by_name(region, summonerName[0])
            list_summoner_puuid.append(summoner['puuid'])
            list_summoner_name.append(summoner['summonerId'])
        except:
            print('error')
            list_summoner_puuid.append("error")
            list_summoner_name.append("error")

    df = pd.DataFrame(data=zip(list_summoner_puuid, list_summoner_name), columns=['puuid', 'summonerId'])
    df.to_csv('summoner_puuid2.csv', index=False)

def get_matchlist_bypuuid(list_puuid, lol_watcher):
    #for puuid in list_puuid:
    print(list_puuid[0][0])
    match_list_history = lol_watcher.match.matchlist_by_puuid
    match_history = lol_watcher.match.matchlist_by_puuid(region, list_puuid[0][0])
