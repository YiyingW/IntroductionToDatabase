DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS AuctionUser;
DROP TABLE IF EXISTS Category_Belong;
DROP TABLE IF EXISTS Bids;

CREATE TABLE Item
(
	Item_ID varchar(255),
	Name varchar(255),
	Currently real,
	Buy_Price real,
	First_Bid real,
	Number_of_Bids int,
	Started timestamp,
	Ends timestamp,
	Seller_ID varchar(255),
	Description varchar(100000),
	PRIMARY KEY (Item_ID)

);

CREATE TABLE AuctionUser
(
	User_ID varchar(255),
	Rating int,
	Location varchar(255),
	Country varchar(255),
	PRIMARY KEY (User_ID)
);

CREATE TABLE Category_Belong
(
	Item_ID varchar(255),
	Category varchar(255)

);

CREATE TABLE Bids
(
	Item_ID varchar(255),
	User_ID varchar(255),
	Time_of_Bid timestamp,
	Amount real

);