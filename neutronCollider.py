"""
Neutron Collision Sim!
Variables:

-Neutron energy (how fast it's moving)
-Type of reaction

Scenario: You happen to have a bunch of free neutrons and Fissile isotopes 
(Uranium 233, 235 and Plutonium 235, 241). So, you make the neutrons and 
isotopes collide with varying results. The results are based on how fast 
the neutron goes which is measured in eV (electron volts). You run this 
5 times. Make sure you do this very quickly because free neutrons 
only live a little under 15 minutes!
"""

import random as rm
import simpy as simp
import numpy as np

def neutron_collisions(env):
    testNum=1   #The test number
    while True:
        print('Test %d' % testNum)
        neutron_energy=rm.randint(0,8)    #The power of the amount of energy the neutron has (changes every test)
        yield env.timeout(1)
        
        if neutron_energy <= 5:   #If the power is 5 or under then it falls into this catagory
            print("eV = 10^%d" % neutron_energy)      #This prints out the amount of electron volts of energy the neutron has
            print("The neutron collided with the target atom and the neutron kept some of its kinetic energy but is moving in another direction")
            
        elif neutron_energy > 5 and neutron_energy <= 7:    #If the power is over 5 but under or equal to 7 it falls into this catagory
            print("eV = 10^%d" % neutron_energy)
            action=['the neutron escapes but with a lower energy level','the neutron escaped with the same amount of energy (but not direction)', 'the neutron dropped to the bottom of the potentail well and then fission occured']
            print("A compound nucleus was formed and",rm.choice(action))
            
        else:     #If the power is 8 and over then it falls under this catagory
            print("eV = 10^%d" % neutron_energy)
            print("A compound nucleus was formed and the neutron escaped with the same amount of energy (but not direction)")
            
        testNum+=1
env = simp.Environment()
env.process(neutron_collisions(env))
env.run(until=6)
