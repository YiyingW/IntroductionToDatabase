--select User_ID from Bids
--where Item_ID = 1679234611 AND Amount = (select MAX(Amount) from Bids where Item_ID = 1496248160);
--select * from Bids where Item_ID = 1496248160;

--select Item_ID from Item where (typeof(Buy_Price) != 'float' and Ends > '2001-12-25 12:00:00') or (Ends > '2001-12-25 12:00:00' and Currently < Buy_Price);

select * from Bids where Item_ID = 1496908302;
select * from Item where Item_ID = 1496908302;