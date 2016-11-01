
# coding: utf-8

# ### Analysis 4

# In[41]:

import os
import json
from bs4 import BeautifulSoup
import operator


# In[4]:

import argparse
title_score = {}

parser = argparse.ArgumentParser(description='Process some characters.')
parser.add_argument("tag",help="ENTER THE KEYWORD: ")
args = parser.parse_args()
#fromdate = '2016-10-29'
#todate = '2016-10-30'
tag = args.tag


# In[44]:

ans_data = {}
lenBdy=0
i=0
avgLenBdy=0
html_tag = ''
hasCode=0
noCode=0
percent=0
avgLengthTag = {}
percentCode={}

mysearch = tag.split(";")
for term in mysearch :
    file_name = "answers_"+term+".json"
    json_files = [f_json for f_json in os.listdir(".") if f_json == file_name]
    if json_files:
        with open(json_files[0],'r') as data_file:
            file_ans = json.load(data_file)
            data_file.close()
            for ids in file_ans :
                bdy = file_ans[ids]['body']
                lenBdy += len(bdy)
                i = i + 1
                avgLenBdy = (lenBdy/i)
                soup = BeautifulSoup(bdy, 'html.parser')
                html_tag = soup.findAll('code')
                if (html_tag != None) :
                    hasCode = hasCode + 1
                else :
                    noCode = noCode + 1
                percent = (hasCode/(hasCode+noCode))*100
                avgLengthTag[term] =  avgLenBdy
                percentCode[term] = percent


# In[45]:

print("The avg length of the answer body per tag is :")
print(avgLengthTag)
print("The percentage of code in the answers per tag is :")
print(percentCode)
print("")
print("")
print("")


# ### Analysis 5

# In[72]:

loc = ''
locationDic = {}
tag = 'python;pandas'
mysearch = tag.split(";")
for term in mysearch :
    file_name = "user_"+term+".json"
    json_files = [f_json for f_json in os.listdir(".") if f_json == file_name]
    if json_files:
        with open(json_files[0],'r') as data_file:
            file_usr = json.load(data_file)
            data_file.close()
            for ids in file_usr :
                if 'location' in file_usr[ids].keys() :
                    loc = file_usr[ids]["location"]
                    if(loc in locationDic) :
                        locationDic[loc] = locationDic[loc] + 1
                    else :
                        locationDic[loc] = 1
                    


# In[75]:

print ("For a given tag, the most popular location is :")
sorted_loc = sorted(locationDic.items(), key=operator.itemgetter(1),reverse=True)
i = 0
for (key, val) in sorted_loc :
    if(i < 1) :
        print(key," : ",val)
        i = i+1
print("")
print("")
print("")

