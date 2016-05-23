import web
from datetime import datetime

db = web.database(dbn='sqlite',
        db='AuctionBase.db' #TODO: add your SQLite database filename
    )

######################BEGIN HELPER METHODS######################

# Enforce foreign key constraints
# WARNING: DO NOT REMOVE THIS!
def enforceForeignKey():
    db.query('PRAGMA foreign_keys = ON')

# initiates a transaction on the database
def transaction():
    return db.transaction()
# Sample usage (in auctionbase.py):
#
# t = sqlitedb.transaction()
# try:
#     sqlitedb.query('[FIRST QUERY STATEMENT]')
#     sqlitedb.query('[SECOND QUERY STATEMENT]')
# except Exception as e:
#     t.rollback()
#     print str(e)
# else:
#     t.commit()
#
# check out http://webpy.org/cookbook/transactions for examples

# returns the current time from your database
def getTime():
    # TODO: update the query string to match -- Done!
    # the correct column and table name in your database
    query_string = 'select ct from CurrentTime'
    results = query(query_string)
    # alternatively: return results[0]['currenttime']
    return results[0].ct # TODO: update this as well to match the
                                  # column name -- Done!

# returns a single item specified by the Item's ID in the database
# Note: if the `result' list is empty (i.e. there are no items for a
# a given ID), this will throw an Exception!
def getItemById(item_id):
    # TODO: rewrite this method to catch the Exception in case `result' is empty -- Done!
    t = transaction()
    try:
        query_string = 'select * from Item where Item_ID = $itemID'
        result = query(query_string, {'itemID': item_id})
        
    except Exception as e:
        t.rollback()
    else:
        t.commit()
        return result

def getItem(itemID, userID, Category, Description, minPrice, maxPrice, status):
    t = transaction()
    if itemID != '':
        query_string = 'select * from Item where Item_ID=$itemID'
    else:
        query_string ='select * from Item where'
        count = 0
        if userID != '':
            query_string += ' Seller_ID=$userID'
            count += 1
        if Description != '':
            if count > 0:
                query_string += " AND Description LIKE "+"'%" +Description+"%'"
                count += 1
            else:
                query_string += " Description LIKE "+"'%" +Description+"%'"
                count += 1
        if minPrice != '' and maxPrice != '':
            if count > 0:
                query_string += " AND Buy_Price<=$maxPrice AND Buy_Price>=$minPrice"
                count += 1
            else:
                query_string+= " Buy_Price<=$maxPrice AND Buy_Price>=$minPrice"
                count += 1
        elif minPrice == '' and maxPrice != '':
            if count > 0:
                query_string += " AND Buy_Price<=$maxPrice"
                count += 1
            else:
                query_string+= " Buy_Price<=$maxPrice"
                count += 1 
        elif minPrice != '' and maxPrice == '':
            if count > 0:
                query_string += " AND Buy_Price>=$minPrice"
                count += 1
            else:
                query_string+= " Buy_Price>=$minPrice"
                count += 1 
        if Category != '':
            if count > 0:
                query_string += " AND Item_ID IN (select Item_ID from Category_Belong where Category = $Category)"
                count += 1
            else:
                query_string += " Item_ID IN (select Item_ID from Category_Belong where Category = $Category)"
                count += 1
        currtime = getTime()
        if status == 'close':
            if count == 0:
                query_string += " Ends <= " + "'"+currtime+"'" + " or Currently >= Buy_Price"
                count += 1
            else:
                query_string += " AND (Ends <= " + "'"+currtime+"'" + " or Currently >= Buy_Price)"
                count += 1
        elif status == 'open':
            if count == 0:
                query_string += " ((typeof(Buy_Price) != 'float' and Ends >"+ "'"+currtime+"'" + " AND Started <=" + "'"+currtime+"')"
                query_string += " or (Ends > " + "'"+currtime+"'" + " AND Currently < Buy_Price)" + " AND Started <=" + "'"+currtime+"')"
                count += 1
            else:
                query_string += " AND ((typeof(Buy_Price) != 'float' and Ends >"+ "'"+currtime+"'" + " AND Started <=" + "'"+currtime+"')" 
                query_string += " or (Ends > " + "'"+currtime+"'" + " AND Currently < Buy_Price)" + " AND Started <=" + "'"+currtime+"')"
                count += 1  
        elif status == 'notStarted':
            if count == 0:
                query_string += " Started > " + "'"+currtime+"'"
                count += 1
            else:
                query_string += " AND Started > " + "'"+currtime+"'" 
                count += 1     

    try:
        result = query(query_string, {'itemID': itemID, 'userID': userID, 'Description': Description, 'minPrice': minPrice, 'maxPrice': maxPrice, 'Category': Category, 'status': status})
    except Exception as e:
        t.rollback()
    else:
        t.commit()
        return result

def getBid(itemID):  # get the bid details given an itemID
    t = transaction()
    query_string = "select User_ID, Time_of_Bid, Amount from Bids where Item_ID=$itemID"
    try:
        result = query(query_string, {'itemID': itemID})
    except Exception as e:
        t.rollback()
    else:
        t.commit()
        return result

def string_to_time(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def getStatus(itemID):  # get the status of an item, open or closed
    t = transaction()
    query_string = "select Currently, Buy_Price, Started, Ends from Item where Item_ID = $itemID"
    try:
        result = query(query_string, {'itemID': itemID})
    except Exception as e:
        t.rollback()
    else:
        t.commit()

    currently = result[0]['Currently']
    Buy_Price = result[0]['Buy_Price']
    Started = result[0]['Started']
    Ends = result[0]['Ends']
    currtime = string_to_time(getTime())

    if Buy_Price == None and currtime < Ends:
        return 'open'
    elif currently >= Buy_Price or Ends <= currtime:
        return 'closed'
    elif currtime < Started:
        return 'not started'
    else:
        return 'open'
def getWinner(itemID):
    t = transaction()
    query_string = 'select User_ID from Bids where Item_ID = $itemID AND Amount = (select MAX(Amount) from Bids where Item_ID=$itemID)'
    try:
        result = query(query_string, {'itemID': itemID})
    except Exception as e:
        t.rollback()
    else:
        t.commit()
    if len(result) ==1:
        return result[0].User_ID
    else:
        return 'Auction closed but no winner.'




# wrapper method around web.py's db.query method
# check out http://webpy.org/cookbook/query for more info
def query(query_string, vars = {}):
    return list(db.query(query_string, vars))

#####################END HELPER METHODS#####################

#TODO: additional methods to interact with your database,
# e.g. to update the current time
