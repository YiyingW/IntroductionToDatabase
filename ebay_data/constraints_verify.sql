SELECT * FROM Item WHERE NOT EXISTS (SELECT * FROM AuctionUser WHERE Item.Seller_ID = AuctionUser.User_ID);
SELECT * FROM Category_Belong WHERE NOT EXISTS (SELECT * FROM Item WHERE Item.Item_ID = Category_Belong.Item_ID);
SELECT * FROM Bids WHERE NOT EXISTS (SELECT * FROM AuctionUser WHERE Bids.User_ID = AuctionUser.User_ID);
SELECT * FROM Bids WHERE NOT EXISTS (SELECT * FROM Item WHERE Item.Item_ID = Bids.Item_ID);