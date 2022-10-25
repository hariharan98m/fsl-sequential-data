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


# In[104]:


def preprocess_raw_data_to_create_prompts(file_name:str):
    prompt = []
    separator = '=>'
    df = pd.read_csv(file_name)
    df['narration_id_int'] = df.apply(lambda row: columnStringToInt(row), axis=1)
    participants_ids = df['participant_id'].unique()
    for participant_id in participants_ids:
        filtered_df_by_participant_id = df[df['participant_id'] == participant_id] 
        video_ids = filtered_df_by_participant_id['video_id'].unique()
        start_index = video_ids[0].index('_') + 1
        video_ids_modified = [int(video_ids[i][start_index:len(video_ids[i])]) for i in range(len(video_ids))]
        video_ids_modified = np.sort(video_ids_modified)
        for video_id_int in video_ids_modified:
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


# In[105]:


prompts = preprocess_raw_data_to_create_prompts(file_name)


# In[106]:


prompts[1]


# In[92]:


prompts[2]


# In[93]:


prompts[3]


# In[94]:


print(len(prompts))


# In[107]:


train_file_name = 'train_data.csv'
train_prompts = preprocess_raw_data_to_create_prompts(train_file_name)
with open('train_prompt.txt', 'w') as f:
    for prompt in train_prompts:
        f.write(f"{prompt}\n")


# In[108]:


validation_file_name = 'validation_data.csv'
validation_prompts = preprocess_raw_data_to_create_prompts(validation_file_name)
with open('validation_prompt.txt', 'w') as f:
    for prompt in validation_prompts:
        f.write(f"{prompt}\n")


# In[111]:


test_file_name = 'test_data.csv'
test_prompts = preprocess_raw_data_to_create_prompts(test_file_name)
with open('test_prompt.txt', 'w') as f:
    for prompt in test_prompts:
        f.write(f"{prompt}\n")


# In[ ]:




