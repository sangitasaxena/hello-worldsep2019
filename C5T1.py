#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy


# In[3]:


import math


# In[4]:


import scipy.stats


# In[5]:


from numpy import random
import numpy as np


# In[6]:


# uniform random numbers in [0,1]
dataOne = random.rand(5,5)
print (dataOne)


# In[7]:


np.mean(dataOne)


# In[8]:


np.round(dataOne)


# In[9]:


np.rint(dataOne)


# In[10]:


np.fix(dataOne)


# In[11]:


np.floor(dataOne)


# In[12]:


np.ceil(dataOne)


# In[13]:


np.trunc(dataOne)


# In[14]:


np.amin(dataOne,0)


# In[15]:


np.amin(dataOne,1)


# In[16]:


np.var(dataOne)


# In[17]:


np.std(dataOne)


# In[18]:


varOne = 25
varTwo = 25.0
varThree = varOne + varTwo
print(varThree)


# In[22]:


varOne = 25
VarTwo = 'Hello'
varThree = varOne + varTwo
print(varThree)


# In[7]:


a_dict = {x: x**3 for x in (3, 6, 9, 12, 15)}
print(a_dict)
var1 = a_dict[3]
print(var1)
var2 = a_dict[6]
print(var2)
var3 = a_dict[15]
print(var3)
varadd = print(var1+var2+var3)
varsubadd = print(var1 - a_dict[9] + a_dict[12])
vardiv = print(var2/var1)


# import pandas as pd
# xls = pd.ExcelFile("D:/UnivofTexas/C5/T1/sample_file.xls")
# file_sample_data = xls.parse('sample_file.xls', index_col = None, na_values = ['NA'])
# print(file_sample_data)

# In[ ]:


---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-12-72990b64b2de> in <module>
      1 import pandas as pd
----> 2 xls = pd.ExcelFile("D:/UnivofTexas/C5/T1/sample_file.xls")
      3 file_sample_data = xls.parse('sample_file.xls', index_col = None, na_values = ['NA'])
      4 print(file_sample_data)

~\Anaconda3\lib\site-packages\pandas\io\excel.py in __init__(self, io, engine)
    651         self._io = _stringify_path(io)
    652 
--> 653         self._reader = self._engines[engine](self._io)
    654 
    655     def __fspath__(self):

~\Anaconda3\lib\site-packages\pandas\io\excel.py in __init__(self, filepath_or_buffer)
    422             self.book = xlrd.open_workbook(file_contents=data)
    423         elif isinstance(filepath_or_buffer, compat.string_types):
--> 424             self.book = xlrd.open_workbook(filepath_or_buffer)
    425         else:
    426             raise ValueError('Must explicitly set engine if not passing in'

~\Anaconda3\lib\site-packages\xlrd\__init__.py in open_workbook(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows)
    109     else:
    110         filename = os.path.expanduser(filename)
--> 111         with open(filename, "rb") as f:
    112             peek = f.read(peeksz)
    113     if peek == b"PK\x03\x04": # a ZIP file

FileNotFoundError: [Errno 2] No such file or directory: 'D:/UnivofTexas/C5/T1/sample_file.xls'


# In[ ]:


# It was easy to install python and libraries
# The tutorial was quite useful
# Python is similar to R but much more robust and easier to use

