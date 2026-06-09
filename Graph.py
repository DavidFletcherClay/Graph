#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
#sns.set_theme()
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\User\OneDrive\Desktop\testing.xlsx')
# In[ ]:


df

import ipywidgets as widgets
from IPython.display import display

def plot_line(column):
    plt.plot(df['Month'], df[column])
    #plt.plot(df.index, df[column])
    plt.show()

dropdown = widgets.Dropdown(
    options=['Act', 'Bud', 'PY'],
    value='Act',
    description='Select:'
)

widgets.interact(plot_line, column=dropdown)
# In[ ]:





# In[ ]:




