DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS AuctionUser;
DROP TABLE IF EXISTS Category_Belong;
DROP TABLE IF EXISTS Bids;

CREATE TABLE Item
(
	Item_ID PRIMARY KEY,
	Name,
	Currently,
	Buy_Price,
	First_Bid,
	Number_of_Bids,
	Started,
	Ends,
	Seller_ID,
	Description
);

CREATE TABLE AuctionUser
(
	User_ID PRIMARY KEY,
	Rating,
	Location,
	Country
);

CREATE TABLE Category_Belong
(
	Item_ID,
	Category

);

CREATE TABLE Bids
(
	Item_ID,
	User_ID,
	Time_of_Bid,
	Amount

);