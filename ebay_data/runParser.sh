#!/bin/bash
# shell script to run parser on .json files to porduce .dat files and eliminate duplicates

rm *_YW.dat  # need to remove existing .dat files 
rm Category.dat
rm Bids.dat
rm Users.dat
rm Items.dat

python YW_parser.py items-*.json

sort Category_Belong_YW.dat | uniq > Category.dat
sort Bids_YW.dat | uniq > Bids.dat
sort Users_YW.dat | uniq > Users.dat
sort Items_YW.dat | uniq > Items.dat

sed -i -e 's/"/""/g' Users.dat  # add " next to an existing "
sed -i -e 's/^/"/' Users.dat  # add " at the front of the line
sed -i -e 's/$/"/' Users.dat  # add " at the end of the line
sed -i -e 's/|/"|"/g' Users.dat  # add " around each |

sed -i -e 's/"/""/g' Items.dat  # add " next to an existing "
sed -i -e 's/^/"/' Items.dat  # add " at the front of the line
sed -i -e 's/$/"/' Items.dat  # add " at the end of the line
sed -i -e 's/|/"|"/g' Items.dat  # add " around each |