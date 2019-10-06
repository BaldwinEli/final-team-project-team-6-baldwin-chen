## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
The code imports the libraries necessary for web scraping. Then the user will be prompted to input the coordinates of the place for which they want to get a weather forecast, with the specifications that the coordinates should be in decimal degrees to four decimal places and put in quotes. The coordinates should be put in quotes so they will be a string and not a float. Because people are often bad at following directions, the code tests if the input is a string or not. I had some trouble with the logic statement, but I found the function isinstance(variable, type) on geeksforgeeks.org, which has worked well. If the input is not a string, it is converted to one. The coordinates are then put into a string variable called url, to form a url for the website forecast.weather.gov. The code gets all the information from that web page, which is then stored in a beautiful soup object. The page content is accessed using an html parser. The code then goes through each element of the website to find the specified elements, which are a five-day weather forecast. The five days of the weather forecast are stored in a list. Some of the spacing one would expect in proper English is not present in these forecasts because it was not preserved during the web scraping. The replace function is used to remedy this. The forecast is converted entirely to uppercase letters and then output using the print function.

## Final Project: Script 2
### Volume Calculater
This script can calculate the volume of a prism, cuboid, and cylinder, and can convert units for the input and output results. 

### Volume Calculater Workflow:
firstly, the user enters the base shape that he wants to calculate, and three kinds of shapes, triangle, rectangle and circle, are provided for the user to choose; 

secondly, the user selects the units for input, which are inch, foot and meter; 

thirdly, the user selects the units for output and there are three units, cubic feet, gallon and cubic meters,for choosing. 
<In the statement entered by the user in the above three steps, if the user enters a mistake, it will return to enter the statements again;>

Fourthly, the user needs to input the required graphics parameters, among which, triangle needs to input three side lengths, rectangle needs to input length and width, circle needs to input radius length. 

The output result is the numeric result of the calculation and the output unit selected by the user, but if the value entered by the user cannot form a graph, for example, if the user inputs 2,899,3 as the three sides of a triangle, which cannot form a triangle, the program will report an error and go to end.

### Documentation for Designing the Project
In the process of designing the program, our initial assumption was only to calculate the volume of solid figure with three different base shapes. But after reviewing lab1, I found that units conversion also matters, so I added the units conversion module. Writing the project is relatively simple, for not using complex statements. In the process of writing the first version of this project, I let the program automatically run overused if the user enters the wrong statement. After searching from the website, Stackoverflow.com, I adopted the sys. Exit (0) statement. In the subsequent tests, we thought that the immediate quit after inputting wrong parameters is not so convenient and we did have some problems in the third input for choosing the unit for output. The program will stop and print the sentence, “the input is wrong”, even if the user enters the correct words. So we change the choosing statements into loop statement instead. After the user input the wrong words, the program still can allow users to enter again to continue the calculation.
