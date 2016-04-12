import sys
from json import loads
from re import sub



# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

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


json_file = 'items-0.json'
with open(json_file, 'r') as f:
	items = loads(f.read())['Items']

for i in range(0, 200):
	if 'Buy_Price' in items[i].keys():
		print items[i]['Buy_Price']
		print i 

# create Users.dat file
'''
for item in items:

	with open('test_users.dat', 'a') as test_users:
		test_users.write(item['Seller']['UserID'] + "|" + item['Seller']['Rating'] \
			+ "|" + item["Location"] + "|" + item['Country']+"\n")
		if item['Bids'] != None:
			for individual_bid in item['Bids']:
				bidder_info = individual_bid['Bid']['Bidder']
				Location = "default"
				Country = "default"
				if "Location" not in bidder_info.keys():
					Location = 'NULL'
				if "Country" not in bidder_info.keys():
					Country = 'NULL'
				bidder_ID = bidder_info['UserID']
				bidder_rating = bidder_info['Rating']
				if Location != 'NULL':
					Location = bidder_info['Location']
				if Country != 'NULL':
					Country = bidder_info['Country']
				test_users.write(bidder_ID + "|" + bidder_rating + "|" + Location + "|" + Country + "\n")
'''



