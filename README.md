## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python

This code takes user input of latitude and longitude coordinates and outputs the five-day weather forecast for that location.

The code imports the libraries necessary for web scraping. Then the user will be prompted to input the coordinates of the place for which they want to get a weather forecast, with the specifications that the coordinates should be in decimal degrees to four decimal places and put in quotes. The coordinates should be put in quotes so they will be a string and not a float. Because people are often bad at following directions, the code tests if the input is a string or not. I had some trouble with the logic statement, but I found the function isinstance(variable, type) on geeksforgeeks.org, which has worked well. If the input is not a string, it is converted to one. The coordinates are then put into a string variable called url, to form a url for the website forecast.weather.gov. The code gets all the information from that web page, which is then stored in a beautiful soup object. The page content is accessed using an html parser. The code then goes through each element of the website to find the specified elements, which are a five-day weather forecast. The five days of the weather forecast are stored in a list. Some of the spacing one would expect in proper English is not present in these forecasts because it was not preserved during the web scraping. The replace function is used to remedy this. The forecast is then converted entirely to uppercase letters and output using the print function.

## Final Project: Script 2
### Volume Calculator
This script can calculate the volume of a prism, cuboid, and cylinder, and can convert between units for the input and output. 

### Volume Calculator Workflow:
Firstly, the user enters the base shape that they want to calculate the volume of runoff for. Three shapes: triangle, rectangle and circle, are provided for the user to choose from. 

Secondly, the user selects the input units, which can be inch, foot or meter. 

Thirdly, the user selects the units for output and there are three units, cubic feet, gallons and cubic meters to choose from. 
If the statement entered by the user in the above three steps is not compatible, the user will get a message telling them they have entered an invalid word and to try again.

Fourthly, the user needs to input the required graphics parameters, among which, triangle needs an input of three side lengths and height, rectangle needs the inputs length, width and height, and circle needs the inputs radius length and height. 

The output result is the numeric result of the calculation in the output unit selected by the user. However, if the value entered by the user cannot form a triangular prism; for example, if the user inputs 2, 899, 3 as the three sides of a triangle, which is impossible, the program will report an error and go to end.

### Documentation for Designing the Project
In the process of designing the program, our initial plan was only to calculate the volume of a solid figure with three different base shapes. But after reviewing lab1, I found that unit conversion also matters, so I added the unit conversion module. Writing the project was relatively simple, in that it did not require the use of complex statements. In the process of writing the first version of this project, I let the program automatically run overused if the user enters the wrong statement. After searching from the website, Stackoverflow.com, I adopted the sys.Exit(0) statement. In the subsequent tests, we thought that the immediate quit after inputting wrong parameters was inconvenient. We had some problems in the third input for choosing the unit for output. The program will stop and print the sentence, “the input is wrong”, even if the user enters correct word(s) in the online compiler. We decided to change the input process to have while loops that are exited when the user input is correct. As long as the input is incorrect the user will keep getting prompted to change the input.

