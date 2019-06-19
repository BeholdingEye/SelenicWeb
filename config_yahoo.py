#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_config():
    """
    Returns Yahoo config
    
    """
    # Initial delay
    initialDelay = 5
    
    # Ending delay
    endingDelay = 5
    
    # Search string for this config
    searchString = "digital camera"
    
    # Maximum number of search result pages to traverse
    searchPagesMax = 3

    config_yahoo = {
        
        "initialDelay"      : initialDelay,
        "endingDelay"       : endingDelay,
        "sleepAfterAction"  : 2 + (3 * random.random()),
        "optionsArguments"  :   [
                                    "--start-maximized",
                                    "--disable-infobars",
                                    "--disable-extensions",
                                    "load-extension", # Disabling, rather than enabling, preventing a warning popup
                                    #"--user-data-dir=/path/to/chrome", # Use the path to your Chrome config folder
                                    "test-type=browser"
                                ],
        "avoidDetection"    : False,
        "searchingSite"     : "http://www.yahoo.com",
        "searchCondition"   : {"title" : "Yahoo"},
        "searchActions"     :   [
                                    {
                                        "elementByType" : "name",
                                        "elementValue" : "agree",
                                        "actionType" : "click",
                                        "actionValue" : None,
                                        "callback" : None,
                                        "searchResultURLQuery" : None,
                                        "searchResultBlockQuery" : None,
                                        "elementOptional" : True,
                                    },
                                    {
                                        "elementByType" : "name",
                                        "elementValue" : "p",
                                        "actionType" : "type-text",
                                        "actionValue" : searchString + Keys.ENTER,
                                        "callback" : None,
                                        "searchResultURLQuery" : None,
                                        "searchResultBlockQuery" : None,
                                    },
                                    {
                                        "elementByType" : "query-multi",
                                        "elementValue" : "div#main div#web ol.searchCenterMiddle > li",
                                        "actionType" : "get-html",
                                        "actionValue" : None,
                                        "callback" : process_search_results,
                                        "searchResultURLQuery" : "h3.title a",
                                        "searchResultBlockQuery" : "div.compText p",
                                    },
                                ],
        "searchPaginate"    :   [
                                    {
                                        "elementByType" : "query",
                                        "elementValue" : "ol.searchBottom div.pagination a.next",
                                        "actionType" : "click",
                                        "actionValue" : None,
                                        "callback" : None,
                                        "searchResultURLQuery" : None,
                                        "searchResultBlockQuery" : None,
                                    },
                                    {
                                        "elementByType" : "query-multi",
                                        "elementValue" : "div#main div#web ol.searchCenterMiddle > li",
                                        "actionType" : "get-html",
                                        "actionValue" : None,
                                        "callback" : process_search_results,
                                        "searchResultURLQuery" : "h3.title a",
                                        "searchResultBlockQuery" : "div.compText p",
                                    },
                                ],
        "searchPagesMax"    :   max(0,searchPagesMax-1),
    }
    print("We are going to obtain up to "+str(max(0,searchPagesMax-1))+" pages of search results on Yahoo for:", searchString)
    return config_yahoo


def process_search_results(elements, SWobj):
    """
    Processes search result HTML elements
    
    """
    for el in elements:
        url = el.find_element_by_css_selector(SWobj.searchResultURLQuery)
        resultBlock = el.find_element_by_css_selector(SWobj.searchResultBlockQuery)
        if url_satisfies_conditions(url, SWobj) and result_block_satisfies_conditions(resultBlock, SWobj):
            use_element(el, url, resultBlock, SWobj)
    return 0


def url_satisfies_conditions(url, SWobj):
    """
    Tests URL
    
    """
    # TODO
    return True


def result_block_satisfies_conditions(resultBlock, SWobj):
    """
    Tests resultBlock
    
    """
    # TODO
    return True


def use_element(element, url, resultBlock, SWobj):
    """
    Performs action on element and its url/resultBlock components
    
    """
    print(url.get_attribute("href"))
    print("")
    print(resultBlock.text)
    print("----")
    return 0


def main():
    print("This is a config file, to be called from main.py.")
    sys.exit()

if __name__ == "__main__":
    main()
