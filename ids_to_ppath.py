#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys, pairtree;
for line in sys.stdin:
    (n,i) = line.strip().split('.',1);
    print("/".join([n, 'pairtree_root', pairtree.id2path(i), pairtree.id_encode(i)]))

