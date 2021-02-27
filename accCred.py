from time import sleep
from selenium import webdriver
import random


def numGen():
    n = random.randint(0, 100)
    return n * 10

def passGen():
    n = random.randint(10000000, 1000000000)
    return n

botUsername = "offworld_agent_" + str(numGen())

print(botUsername)
print(passGen())