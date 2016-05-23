-- description: <all new bids must be placed at the time which matches the current time of your AuctionBase system>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger7;
create trigger trigger7
before insert on Bids 
when (
	new.Time_of_Bid <> (select ct from CurrentTime)
)
begin
	select raise(rollback, 'all new bids must be placed at the time which matches the current time of your AuctionBase system');
end; 


