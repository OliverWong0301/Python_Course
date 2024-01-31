# Return will end up the function
# Flip the coins exercise

from random import random

def flip_coin():
    # 1: Generate a random number 0 - 1
    nums = random()
    if nums > 0.5:
        return "Head"
    else:
        return "Tail"

# function will be override and execute the latest one
def flip_coin():
    if random() > 0.5:
        return "HeAd"
    else:
        return "TaIl"
    
print(flip_coin())