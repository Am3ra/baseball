#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pybaseball as pyball
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


from pybaseball.retrosheet import *
# events(2018, type='regular', export_dir='.')


# In[12]:


example = season_game_logs(2019)[['date','home_team','home_team_game_num','visiting_team','visiting_team_game_num']]
example.columns.tolist()
# example.head()


# In[13]:


example.head()


# In[5]:


pd.concat([example[example['home_team'] == 'OAK'],example[example['visiting_team'] == 'OAK']] ).sort_values('date').reset_index().head()


# In[6]:


from pybaseball import schedule_and_record
schedule_and_record(2019, "OAK")[:50]


# In[41]:


teams = np.unique(season_game_logs(2019)[['home_team']])
results = np.array((schedule_and_record(2019, "OAK").shape))
print(teams)
# teams = schedule_and_record(2019,ANA)
err = []
for team in teams:
    print(team)
    try:
        np.append(results,schedule_and_record(2019, team))
    except:
        print(team,"didn't work")
        err=np.append(err,team)


# In[43]:


results


# There are only 19 teams in this array, there should be 30

# In[69]:


from pybaseball import statcast

# get all statcast data for July 4th, 2017
data = statcast('2017-07-04')

#get data for the first seven days of August in 2016
data = statcast('2016-08-01', '2016-08-07')


# In[70]:


data.columns.tolist()


# In[71]:


data = data[data['launch_angle'].notna()]
data = data[data['launch_speed'].notna()]


# In[76]:


data[['launch_angle','launch_speed','hit_distance_sc']]


# In[81]:


plt.scatter(data['launch_angle'],data['launch_speed'],c=data['hit_distance_sc'])
plt.xlabel("Launch angle")
plt.ylabel("Exit Velocity")
plt.xlim([-50,75])
plt.ylim([40,120])


# In[75]:


data[data['events']=='home_run']


# In[ ]:




