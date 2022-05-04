# -*- coding: utf-8 -*-
"""
bacterial_bomb_model
The model is used to track the movements of biological fallout from a bomb filled
with bacteria, and return the density data.

- The wind_raster file is read into the model, and used to build the area.
- The bacteria, bacteria_count and height variables are created.
- The starting XY positions are returned from the unique area value.
- The bacteria list is populated using the bacteria_count and the starting XY positions.
- Calls the methods from bacterial_behaviour.py to move the bacteria and alter the area.
    The turbulance method controls the bacteria's height.
    The horizontal_movement method controls the bacteria's XY direction.
    The add_density method marks the bacteria location on the area.
- Add and show the density map.
- Print interesting data values.
- The output_area showing density writen as a text file in the directory.

Version: 1.0
Created by: StudID - 201465981
"""


"""Import the modules to be used in the bacterial_bomb_model code - bacterial behavious, 
csv, matplotlib.animation, matplotlib.pyplot, numpy, time"""
import bacterial_behaviour
import csv
import matplotlib.animation
import matplotlib.pyplot
import numpy
import sys
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
height = 75#height in meters

"""Create input parameter and default values for command line"""
bacteria_count = int(sys.argv[1]) if len(sys.argv) >= 2 else 5000 
height = int(sys.argv[2]) if len(sys.argv) >= 3 else 75 #the parameter order of entry is bacteria_count then height


"""Discover the position of the bomb epicentre Y and X coordinates from the
2D list, utilising the unique value.
Convert the 255 value to 0 in area to ensure the bacteria density.
Write the output file to test that 255 has changed """
area_array = numpy.array(area) #create an array to use numpy functions on
epicentre_yx = numpy.argwhere(area_array == 255) #find the index of the bomb epicenter, given as row (Y) then value (X)
epicentre = epicentre_yx[:, ::-1] #reverse for model print statement, XY is more relatable to the end user
#print("The XY coordinates for the bomb epicentre are " + str(epicentre).strip('[]')) #printout for model output

area[150][50] = 0 #update bomb epicentre value to 0
#print(area[150][50]) #test print

"""Create the bacteria"""
for i in range(bacteria_count): #for the amount of bacteria stated in the count
    bacteria.append(bacterial_behaviour.Bacteria(height, area)) #populate bacteria variable using Bacteria object

"""Move the bactreia to their final location"""
for i in range(height * 2): #large number to allow height to reach 0
    for i in range(bacteria_count): #for the amount of bacteria stated in the count
        if bacteria[i].height > 0: #complete the actions if bacteria is in the air or 'moveable'
            #print(str(bacteria[i].horizontal_movement()) + " " + 
            #str(bacteria[i].getx()) + " " + str(bacteria[i].gety()) + 
            #" " + str(bacteria[i].turbulance(height))) #test print
            bacteria[i].turbulance(height) #adjust the bacteria height
            bacteria[i].horizontal_movement() #move the bacteria 
            bacteria[i].oob() #check for out of bounds bacteria

"""Create the density map"""
for i in range(bacteria_count): #for each bacteria
    bacteria[i].add_density(area) #add the location to the area
    #matplotlib.pyplot.scatter(bacteria[i].getx(),bacteria[i].gety()) #test plot

"""Find the size of the area for further coding inputs then comment out of the 
final model. (Answer 300)."""
#size_of_area = len(area) #count the amount of rows in the area
#print("The size of the environment is " + str(size_of_area)) #test print

"""Display the density map"""
matplotlib.pyplot.ylim(0, 300) #create y axis (using the size of area value)
matplotlib.pyplot.xlim(0, 300) #create x axis (using the size of area value)
matplotlib.pyplot.imshow(area) #show the area

matplotlib.pyplot.show() #create the popup

#check_density = sum(sum(area,[])) #test density
#print(check_density) #test density

"""Return writen data values"""
outside_count = 0 #create variable with int value 0
for i in range(bacteria_count): # for the bacteria
    if bacteria[i].getx() < 0 or bacteria[i].getx() > 300 or bacteria[i].gety() < 0 or bacteria[i].gety() > 300: #if outside X or Y axis
        outside_count += 1 #increase outside_count by 1

densest = numpy.max(numpy.array(area)) #obtain the maximum area value

x_list = [] #create empty list for X axis values
y_list = [] #create empty list for y axis values
for i in range(bacteria_count): #for the bacteria
    x_list.append(bacteria[i].getx())#append the x values to a list
    y_list.append(bacteria[i].gety())#append the y values to a list
    spread = ((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))#formula to estimate the area coverage
    
#Printed data returns for user
print("The XY coordinates for the bomb epicentre are " + str(epicentre).strip('[]')) #print bomb location
print(str(outside_count) + " bacteria particles landed outside the study area")
print("The most dense location contains " + str(densest) + " bacteria particles")
print("The estimated area spread of the bacteria particles is " + str(spread) + " metres squared")

"""Write area_output.txt file to include the updated area"""
write_area = open('area_output.txt', 'w', newline='') #open area_output.txt
writer = csv.writer(write_area, delimiter=',') #use csv writer function
for row in area: #for each row of data within area
    writer.writerow(row) #write the row values in the text file
write_area.close() #close write_area_output.txt

"""Use the timer function to check how long it takes to run the model.(End)"""
end_timer = time.process_time() #create end_timer variable to read the time
print("Model runtime = " + str(end_timer - start_timer)) #print end time minus start time



"""Attempted to use animation however came accross issues, redundant code left 
at bottom of main code"""

"""Create a new figure to set the popup frame and the continue_animation variable 
to get the animation continuing/ stopping contidition.

Create the update function, clear the figure and call in the continue_animation
variable. Create a 300 x 300 grid and show the area as background.

Create the animation including the input parameters and play the animartion."""

"""figure = matplotlib.pyplot.figure(figsize=(7, 7)) #create the figure, specify the window size in inches
axes = figure.add_axes([0, 0, 1, 1]) #create the XY axis 
continue_animation = True #whilst carry_on equals true the animation will keep running

def update(frame_number): #create a new function
    figure.clear() #clear the figure between animations
    global continue_animation #global variables can be used accross functions
    
    matplotlib.pyplot.ylim(0, 300) #create y axis (using the size of area value)
    matplotlib.pyplot.xlim(0, 300) #create x axis (using the size of area value)
    matplotlib.pyplot.imshow(area) #show the area
    
    
    for i in range(bacteria_count): #for the amount of bacteria stated in the count
        if bacteria[i].height > 0:    
            print(str(bacteria[i].horizontal_movement()) + " " + str(bacteria[i].getx()) + " " + str(bacteria[i].gety()) + " " + str(bacteria[i].turbulance(height)))
            bacteria[i].turbulance(height)
            bacteria[i].horizontal_movement() #call the horizontal_movement method 
        if bacteria[i].height == 0:    
            area[bacteria[i].gety()][bacteria[i].getx()] += 1
        if bacteria_count <= 500:
            matplotlib.pyplot.scatter(bacteria[i].getx(),bacteria[i].gety()) #plot the XY coordinates
       
    
    if random.random() < 0: #no chance
        continue_animation = False #make carry_on false
        print("stopping condition") #Test print


def gen_function(b = [0]): #create the gen_function function
    a = 0 #create variable and set to 0
    global continue_animation #check carry_on is true
    while (a < 100) & (continue_animation) : #whilst a is under and carry_on
        yield a			# Returns control and waits next call.
        a += 1 #add 1 to a
        
#create the animation to bring in the figure varable, call in the update function, 
#1 millisecond interval between frames, do not repeat after animation finished and total number of frames
animation = matplotlib.animation.FuncAnimation(figure, update, frames=gen_function, repeat=False) 
matplotlib.pyplot.show() #show the animation
"""