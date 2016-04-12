
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

parseJSON function filled by Yiying Wang.
Modified: 04/2016

Skeleton parser for CS145 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            ItemID = item['ItemID']
            # Create Category_Belong.dat file
            
            with open('Category_Belong_YW.dat','a') as f_Category_Belong:
                for category in item['Category']:
                	f_Category_Belong.write(ItemID + columnSeparator + category + "\n")
            

            # Create Bids.dat file 
            with open('Bids_YW.dat','a') as f_bids:
                if item['Bids'] != None:
                	for individual_bid in item['Bids']:
                		f_bids.write(str(ItemID) + columnSeparator + str(individual_bid['Bid']['Bidder']['UserID']) + columnSeparator \
               			+ str(transformDttm(individual_bid['Bid']['Time'])) + columnSeparator + str(transformDollar(individual_bid['Bid']['Amount'])) + "\n")
            
            # Create Users.dat file
            # append seller's information, including UserID, Rating, Location and Country 
            # append all the bidders information into Users.dat file, if Location and Country not available use 'NULL' instead
            # Note: This Users.dat file needs to remove duplicates later
            with open('Users_YW.dat', 'a') as f_users:
                f_users.write(item['Seller']['UserID'] + columnSeparator + item['Seller']['Rating'] + \
                	columnSeparator + item['Location'] + columnSeparator + item['Country'] + '\n')
                if item['Bids'] != None:
                    for individual_bid in item['Bids']:
                        bidder_info = individual_bid['Bid']['Bidder']
                        Location = 'default'
                        Country = 'default'
                        if 'Location' not in bidder_info.keys():
                            Location = 'NULL'
                        if 'Country' not in bidder_info.keys():
                            Country = 'NULL'
                        bidder_ID = bidder_info['UserID']
                        bidder_rating = bidder_info['Rating']
                        if Location != 'NULL':
                            Location = bidder_info['Location']
                        if Country != 'NULL':
                            Country = bidder_info['Country']
                        f_users.write(bidder_ID + columnSeparator + bidder_rating + columnSeparator + Location + columnSeparator + Country + "\n")            	
            
            
            # Create items.dat file
            with open('Items_YW.dat', 'a') as f_items:
            	Name = item['Name']
            	Currently = transformDollar(item['Currently'])          	
            	if 'Buy_Price' in item.keys():
            	    Buy_Price = transformDollar(item['Buy_Price'])
            	else:
            		Buy_Price = 'NULL'
                
                First_Bid = transformDollar(item['First_Bid'])
                Number_of_Bids = item['Number_of_Bids']
                Started = transformDttm(item['Started'])
                Ends = transformDttm(item['Ends'])
                Seller_ID = item['Seller']['UserID']
                if item['Description'] !=  None:
                    Description = item['Description']
                else:
                	Description = 'NULL'
                f_items.write(ItemID + columnSeparator + Name + columnSeparator + Currently + columnSeparator + \
                	Buy_Price + columnSeparator + First_Bid + columnSeparator + Number_of_Bids + columnSeparator + \
                	Started + columnSeparator + Ends + columnSeparator + Seller_ID + columnSeparator + Description + '\n')


"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)
