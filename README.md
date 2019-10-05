## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
The code imports the libraries necessary for web scraping. Then the user will be prompted to input the coordinates of the place for which they want to get a weather forecast, with the specifications that the coordinates should be in decimal degrees to four decimal places and put in quotes. The coordinates should be put in quotes so they will be a string and not a float. Because people are often bad at following directions, the code tests if the input is a string or not. I had some trouble with the logic statement, but I found the function isinstance(variable, type) on geeksforgeeks.org, which has worked well. If the input is not a string, it is converted to one. The coordinates are then put into a string variable called url, to form a url for the website forecast.weather.gov. The code gets all the information from that web page, which is then stored in a beautiful soup object. The page content is accessed using an html parser. The code then goes through each element of the website to find the specified elements, which are a five-day weather forecast. The five days of the weather forecast are stored in a list. Some of the spacing one would expect in proper English is not present in these forecasts because it was not preserved during the web scraping. The replace function is used to remedy this. The forecast is converted entirely to uppercase letters and then output using the print function.

## Final Project: Script 2
### Your Chosen Assignment
For this script, you will complete the assignment that you have proposed, which involves modifying a previous exercise. Remember to update the Script2.py file to include comments and documentation in your script to tell me what it’s doing!

## Final Project: Documentation
### Changing this README
Your write-up will be here, on this README page. You will need to edit this page with your new text: you do **not** need to keep these instructions on your README! 
