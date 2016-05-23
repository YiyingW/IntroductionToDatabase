-- description: <any new bid for a particular item must have a higher amount than any of the previous bids for that particular item>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger6;
create trigger trigger6
before insert on Bids 
when (
	new.Amount <= (
		select max(Amount) from Bids where Item_ID = new.Item_ID
	)
)
begin
	select raise(rollback, 'any new bid for a particular item must have a higher amount than any of the previous bids for that particular item');
end; 


