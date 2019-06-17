# SelenicWeb
Chrome automation tool for data scraping

This is a starter app demonstrating the Selenium module by automating 
Chrome to access Yahoo, perform a search for the keyword entered on the 
commandline, and print the URLs from the first page of web search 
results, excluding advertisements.

Requires Python 3.5+, Selenium module, and WebDriver for Chrome.

Usage:
------

`python3 main.py YOUR_SEARCH_KEYWORD`

The script will access Yahoo, click the big OK button, enter your 
keyword in the search box, and print out the URLs.

In case of breakage, check that the "args" settings in the `main()` 
function are still correct for Yahoo.

This script may serve as a starting point for more sophisticated 
scraping.
