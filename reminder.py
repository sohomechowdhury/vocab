#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from plyer import notification
import time
if __name__ =="__main__":
    while True:
        title="Learn"
        with open("term.txt") as vc:
            lines= vc.readlines()
            for vocab in lines:
                notification.notify(title=title,message=vocab.strip(),timeout=10)
        time.sleep(12)
       

