# GEOG5003_Ass2_Bacterial_Bomb_201465981.github.io
 Assignment 2 'Bacterical Bomb' for Programming for Geographical Information Analysis Module

The README documentation is used to list and explain the contents of the github repository,
and to provide an overview and user instructions of the bacterial_bomb model. 


The contents for the GitHub repository (reading from top to bottom) are as follows:-
- __pycache__ - an area holding cached files.
- .gitattributes - a file created whilst setting up the github repository.
- GEOG5003_Ass2_2022_Bacterial_Bomb_Development_Guide_201465981 - the document which outlines
  the development process of the model from cencept to exercution including issues during development.
- LICENSE - the license file stipulates the open source licence for the code.
- README.md - this document, provides initial instructions and overview for user orientation
- _config.yml - the file to set the theme for the landing page, the chosen theme was a Jekyll tactile theme.
- area_output.txt - the output text file written to record the changes from the input text file.
- bacterial_behaviour.py - the module code which is imported into the main model.
- bacterial_bomb_model.py - the code which builds the model.
- index.md - the text file for the website.
- wind.raster - the input data file to make the area.


A brief description of the agent model:-
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


To run the model use the instructions below:-
- Create a local directory.
- Download and save the following files from the github repository and into the directory, 
  bacterial_bomb_model.py, bacterial_behaviour.py, wind_raster.txt.
- Open a cmd prompt on the system.
- Navigate to the local directory in the cmd prompt using the cd function.
- Type bacterial_bomb_model.py and the input parameters in the cmd, there are two parameters and the entered value
  must be a whole number. They must be entered in the following order and separated by a space, bacteria_count
  and height. An example user input method is 'bacterial_bomb_model.py 1000 100'.
    If no imput parameters are entered then default values are used, for bacteria_count the default
	is 5000 and for height the default is 75
- Hit the enter key, to run the model and get the results.

- Please note the matplotlib module may not be available to run on cmd as standard, if this error is 
  encountered then there is a useful troubleshooting guide which can be accessed [here](https://pythonguides.com/no-module-named-matplotlib/#:~:text=the%20above%20topics.-,modulenotfounderror%3A%20no%20module%20named%20'matplotlib'%20pycharm,most%20probably%20it%20will%20work.)
  

The expected output after running the model:-
- Within the cmd the following data will be printed:- 
    - the XY coordinates of the bomb location.
	- a count of bacteria particles landing outside of the area.
	- the densest bacteria location value.
	- the estimated spread of the bacteria.
	- the time in seconds it took for the model to run.
- A popup display will show the area density map after the model actions have been carried out.
- The area_output.txt file will be populated with the bacteria density values.


- Please note the user may print additional lines of data when running the model if required, 
  which were used during the model testing. These have been blanked out in the bacterial_bomb_model.py 
  code, however the user may remove the # where appropriate. 