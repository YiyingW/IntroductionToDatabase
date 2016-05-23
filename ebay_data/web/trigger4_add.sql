-- description: <no auction may have a bid before its start time or after its end time>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger4;
create trigger trigger4
before insert on Bids 
when (
	new.Time_of_Bid < (
		select Started from Item where Item_ID = new.Item_ID
	) or new.Time_of_Bid > (
		select Ends from Item where Item_ID = new.Item_ID
	)
)
begin
	select raise(rollback, 'no auction may have a bid before its start time or after its end time');
end; 


