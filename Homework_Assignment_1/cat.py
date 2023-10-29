#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Cat:
    def __init__(self,name,intro_order):
        self.name=name
        self.intro_order=intro_order
        
    def introduce(self):
        if (self.intro_order<=2 and self.intro_order>0):
            if self.intro_order==1:
                print('Hello I am {}!. Nice to meet you.'.format(self.name))
            else:
                print('Hello I am {}! I see you are also a cool fluffy kitty Snowball IX, let’s together purr at the human, so that they shall give us food.'.format(self.name))
                print("Sure, let's go {}.".format(self.name))
        else:
            print('Provide the right introducing order and try again')

