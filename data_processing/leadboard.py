

def get_challenger_leadboar(queue_type, player_region):
    #GET THE DATA OF THE API TO A DATAFRAME
    chall_player = pd.DataFrame.from_dict(lol_watcher.league.challenger_by_queue(region = player_region,
                                                                                 queue = queue_type)['entries'])
    #Organise leadbord by LeaguePoint
    chall_player = chall_player[
        ['leaguePoints', 'rank', 'summonerName', 'wins', 'losses', 'hotStreak', 'veteran', 'freshBlood', 'inactive',
         'summonerId']]
    chall_player = chall_player.sort_values(by="leaguePoints", ascending = False)
    #Reset index to match the previous sorting
    chall_player.reset_index(drop=True, inplace=True)
    summoner_names = chall_player['summonerName'].tolist()
    return chall_player,