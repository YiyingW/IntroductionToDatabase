-- description: <a user may not bid on an item he or she is also selling>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger2;
create trigger trigger2
before insert on Bids 
when new.User_ID= (select Seller_ID from Item where Item.Item_ID = new.Item_ID)
begin
	select raise(rollback, 'a user may not bid on an item he or she is also selling');
end; 
