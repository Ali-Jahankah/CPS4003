import random as rnd # OR from random import randrange
from random import randrange as rand_range
import os
rand_num=rnd.random()
print(rand_num)

random_range = rand_range(6,100,1)
print(random_range)

# Learn how to use file system in Python
path= os.getcwd()
print(f"""
      CWD==> {path}
      """)

for file in os.listdir(path):
    print(file)