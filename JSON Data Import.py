#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd


# In[14]:


import json
with open('/home/mvisi/Project/DLP/Core/Dynamic_Pricing/Data/UserSessions.json') as f:
    data=json.load(f)

print(data)


# In[37]:


raw_list=list()
for key, value in data.items():
    raw_list.append(value)


# In[38]:


del raw_list[0]


# In[39]:


raw_list1=raw_list[0]


# In[40]:



len(raw_list1)


# In[41]:


raw_list1


# In[42]:


keyList = ['appVersion', 'applicationType', 'bounce', 'browserFamily', 'browserMajorVersion', 'browserMonitorId', 'browserMonitorName', 'browserType', 'carrier', 'city', 'clientTimeOffset', 'connectionType', 'continent', 'country', 'crashGroupId', 'dateProperties', 'device', 'displayResolution', 'doubleProperties', 'duration', 'endReason', 'endTime', 'hasCrash', 'hasError', 'hasSessionReplay', 'internalUserId', 'ip', 'isp', 'longProperties', 'manufacturer', 'matchingConversionGoals', 'matchingConversionGoalsCount', 'networkTechnology', 'newUser', 'numberOfRageClicks', 'osFamily', 'osVersion', 'reasonForNoSessionReplay', 'reasonForNoSessionReplayMobile', 'region', 'replayEnd', 'replayStart', 'rootedOrJailbroken', 'screenHeight', 'screenOrientation', 'screenWidth', 'startTime', 'stringProperties', 'totalErrorCount', 'totalLicenseCreditCount', 'userActionCount', 'userExperienceScore', 'userId', 'userSessionId', 'userType']


# In[44]:


df = pd.DataFrame(raw_list1, columns =keyList )
#print(df.head())
df.head()


# In[45]:


df.to_csv('Dynatrace_data.csv', index=False)


# In[ ]:





# In[ ]:




