#!/bin/bash

# This script checks to see if there are any "L"s in your file names in your working directory, 
# because you use those to signify library when you have multiple lanes 
# with redundant barcodes. I have a script for adding library identifier,
# and I want to make sure I don't added the identifier more than once. 



object=($(find . -name '*L*')) # finds the first item with an L in its file name and stores it as "object"
length=${#object} # gets length of this object in characters
if [ $length -ge 1 ] # if the length of the object is more than 0, then there is a file name with an L in it
then
	echo "At least one of your filenames already as an L in it. Check your filenames before adding a library identifier." # so print a notice of this
else
	echo "None of your filenames have an L in them. It is safe to add a library identifier." # if the length of the object is 0, then there isn't a filename with an L yet, so print notice
fi	

