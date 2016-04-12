#!/bin/bash
# shell script to run parser on .json files to porduce .dat files and eliminate duplicates

rm *_YW.dat  # need to remove existing .dat files 
python YW_parser.py items-*.json

sort Category_Belong_YW.dat | uniq > Category.dat
sort Bids_YW.dat | uniq > Bids.dat
sort Users_YW.dat | uniq > Users.dat
sort Items_YW.dat | uniq > Items.dat