import pandas as pd
import os
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-5a222cb1-a5dd-4b3d-99cc-4a362265648c')
my_region = "euw1"
queue_type = "RANKED_SOLO_5x5"
