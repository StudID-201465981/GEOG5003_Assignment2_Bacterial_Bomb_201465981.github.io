# -*- coding: utf-8 -*-
"""
bacterial_bomb_model
description



Version: 1.0
Created by: StudID - 201465981
"""


"""Import the modules to be used in the bacterial_bomb_model code - csv, matplotlib.animation, 
matplotlib.pyplot, numpy, time, """
import csv
import matplotlib.animation
import matplotlib.pyplot
import numpy
import time



"""Use the timer function to check how long it takes to run the model.(Start)"""
start_timer = time.process_time() #create start_timer variable to read the time



"""Open and read in the wind_raster file using the csv reader. Create a 2D list
called area which is used to create a visual display for the model and act as the 
map for the bacterial spread."""
wind_raster = open('wind.raster', newline='') #open wind.raster file in the directory to create variable
wind_raster_csv = csv.reader (wind_raster, quoting=csv.QUOTE_NONNUMERIC) #use the csv reader and convert to float
area = [] #create a blank list named area
for row in wind_raster_csv: #for each row of data within the wind_raster variable
    row_list = [] #create a blank list named row_list
    for value in row: #for each value within the row
        row_list.append(value) #create many 1D lists full of values
    area.append(row_list) #make these lists into a 2D list which contains the area
wind_raster.close() #close wind raster file as it is no longer needed in the model

#matplotlib.pyplot.imshow(area) #test area working
#matplotlib.pyplot.show() #test area working



"""Create the variables for the code"""
bacteria = [] #empty list to hold the bacteria coordinate values
bacteria_count = 5000 #number of bacteria



""""""



"""Discover the position of the bomb epicentre Y and X coordinates from the
2D list, utilising the unique value.

Convert the 255 value to 0 in area to ensure the bacteria density.
Write the output file to test that 255 has changed """
check_loc = numpy.array(area) #create an array to use numpy functions on
epicentre_yx = numpy.argwhere(check_loc == 255) #find the index of the bomb epicenter, given as row (Y) then value (X)
epicentre = epicentre_yx[:, ::-1] #reverse for model print statement, XY is more relatable to the end user
print("The XY coordinates for the bomb epicentre are " + str(epicentre).strip('[]')) #printout for model output

area[150][50] = 0 #update bomb epicentre value to 0
#print(area[150][50]) #test print



"""Find the size of the area for further coding inputs then comment out of the 
final model. (Answer 300).

Create a new figure to set the popup frame and the continue_animation variable 
to get the animation continuing/ stopping contidition.

Create the update function and call in the continue_animation variable. Create
a 300 x 300 grid and show the area as background.

Create the animation including the input parameters and play the animartion."""
#size_of_area = len(area) #count the amount of rows in the area
#print("The size of the environment is " + str(size_of_area)) #test print

holder=10

figure = matplotlib.pyplot.figure(figsize=(7, 7)) #create the figure, specify the window size in inches
axes = figure.add_axes([0, 0, 1, 1]) #create the XY axis 
continue_animation = True #whilst carry_on equals true the animation will keep running

def update(frame): #create a new function
    global continue_animation #global variables can be used accross functions
    matplotlib.pyplot.ylim(0, 300) #create y axis (using the size of area value)
    matplotlib.pyplot.xlim(0, 300) #create x axis (using the size of area value)
    matplotlib.pyplot.imshow(area) #show the area

#create the animation to bring in the figure varable, call in the update function, 
#1 millisecond interval between frames, do not repeat after animation finished and total number of frames
animation = matplotlib.animation.FuncAnimation(figure, update, interval=1, repeat=False, 
                                                     frames=holder) 
matplotlib.pyplot.show() #show the animation



"""Use the timer function to check how long it takes to run the model.(End)"""
end_timer = time.process_time() #create end_timer variable to read the time
print("Model runtime = " + str(end_timer - start_timer)) #print end time minus start time