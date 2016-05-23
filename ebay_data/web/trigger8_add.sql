-- description: <the current time of your AuctionBase system can only advance forward, not backward in time>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger8;
create trigger trigger8
before update on CurrentTime
when (
	new.ct < old.ct
)
begin
	select raise(rollback, 'the current time of your AuctionBase system can only advance forward, not backward in time');
end; 


