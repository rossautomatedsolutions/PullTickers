#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd

#Pull tickers from wikipedia
sp_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers_list = list(sp_df['Symbol'])[:]
print(tickers_list)


# In[ ]:




