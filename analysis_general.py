
# coding: utf-8

# In[13]:

import os
import json
import operator
user_score = {}
file_data = {}
file_user = {}


# ### Analysis 1

# In[9]:

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("question.json")]

if json_files:
    with open(json_files[0],'r') as data_file:
        file_data = json.load(data_file)
        data_file.close()


# In[10]:

for ids in file_data:
    title = file_data[ids]['title']
    if 'badge_counts' in file_data[ids]['owner'].keys():
        silver = file_data[ids]['owner']['badge_counts']['silver']
        bronze = file_data[ids]['owner']['badge_counts']['bronze']
        gold = file_data[ids]['owner']['badge_counts']['gold']
        badge_wt = 3*gold + 2*silver + bronze
        user_score[title] = badge_wt
sorted_score = sorted(user_score.items(), key=operator.itemgetter(1),reverse=True)
print ("TOP 10 QUESTIONS:")
print ("")
i=0
for (key, val) in sorted_score :
    if(i < 10) :
        print(key," : ",val)
        i = i+1
print ("")
print ("")
print ("")


# ### Analysis 2

# In[11]:

dic = {}
tags = []

for ids in file_data:
    tags += file_data[ids]['tags']

for t in tags :
    if t in dic :
        dic[t] = dic[t]+1
    else :
        dic[t] = 1

print("No of questions for each tag :")
print("")
sorted_n_questions = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
i = 0
for (key, val) in sorted_n_questions :
    if i < 10 :
        print(key," : ",val)
        i = i + 1
print ("")
print ("")
print ("")   


# In[12]:

que_ans = {}
print("The questions with most answer count :-")
print("")
for ids in file_data :
    title = file_data[ids]["title"]
    ans_count = file_data[ids]["answer_count"]
    que_ans[title] = ans_count

sorted_ansQues = sorted(que_ans.items(), key=operator.itemgetter(1),reverse=True)

i=0
for (key, val) in sorted_ansQues :
    if i <10 :
        print(key," : ",val)
        i=i+1
print ("")
print ("")
print ("")
    


# ### Analysis 3

# In[14]:

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("user.json")]
if json_files:
    with open(json_files[0],'r') as data_file:
        file_user = json.load(data_file)
        data_file.close()


# In[15]:

dic_down_vote = {}
for usr_id in file_user :
    if 'down_vote_count' in file_user[usr_id].keys() :
        down_vote = file_user[usr_id]['down_vote_count']
        dic_down_vote[usr_id] = down_vote
print ("Top 10 downvoted users:")
sorted_downvote = sorted(dic_down_vote.items(), key=operator.itemgetter(1),reverse=True)
i = 0
for (key, val) in sorted_downvote :
    if(i < 10) :
        print(key," : ",val)
        i = i+1
print("")
print("")
print("")


# 

# In[ ]:




# In[ ]:



