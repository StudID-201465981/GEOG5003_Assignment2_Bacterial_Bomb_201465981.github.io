# -*- coding: utf-8 -*-
"""
bacterial_bomb_model
description



Version: 1.0
Created by: StudID - 201465981


"""

"""Import the modules to be used in the bacterial_bomb_model code - matplotlib.pyplot,
time, """
import matplotlib.pyplot
import time
import csv

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
wind_raster.close() #close wind raster file as it is no linger needed in the model

matplotlib.pyplot.imshow(area) #test area working
matplotlib.pyplot.show() #test area working

"""Use the timer function to check how long it takes to run the model.(End)"""
end_timer = time.process_time() #create end_timer variable to read the time
print("Model runtime = " + str(end_timer - start_timer)) #print end time minus start time