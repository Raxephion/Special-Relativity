# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:03:04 2020

@author: Pierre-Henri Rossouw

Time Dilation and  Special Relativity

"""

import sys


print("""Cosmic Rays from deep space collide with our atmosphere roughly 10
km above the Earth's surface. With a half life of 2.2 Microseconds
they ought to travel roughly 659km, yet we can detect them on the surface in
cloud and bubble chambers more than 10km's below the atmosphere. How can this be? This illustrates Einstein's
Special Relativity and this script proves time dilation when velocities
increase to close the speed of light. """)
user_input=input("""Would you like to test it? Type yes for 
a test and no to exit """)



if user_input == "yes":
   v_input=input("What is the velocity of the particle expressed as a percentile of the speed of light ")
   v = eval(v_input)
else:
    sys.exit()
    
    
    

c=1

#v_input=input("What is the velocity of the particle expressed as a percentile of the speed of light ")


squares = v**2/c**2     #Partof Lorentz Transformation or Gamma Function
print(squares)
common = (v**2/c**2)
print(common)
main_square = (1-common)
denom = main_square**(1/2)
gamma = 1/denom
print("Due to its velocity, the particle's halflife is now multiplied by its own resting decay time by" , gamma,"MicroSeconds")                    #gamma)

#how long itll live

dtime_input = input("How long before the partcle decays (in microseconds)? ")
dtime=float(dtime_input)
newdecaytime = gamma * dtime
print("The particle will now decay in ", newdecaytime, "MicroSeconds") 



####Still Needs Work###
dist = 659/2.2 #In Metres
part_distance = dist * newdecaytime
print("That means that due to it's velocity it will now travel", part_distance, "Metres")
