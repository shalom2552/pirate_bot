#!/bin/bash

# print current Date
function nowDate {
	date +'%m/%d/%Y,'
}

# copy data to desktop
function copyFile {
	cp /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv ~/Desktop
	echo "$(tput setaf 2)copyed: '/Desktop/ikarim_score.csv'."
}

# preview the last 3 data rows
function tailData {
	echo -e "$(tput sgr0)Tail score:$(tput setaf 6)"
	tail -3 /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv
}

# delete the last csv row
function rmRow {
	file="/home/marshall/Documents/github/coding/ikarim/ikarim_score.csv"
	tmpFile="/home/marshall/Documents/github/coding/ikarim/tmp_score.csv"
	head -n -1 $file > $tmpFile
	cp $tmpFile $file
	rm $tmpFile
	echo -e "$(tput setaf 2)\nLast row deleted!"
}

function cancelOperation {
	echo -e "$(tput setaf 1)Operation canceld!\n"
}

# User interaction
function printRequest {
	echo -e "$(tput sgr0)\nType in the parameters values:"
	echo "Date(auto), Total, Buildings, Academic, Army, Rank"
	echo -n "$(nowDate) "
}

# Append the data observation into a data file ikarim_score.csv
function appendRow {
	echo -n -e "$(nowDate)"$Total,$Builders,$Academic,$Army,$Rank"\n" >> /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv
	echo -e "$(tput setaf 2)\nFile appended:	'/home/marshall/Documents/github/coding/ikarim/ikarim_score.csv'"
	echo -n "$(tput setaf 2)Row appended:	$(tput setaf 2)"
	tail -1 /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv
	echo "Done!"
}


# function print_changes() {
# 	OUT=$(tail -1 /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv)
# 	IFS=', ' read -r -a old_scores <<< "$OLD"
#
# 	echo "**********************"
# 	echo $old_scores
# 	echo $OUT
#
# 	# $old_Total = $Total
# 	# $old_Buildings = $Builders
# 	# $old_Academic = $Academic
# 	# $old_Army = $Army
# 	# $old_Rank = $Rank
# 	#
# 	#
# 	# $Total_D = $Total
# 	# $Buildings_D = $Builders
# 	# $Academic_D = $Academic
# 	# $Army_D = $Army
# 	# $Rank_D = $Rank
# }

# ===============================================
tailData
printRequest
# get data parameters from user
read Total Builders Academic Army Rank
# Verification
read -p "$(tput setaf 3)Are you sure? [Y/y/ENTER]: " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
	appendRow
	copyFile
else
	cancelOperation
fi
# remove last row
tailData
read -p "$(tput setaf 3)Remove last row? [Y/y/ENTER]: " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
	rmRow
else
	cancelOperation
fi

echo -e "$(tput sgr0)Tail score:$(tput setaf 6)"
tail /home/marshall/Documents/github/coding/ikarim/ikarim_score.csv
copyFile

print_changes

# ===============================================
