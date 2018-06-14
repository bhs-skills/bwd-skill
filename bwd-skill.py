#!/usr/bin/env python3
#****************************************************************************
# BHS 2018-07-12 Experiments in web scraping with Python BeautifulSoup

#****************************************************************************
# I M P O R T S
#****************************************************************************

#import urllib2
from bs4 import BeautifulSoup
import sys

#****************************************************************************
def localize(location):

    if   location == "bowie-north":    return "***.xml"
    elif location == "bowie-south":    return "bowie.xml"
    elif location == "dixon-entrance":    return "dixon-entrance.xml"
    elif location == "douglas-channel":    return "douglas-channel.xml"
    elif location == "explorer":    return "explorer.xml"
    elif location == "hecate-strait":    return "hecate-strait.xml"
    elif location == "queen-charlotte-sound-west":    return "queen-charlotte-sound.xml"
    elif location == "queen-charlotte-sound-east":    return "***.xml"
    elif location == "west-coast-haida-gwaii-north":    return "west-coast-haida-gwaii-north.xml"
    elif location == "west-coast-haida-gwaii-south":    return "west-coast-haida-gwaii-south.xml"
    elif location == "west-coast-vancouver-island-north":    return "west-coast-vancouver-island-north_15300.xml"
    elif location == "west-coast-vancouver-island-south":    return "west-coast-vancouver-island-south_16200.xml"
    elif location == "johnstone-strait":    return "johnstone-strait_06800.xml"
    elif location == "howe-sound":    return "howe-sound_06400.xml"
    elif location == "georgia-strait":    return "georgia-strait_14300.xml"
    elif location == "haro-strait":    return "haro-strait_06100.xml"
    elif location == "juan-de-fuca-strait":    return "juan-de-fuca-strait_07000.xml"
    else:    return None

#****************************************************************************
# M A I N L I N E
#****************************************************************************

print("**************************************************************")
print("*** Execute " + sys.argv[0])

path = "/home/brian/Devel/bwd/samples"

localeName = sys.argv[1]
feedPage = localize(localeName)
if feedPage is None:
    print("Error: locale '"+ localeName +"' not found.")
    print(localeName)
    exit(1)

feedPage = path +"/"+ feedPage
print("Parsing " + feedPage)

#****************************************************************************
    
#with urllib2.urlopen(feedPage) as report:
with open(feedPage) as report:

    # parse the html (with beautiful soup) into a variable
    forecast = BeautifulSoup(report, "html.parser")
    elnum = 0

    #****************************************************************************
    # get the forecast entry for today & tonight...

    for entry in forecast.find_all('entry'):
        elnum = elnum + 1
        # get the <title> tag
        titleTag =  entry.find('title')
        titleName = titleTag.text.strip()
        print(titleName)

        # get the <updated> tag
        if elnum == 1:
            updateTag = entry.find('published')
            updated = updateTag.text
            print("Updated: " + updated)

        summaryTag = entry.find('summary')
        summary = summaryTag.text
        print(summary)

#****************************************************************************
