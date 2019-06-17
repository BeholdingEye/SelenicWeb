#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#                                                                      #
#                            SELENICWEB                                #
#                                                                      #
#               Demonstration of Chrome automation with                #
#                         the Selenium module                          #
#                                                                      #
#            Copyright 2019 Karl Dolenc, beholdingeye.com.             #
#                         All rights reserved.                         #
#                                                                      #
#                       Tested with Python 3.5.                        #
#                                                                      #
########################################################################

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


import sys, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SelenicWeb:
    """
    Main class, demonstrating the Selenium module by automating Chrome
    to access Yahoo, perform a search for the keyword entered on the 
    commandline, and print the URLs from the first page of web search 
    results, excluding advertisements
    
    """
    
    def __init__(self, args):
        """
        "args" dict:
        
            sleepAfterAction: number of seconds to pause after an action
            searchingSite: site to search
            searchCondition: condition that must be true for the search site
            searchActions: list of dicts specifying series of elements and actions to perform on them
        
        """
        self.sleepAfterAction = args["sleepAfterAction"]
        self.searchingSite = args["searchingSite"]
        self.searchCondition = args["searchCondition"]
        self.searchActions = args["searchActions"]
        
        self.start_search()
        self.browser.quit()
    
    
    def start_search(self, *args, **kwargs):
        """
        Start browsing with searchingSite
        
        """
        self.get_browser()
        self.get_url(self.searchingSite)
        if self.evaluate_site(condition=self.searchCondition):
            print("Site accessed - we are ready to test for elements and act on them")
            time.sleep(self.sleepAfterAction)
            for actionSpec in self.searchActions:
                # elem may be a list of elements
                elem = self.get_action_element(actionSpec["elementByType"], actionSpec["elementValue"])
                if elem and not isinstance(elem, list):
                    print("Element found:", actionSpec["elementByType"], "-", actionSpec["elementValue"])
                    result = self.do_action(elem, actionSpec["actionType"], actionSpec["actionValue"])
                    print("Action performed:", actionSpec["actionType"])
                    time.sleep(self.sleepAfterAction)
                    if result:
                        self.process_result(result) # TODO
                elif elem and isinstance(elem, list):
                    self.process_elements(elem)
            print("Quit")
        return 0
    
    
    def process_elements(self, elements): # TODO make generic
        """
        Processes elements
        
        """
        print("==== Processed results:")
        for elem in elements:
            elemURL = elem.get_attribute("href")
            if elemURL: print(elemURL)
        print("==== Processing completed")
        return 0
    
    
    def process_result(self, result):
        """
        Process the result of an action
        
        """
        # TODO
        return 0
        
    
    def get_browser(self, *args, **kwargs):
        """
        Return Chrome browser instance
        
        """
        self.browser = webdriver.Chrome()
        return 0
    
    
    def evaluate_site(self, condition={}):
        """
        Evaluates a condition about the site; the condition is a dict:
        
            {"title" : "text to evaluate in browser title"}
        
        """
        for x in condition.keys():
            if x == "title":
                if condition[x] not in self.browser.title: return False
        return True
    
    
    def get_url(self, url):
        """
        Gets URL in our browser property
        
        """
        self.browser.get(url)
        return 0
    
    
    def get_action_element(self, elemByType, elemByStr):
        """
        Gets the element(s) we need for an action:
        
            elemByType: "name"/"class"/"id" etc.
            elemByStr: identifying string for attribute specified by elemByType
        
        """
        if elemByType == "name": elem = self.browser.find_element_by_name(elemByStr)
        elif elemByType == "class": elem = self.browser.find_element_by_class_name(elemByStr)
        elif elemByType == "id": elem = self.browser.find_element_by_id(elemByStr)
        elif elemByType == "query": elem = self.browser.find_element_by_css_selector(elemByStr)
        
        elif elemByType == "query-multi": elem = self.browser.find_elements_by_css_selector(elemByStr)
        
        elif elemByType == "tag": elem = self.browser.find_element_by_tag_name(elemByStr)
        elif elemByType == "link-text": elem = self.browser.find_element_by_link_text(elemByStr)
        elif elemByType == "partial-link-text": elem = self.browser.find_element_by_partial_link_text(elemByStr)
        
        return elem # Could be a list if "query-multi"
    
    
    def do_action(self, element, actionType, actionValue):
        """
        Performs action on element
        
        """
        if actionType == "type-text": element.send_keys(actionValue)
        elif actionType == "click": element.click()
        elif actionType == "get-text":
            return element.text
        elif actionType == "get-html":
            return element.get_attribute('outerHTML')
        return 0



def main():
    """
    Testing
    
    In case of breakage, check if the args are still correct
    
    """
    # Get search string from commandline
    if len(sys.argv) < 2:
        print("Missing search string parameter")
        sys.exit()
    searchString = sys.argv[1]
    
    # The "args" structure defines our activity on the site
    args = {
        "sleepAfterAction"  : 2,
        "searchingSite"     : "http://www.yahoo.com",
        "searchCondition"   : {"title" : "Yahoo"},
        "searchActions"     :   [
                                    {
                                        "elementByType" : "name",
                                        "elementValue" : "agree",
                                        "actionType" : "click",
                                        "actionValue" : None,
                                    },
                                    {
                                        "elementByType" : "name",
                                        "elementValue" : "p",
                                        "actionType" : "type-text",
                                        "actionValue" : searchString + Keys.ENTER,
                                    },
                                    {
                                        "elementByType" : "query-multi",
                                        "elementValue" : "div#main div#web ol.searchCenterMiddle > li h3.title a",
                                        "actionType" : "get-html",
                                        "actionValue" : None,
                                    },
                                ],
    }
    sw = SelenicWeb(args)
    return 0

if __name__ == "__main__":
    main()
