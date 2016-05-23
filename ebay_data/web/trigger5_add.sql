-- description: <In every auction, the Number_of_Bids attribute corresponds to the actual number of bids for that particular item.>
PRAGMA foreign_keys = ON;
drop trigger if exists trigger5;
create trigger trigger5
after insert on Bids 
begin
	update Item set Number_of_Bids = Number_of_Bids + 1 where Item_ID = new.Item_ID;
end; 


