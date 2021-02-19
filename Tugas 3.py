#!/usr/bin/env python
# coding: utf-8

# In[22]:


kkm = float(70)


# In[32]:


praktek = float(input("nilai praktek:"))


# In[29]:


teori = float(input("nilai teori:"))


# In[30]:


if praktek >= 70 and teori >= 70:
    print("Selamat, anda lulus.")
elif teori <= 70 and praktek >= 70:
    print("Anda harus mengulangi ujian teori.")
else:
    print("Anda harus mengulangi ujian teori dan praktek.")

