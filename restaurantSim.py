""" 
Fast Food Sim!
Variables:
- Customer impatience
- Time it takes to process order
Scenario:
  This simulates a fast food restaurant's normal day. This restaurant can take 1-6 sim minutes
  to finish a meal. Sim minuites represent minuites in the simulation. But, the customer 
  has an impatience level that ranges from 3-6 which represents the amount of
  time they're willing to wait. If the impatience level is less than or equal to the wait
  then the customer leaves.
"""
import random as rm
import simpy as simp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def cooking(env):
    #Happy is the amount of people happy with their purchase 
    #Left is the amount of people unhappy
    happy=0
    left=0
    while True:
        print('Start cooking at %d' % env.now)
        #The wait changes every order
        cooking_time = rm.randint(1,6)
        yield env.timeout(cooking_time)
        #Every customer has a different patience level
        impatience_Lvl=rm.randint(3,6)
        if cooking_time>=impatience_Lvl:
            print('Customer left at %d' % env.now)
            left+=1
            print('There are',left,'unhappy customers')
        else:
            print('Finished cooking at %d' % env.now)
            happy+=1
            print('There are',happy,'happy customers')
env = simp.Environment()
env.process(cooking(env))
#This sim will run for 35 sim minuites
env.run(until=35)
