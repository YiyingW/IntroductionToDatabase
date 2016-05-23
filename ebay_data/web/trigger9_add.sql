-- description: <auction is closed when its buy price is reached>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger9;
create trigger trigger9
before insert on Bids 
when (
	(select Currently from Item where Item.Item_ID = new.Item_ID) >= (select Buy_Price from Item where Item.Item_ID = new.Item_ID)
)
begin
	select raise(rollback, 'Auction is closed because its buy price is reached.');
end; 


