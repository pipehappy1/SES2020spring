
# coding: utf-8

# In[3]:


def count_words(fn):
    import os.path
    if os.path.isfile(fn):
        with open(fn,'r') as fh:
            words_num=0
            for line in fh:
                words_num+=len(line.split())
            return words_num
count_words('./Desktop/unit2/readme.md ') 

