# Simulations in Python!
The documentation for SimPy is here: https://simpy.readthedocs.io/en/latest/
## Fast Food Sim
This simulates a fast food restaurant's normal day. This restaurant can take 1-6 minutes to finish a meal. But, the customer has an impatience level that ranges from 3-6 which represents the amount of time they're willing to wait. If the impatience level is less than or equal to the wait then the customer leaves.<br>
### Results
After running the program, 5 customers left happy while 5 left unhappy.<br>
## Coronavirus Sim
A certian virus that may or may not start with a C has started infecting people in DC! Each day a number is chosen between 0 and 8. If that number is 3 then it spreads to one more country and the people infected per day is increased by one. If that number is over 5 then the people infected is multiplied by 2. If the number is 1, 2 or 4 then another country gets infected and the amount of people infected per day is increased by 1. By the 15 day point if the randomly drawn number is 1 then the world found a vaccine/cure and the people infected decreases by 5 every day.<br>
### Results
At first the amount of people infected grew exponentally but, after the 15th day the amount of people infected started to decrease just as fast. The amount of countries with infected people stopped increasing at the 15th day, too.<br>
## Neutron Collision Sim
You happen to have a bunch of free neutrons and Fissile isotopes (Uranium 233, 235 and Plutonium 235, 241). So, you make the neutrons and isotopes collide with varying results. The results are based on how fast the neutron goes which is measured in eV (electron volts). You run this expirement 5 times. Make sure you do this very quickly because free neutrons only live a little under 15 minutes!
### Results
1. The first test's neutron had 10^6 eV of energy and a compoud nucleus was formed and the neutron escaped but with a lower energy level
2. The second test's neutron had 10^4 eV of energy and the neutron collided with the target atom and the neutron kept some of its kinetic energy but is moving in another direction
3. The third test's neutron had 10^1 eV of energy and the neutron collided with the target atom and the neutron kept some of its kinetic energy but is moving in another direction
4. The fourth test's neutron had 10^4 eV of energy and the neutron collided with the target atom and the neutron kept some of its kinetic energy but is moving in another direction
5. In the last test the neutron had 10^8 eV of energy and a compound nucleus was formed and the neutron escaped with the same amount of energy (but not direction)
