# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:03:04 2020

@author: Pierre-Henri Rossouw

Time Dilation and  Special Relativity

"""

import sys



print("""Cosmic Rays (especially high energy Protons) from deep space collide with our atmosphere roughly 10
km above the Earth's surface. These high energy Protons then decay in Muons (a Lepton - fundamental particle) 
with a very short half of only 2.2 Microseconds they ought to travel roughly 659km, yet we can detect them on 
the surface in cloud and bubble chambers more than 10km's below the atmosphere. How can this be? 
This illustrates Einstein's Special Relativity and this script proves time dilation when velocities
increase to close to the speed of light. So how far would a Muon travel using Newtonian Mechanics?
Well, let's take an example of a very fast moving Muon. Let's say it's velocity is 99.9% of the speed of light. 
The speed of light 'c' is a constant at 2.997 times 10 to the power of 8. Distance is speed times time so let's 
calculate how far they would travel using conventional mechanics. 2.997 * 10 ** 8 *2.2**-6 (mean half life in microseconds) 
If you multiply you will get 659 meters which isn't nearly enough distance to reach the earth's surface, yet we do detect them. 
All because of Time Dilation and Special Relativity """)


user_input=input("""Would you like to test it? Type yes for 
a test and no to exit """)



if user_input == "yes":
    v_input=input("What is the velocity of the particle expressed as a percentile of the speed of light? ")
    v = eval(v_input)
else:
    sys.exit()
    
    
    
c=1

#v_input=input("What is the velocity of the particle expressed as a percentile of the speed of light ")


squares = v**2/c**2     #Partof Lorentz Transformation or Gamma Function
#print(squares)
common = (v**2/c**2)
#print(common)
main_square = (1-common)
denom = main_square**(1/2)
gamma = 1/denom
print("Due to its velocity, the particle's halflife is now multiplied by its own resting decay time by a factor of " , gamma,"MicroSeconds")                    #gamma)

#how long itll live
dtime_input = input("How long before the partcle decays (in microseconds)? ")
dtime=float(dtime_input)
newdecaytime = gamma * dtime
print("The particle's new half life is ", newdecaytime, "microseconds") 



####Still Needs Work###
dist = 659/2.2 #In Metres (If in 2.2 microseconds it travels 659 meters)
part_distance = dist * newdecaytime           #particle's distance after applying Lorenz Transformation
print("That means that due to it's velocity it will now travel", part_distance, "Metres")

#######This section needs loads of work#########

user_input2=input("Press Enter to close the app")


if user_input2 == "yes":
    sys.exit()
else:
    sys.exit()
