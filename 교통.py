#!/usr/bin/env python
# coding: utf-8

# # 좌표로 행정동 가져오기

# ## 버스 정류장

# In[1]:


import pandas as pd
import numpy as np
import requests


# In[2]:


bus_stop = pd.read_csv('서울시버스정류소좌표데이터(2022.08.24).csv', encoding='CP949')
bus_stop.head()


# In[3]:


def juso(x) :
    method = "GET"
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json"
    params = {'x' : x['좌표X'], 'y' : x['좌표Y']}
    header = {'authorization': 'KakaoAK apikey', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    
    try :
        response = requests.request(method=method, url=url, headers=header, params=params )
        tokens = response.json()
        x['시도'] = tokens['documents'][1]['region_1depth_name']
        x['시군구'] = tokens['documents'][1]['region_2depth_name']
        x['동'] = tokens['documents'][1]['region_3depth_name']
    except :
        x['시도'] = ''
        x['시군구'] = ''
        x['동'] = ''
    return x


# In[4]:


bus_stop = bus_stop.apply(juso, axis =1)


# In[5]:


bus_stop.head()


# In[6]:


bus_stop.to_csv('버스 정류장 주소.csv', index=False, encoding='CP949')


# ## 지하철역

# In[7]:


subway = pd.read_csv('station_coordinate.csv', names = ['호선', '역 이름', 'ID', '좌표Y', '좌표X'], skiprows=1)
subway.head()


# In[8]:


subway = subway.apply(juso, axis =1)


# In[9]:


subway.head()


# In[11]:


subway.to_csv('지하철역 주소.csv', index=False, encoding='CP949')


# In[ ]:




