#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np


# In[3]:


file_name = 'train_data.csv'
df = pd.read_csv('train_data.csv')


# In[57]:


def columnStringToInt(row):
    strat_index = row['narration_id'].rindex('_') + 1
    return int(row['narration_id'][strat_index:len(row['narration_id'])])


# In[58]:


df['narration_id_int'] = df.apply(lambda row: columnStringToInt(row), axis=1)


# In[59]:


participants_ids = df['participant_id'].unique()
print(participants_ids)


# In[60]:


participant_id = 'P01'
filtered_df_by_participant_id = df[df['participant_id'] == participant_id] 


# In[61]:


video_ids = filtered_df_by_participant_id['video_id'].unique()
print(video_ids)


# In[62]:


start_index = video_ids[1].index('_') + 1
video_ids_modified = [int(video_ids[i][start_index:len(video_ids[i])]) for i in range(len(video_ids))]
video_ids_modified = np.sort(video_ids_modified)
print(video_ids_modified)


# In[67]:


prompt = []
separator = ' '
for video_id_int in video_ids_modified:
    video_id_str = ''
    if video_id_int <= 9:
        video_id_str = '0' + str(video_id_int)
    else:
        video_id_str = str(video_id_int)
    video_id_str = participant_id + "_" + video_id_str
    filtered_df_by_video_id = df[df['video_id'] == video_id_str] 
    sorted_df_by_narration_id = filtered_df_by_video_id.sort_values(by=['narration_id_int'])
    prompt_str = separator.join(sorted_df_by_narration_id['narration'])
    prompt.append(prompt_str)
    print(prompt_str)


# In[86]:


def preprocess_raw_data_to_create_prompts(file_name:str):
    prompt = []
    separator = ' '
    df = pd.read_csv(file_name)
    df['narration_id_int'] = df.apply(lambda row: columnStringToInt(row), axis=1)
    participants_ids = df['participant_id'].unique()
#     print(participants_ids)
    for participant_id in participants_ids:
#         print(participant_id)
        filtered_df_by_participant_id = df[df['participant_id'] == participant_id] 
        video_ids = filtered_df_by_participant_id['video_id'].unique()
        start_index = video_ids[1].index('_') + 1
        video_ids_modified = [int(video_ids[i][start_index:len(video_ids[i])]) for i in range(len(video_ids))]
        video_ids_modified = np.sort(video_ids_modified)
        for video_id_int in video_ids_modified:
#             print(video_id_int)
            video_id_str = ''
            if video_id_int <= 9:
                video_id_str = '0' + str(video_id_int)
            else:
                video_id_str = str(video_id_int)
            video_id_str = participant_id + "_" + video_id_str
            filtered_df_by_video_id = filtered_df_by_participant_id[filtered_df_by_participant_id['video_id'] == video_id_str] 
            sorted_df_by_narration_id = filtered_df_by_video_id.sort_values(by=['narration_id_int'])
            prompt_str = separator.join(sorted_df_by_narration_id['narration'])
            prompt.append(prompt_str)
        
    return prompt


# In[87]:


prompt = preprocess_raw_data_to_create_prompts(file_name)


# In[88]:


prompt[1]


# In[77]:


prompt[2]


# In[78]:


prompt[3]


# In[89]:


print(len(prompt))


# In[ ]:




