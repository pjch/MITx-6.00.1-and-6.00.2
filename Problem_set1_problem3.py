
# coding: utf-8

# In[14]:

s = 'ezhlqbkm'

order = ''
longest_order = ''
for i in range(len(s)):
    if i > 0 and (s[i] >= s[i-1]):
        order += s[i]
        if i == len(s)-1 and len(order) > len(longest_order):
            longest_order = order
    else:
        if len(order) > len(longest_order):
            longest_order = order
        order = s[i] 

print('Longest substring in alphabetical order is: ' + longest_order)


# In[ ]:




# In[4]:




# In[ ]:



