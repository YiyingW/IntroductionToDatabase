#!/bin/bash
# shell script to automates the process of creating database, bulk-loading the data, and adding and verifying constraints

sqlite3 AuctionBase.db < create.sql
sqlite3 AuctionBase.db < load.txt
sqlite3 AuctionBase.db < constraints_verify.sql 
sqlite3 AuctionBase.db < trigger1_add.sql 
sqlite3 AuctionBase.db < trigger2_add.sql 
sqlite3 AuctionBase.db < trigger3_add.sql 
sqlite3 AuctionBase.db < trigger4_add.sql 
sqlite3 AuctionBase.db < trigger5_add.sql 
sqlite3 AuctionBase.db < trigger6_add.sql 
sqlite3 AuctionBase.db < trigger7_add.sql 
sqlite3 AuctionBase.db < trigger8_add.sql 
