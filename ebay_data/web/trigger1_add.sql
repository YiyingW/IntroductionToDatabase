-- description: <the Current_Price of an item must always match the Amount of the most recent bid for that item>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger1;
create trigger trigger1 
after insert on Bids 
begin
	update Item set Currently = new.Amount where Item_ID = new.Item_ID;
end; 
