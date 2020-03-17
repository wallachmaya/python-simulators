"""
Disease Sim!
Variables:
-Amount of people infected
-Amount of countries infected
-Amount of people infected per day
-When the world creates a vaccine/cure
Scenario: 
A certian virus that may or may not start with a C has started infecting people in DC! 
Each day a number is chosen between 0 and 8. If that number is 3 then it spreads to one more country 
and the people infected per day is increased by one. If that number is over 5 then the people infected 
is multiplied by 2. If the number is 1, 2 or 4 then another country gets infected and the amount of 
people infected per day is increased by 1. By the 15 day point if the randomly drawn number is 1 then 
the world found a vaccine/cure and the people infected decreases by 5 every day.
"""
def DC(env):
    pplInfected=1
    countries=1
    spreader=2
    while True:
        print('Virus day %d' % env.now)
        spread = rm.randint(0,8)
        yield env.timeout(1)
        if env.now>=15:
            if spread>=1:
                pplInfected-=5
        else:
            if spread == 3:
                pplInfected+=spreader
                countries+=1
            elif spread > 5:
                pplInfected*=2
            else:
                countries+=1
                spreader+=1
        print('Virus has infected', pplInfected,'at day %d' % env.now)
        print('The virus is in',countries,'countries')
env = simp.Environment()
env.process(DC(env))
env.run(until=26)
