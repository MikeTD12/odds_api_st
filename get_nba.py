import pandas as pd
import numpy as np
import requests
from config import *
from api_key import api_key

sport = 'basketball_nba'
mkt = 'spreads'

r = requests.get(
f'{host}/v3/odds/?apiKey={api_key}&sport=basketball_nba&region={region}&dateFormat={date_format}&oddsFormat={odds_format}&mkt={mkt}',
    verify=False)

bb = pd.read_json(r.text)
bb = pd.json_normalize(bb.data)

bb = pd.merge(bb, pd.DataFrame(bb.teams.tolist(), index= bb.index), left_index=True, right_index=True)\
.rename(columns={0: 'team1', 1: 'team2'}).copy()

bb['away_team'] = np.where(bb.team1!=bb.home_team, bb.team1, bb.team2)
bb = bb.loc[bb.sites_count>0].reset_index(drop=True)

odds = []
for i in range(len(bb.sites)):
    m = pd.DataFrame(bb.sites[i][0].items()).T.rename(columns={0:'site_key',1:'site_nice',2:'last_update',3:'odds'}).iloc[1:]
    odds.append(m)
odds = pd.concat(odds)
odds.reset_index(drop=True, inplace=True)

spread = odds.odds.apply(pd.Series)
odds = pd.merge(odds, spread, left_index=True, right_index=True).drop('odds',axis=1)
bb = pd.merge(bb, odds, left_index=True, right_index=True)
bb = pd.merge(bb, bb.spreads.apply(pd.Series), left_index=True, right_index=True)
bb = pd.merge(bb, bb.points.apply(pd.Series), left_index=True, right_index=True)\
.rename(columns={0:'team1_spread',1:'team2_spread'})
bb['awayteam_spread'] = np.where(bb.team1!=bb.home_team, bb.team1_spread, bb.team2_spread)
bb['hometeam_spread'] = np.where(bb.team1==bb.home_team, bb.team1_spread, bb.team2_spread)

bb = bb.drop(['id','sport_key','sport_nice','teams','team1','team2',
              'sites','sites_count','site_key','team1_spread',
              'site_nice','team2_spread','spreads','odds','points'],axis=1)
nba = bb.set_index('commence_time').copy()