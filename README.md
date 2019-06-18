# SelenicWeb
*Chrome automation tool for data scraping*

This is a starter app demonstrating the Selenium module by automating 
Chrome to access Yahoo, perform a search for the keyword entered in the 
configuration file, and print the URLs from the web search results, 
excluding advertisements.

Requires Python 3.5+, Selenium module, and WebDriver for Chrome.

### Usage:

`python3 main.py CONFIGURATION_NAME`

A configuration module "config_yahoo.py" is provided, which the 
"main.py" module imports to search Yahoo. The config module contains 
functions for evaluation of results from Yahoo. For other websites, 
create other config files by duplicating the Yahoo file and making 
changes. To make use of your own config, you will also have to edit the 
config loading in the `main()` function in "main.py".

The Yahoo config will access Yahoo, click the big OK button, enter your 
search string in the search box, and print out the search result URLs 
and text blurbs. The number of pages of results to obtain can be set, as
can the randomised delay between actions.

In case of breakage, check that the config settings are still valid.

This script may serve as a starting point for more sophisticated 
scraping.
