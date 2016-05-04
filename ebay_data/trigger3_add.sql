-- description: <no auction may have two bids at the exact same time>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger3;
create trigger trigger3
before insert on Bids 
when (
	new.Time_of_Bid in (select Time_of_Bid from Bids where new.Item_ID = Item_ID)	
)
begin
	select raise(rollback, 'no auction may have two bids at the exact same time');
end; 


