#!/bin/bash

# This script checks to see if there are any "L"s in your file names in your working directory, 
# because you use those to signify library when you have multiple lanes 
# with redundant barcodes. I have a script for adding library identifier,
# and I want to make sure I don't added the identifier more than once. 



object=($(find . -name '*L*')) # finds the first item with an L in its file name and stores it as "object"
length=${#object} # gets length of this object in characters
if [ $length -ge 1 ] # if the length of the object is more than 0, then there is a file name with an L in it
then
	echo "you added the L" # so print a notice of this
else
	echo "you haven't added the L" # if the length of the object is 0, then there isn't a filename with an L yet, so print notice
fi	

