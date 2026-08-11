#!/usr/bin/env python
# coding: utf-8

# <h1></h1>AICW PROGRAM

# #Python basics

# In[1]:


print("hello AI")


# In[2]:


# Create a variable 'name' and assign your name
name='harshz'
print("harhz")


# In[3]:


name='harshz'


# In[5]:


print('harshz')


# In[7]:


type('harshz')


# In[9]:


age=20
print("20")


# In[10]:


age=20
print(age)


# In[11]:


age=20
print(age)
print(type(age))


# In[12]:


lst=['AICW','MYS','GSSSIETW',12,20.5]


# In[13]:


type(lst)


# In[14]:


dir(lst)


# In[15]:


lst.append('KRS')


# In[16]:


lst


# In[18]:


lst1=lst.copy()
lst1


# In[19]:


lst.count(12)


# In[38]:


lst2 = ['mango','kiwi']
lst1.extend(lst2)
print(lst1)


# In[24]:


lst1


# In[25]:


lst1.insert(2,2004)


# In[26]:


lst1


# In[29]:


lst1.remove(12)
lst1


# In[30]:


lst.pop(-2)


# In[31]:


lst1.pop(-2)


# In[32]:


lst1.reverse()
lst1


# In[33]:


lst.reverse()
lst


# In[34]:


x="krs"
x[::-1]


# In[39]:


lst1


# In[40]:


lst2


# In[41]:


lst


# In[43]:


lst.remove('kiwi')
print(lst)


# In[44]:


tup=('edunet foundation',2004)
tup


# In[45]:


dir(tup)


# In[46]:


tup.count(2004)


# In[48]:


tup.index(2004)


# In[49]:


s1={'name','age'}


# In[50]:


type(s1)


# In[51]:


s1


# In[52]:


s2 = {12,1,10,14,17,10}


# In[53]:


s2


# In[54]:


dir(s1)


# In[55]:


s1
s2


# In[56]:


print(s1)
print(s2)


# In[57]:


s1.union(s2)


# In[58]:


s1.intersection(s2)


# In[59]:


s3={17,'mango',10}
s2.intersection(s3)


# In[60]:


s2


# In[61]:


s2.intersection(s3)


# In[62]:


s1.intersection(s3)


# In[63]:


s1


# In[64]:


s2


# In[65]:


s3


# In[66]:


s4={10,14,'mango'}


# In[67]:


s4


# In[68]:


s2.intersection(s4)


# In[69]:


# dic -{}-keys and values pairs -keys unique
dc={'Name':'Harshz','Age':20,'place':'mys'}
dc


# In[74]:


dc={'Name':'Harshz','Age':20,'place':'mys'}
dc


# In[71]:


dir(dc)


# In[72]:


dc.keys()


# In[73]:


dc.values()


# In[77]:


for i in range(10):
    print(i)


# In[78]:


for rms in range(10):
    print(rms)


# In[79]:


for i in range(0,11,1):
    print(i)


# In[81]:


for i in range(0,11,2):
    print(i)


# In[83]:


for i in range(1,11,2):
    print(i)


# In[86]:


def add(x,y):
    return x+y
add(3,2)


# ##OOPs

# In[88]:


class stu:
    pass


# In[89]:


i=stu()


# In[90]:


i


# In[2]:


class student:
    def __init__(self, name, place):
        self.name=name
        self.place=place
        
    def show(self):
        return f'The name is {self.name} and you are from {self.place}.'
p1 = student('AB','MYS')
print(p1.show())


# In[102]:


class student:
    def __init__(self, usn, name):
        std.usn=usn
        std.name=name
    def show(std):
        print(f'USN of {std.usn} having the name {std.name}.')
    def update(std):
              std.usn=usn


# In[103]:


class student:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        
    def show(self):
        return f'The name is {self.name} and you are from {self.place}.'

p1 = student('AB', 'MYS')
print(p1.show())


# In[ ]:




