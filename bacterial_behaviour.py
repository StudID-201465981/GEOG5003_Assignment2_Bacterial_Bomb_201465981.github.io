# -*- coding: utf-8 -*-
"""
bacterial_behaviour
This is a bespoke module to be called into the bacterial_bomb_model. It contains
the information to create the bacteria locations, move the bacteria and update the 
final locations onto a density map. 

Version: 1.0
Created by: StudID - 201465981
"""

"""Import the random module into the code"""
import random

"""Create an object called Bacteria"""
class Bacteria(): #Create object Bacteria
    
    """Create __init__ method to set the initial conditions of the bacteria including 
    starting location, and height and area variables from bacteria_bomb_model"""
    def __init__(self, height, area): #define __init__ method
        self._x = 50 #set the x coordinate
        self._y = 150 #set the y coordinate
        self.height = height
        self.area = area
  
    """Create the get() method to allow the specified values to be returned without 
    runnning the risk of changing the intitially defined values."""    
    def getx(self): #define getx method
        return self._x #return self
    def gety(self): #define gety method
        return self._y #return y
    
    """Create the set() method to allow the specified values to be redefined to a 
    new value in the code (blocked out as not used)""" 
    #def setx(self, value): #define setx method
    #    return self._x = value #return new value
    #def sety(self, value): #define gety method
    #    return self._y = value #return new value
    
    """Create the horizontal_movement() method to define the XY directional movements
    of the bacteria"""   
    def horizontal_movement(self): #define horizontal_movement method
         wind_direction = random.randint(0,100) #create variable with random number to 100
         
         if wind_direction < 5: #5% chance
             self._x -= 1 #move westwards
         if wind_direction > 5 and wind_direction < 15: #10% chance
             self._y -= 1 #move southwards
         if wind_direction > 15 and wind_direction < 25: #10% chance 
             self._y += 1 #move northwards
         if wind_direction > 25: #75% chance
             self._x += 1 #move eastwards
    
         #return(wind_direction) #for test print
    
    """Create the turbulance() method to determine the height of the bacteria."""
    def turbulance(self, height): #define turbulance method and include hieght variable
        turbulant_direction = random.randint(0,100) #create variable with random number to 100
        
        if self.height >= 75: #for heights equal or above 75m
            if turbulant_direction < 20: #20% chance
                self.height += 1 #rise 1 metre
            elif turbulant_direction > 20 and turbulant_direction < 30: #10% chance
                self.height += 0 #remain level
            elif turbulant_direction > 30: #70% chance
                self.height -= 1 #fall 1 metre
        if self.height < 75: #for heights under 75m
            self.height -= 1 #fall 1 metre
            
        #return(str(turbulant_direction) + " " + str(self.height)) test for print
    
    """Create the add_density() method to show the spread of bacteria"""
    def add_density(self, area): #define add_density method
        if self._y > 0 and self._y < 300 and self._x > 0 and self._x < 300: # if within XY axis 
            self.area[self._y][self._x] += 1 #increament 2D list by 1 at specified XY location 