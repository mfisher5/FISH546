## Adding library identifiers to filenames

When analyzing data from multiple lanes that have redundant barcodes, it may be helpful to add a library identifier to the filename. I wrote a script to do this by adding "\_L1" or "_L2" to the end of the filename, before the file extensions.

##### [1] Checking to see if you've added a library identifier

You can use the following bash script to see whether there is already an "L" in any of the filenames in a given directory. This is useful because the script I wrote for adding the library identifier will add one even if there already has been one added, leading to annoying naming problems like filename_L1_L1_L1, etc.

```
object=($(find . -name '*L*')) # finds the first item with an L in its file name and stores it as "object"
length=${#object} # gets length of this object in characters
if [ $length -ge 1 ] # if the length of the object is more than 0, then there is a file name with an L in it
then
	echo "At least one of your filenames already as an L in it. Check your filenames before adding a library identifier." # so print a notice of this
else
	echo "None of your filenames have an L in them. It is safe to add a library identifier." # if the length of the object is 0, then there isn't a filename with an L yet, so print notice
fi
```

I also wrote a bash script that will tell you if there is a letter "L" in the filename, to see whether you have already added a library identifier.

```
# arguments
# [1] directory name with files to rename 
# [2] text you would like to add to the end of each filename before file extensions

# assumptions
# [1] file extention = fq.qz
# [2] you are one directory above the directory that you want to rename the files of
# [3] your files aren't already renamed! --- write an if else loop to make sure it hasn't been run yet when you have the time

import sys
import subprocess

# make a text file that has each thing in this directory on a line; each line should be each file in the lane

string1 = "" # initiate string

string1 += 'ls ' + sys.argv[1] + ' > ./dircontents.txt' # add ls, wd, redirect to text file

firstshell = open("getcontents_shell.txt", "w")
firstshell.write(string1)
firstshell.close()

subprocess.call(["sh getcontents_shell.txt"], shell = True)

# now that file is made for contents of directory, read that file in
contents = open("dircontents.txt", "r")


# second shell = renaming script
rename_w_lib_shell = open("rename_w_lib_shell.txt", "w")

string2 = ""
string2 += "cd " + sys.argv[1] + "\n"


# loop that will break the script if it's already run to make sure you don't rename files into something wrong!
for line in contents:
	linelist = line.strip().split(".")
	if linelist[0][-4] == "L":
		print "CHECK TO SEE IF YOU HAVE ALREADY RENAMED THESE FILES. SCRIPT PAUSED AS WARNING BECAUSE FILES APPEAR RENAMED."
		sys.exit() # exit script
	else:
		continue
contents.close()



contents = open("dircontents.txt", "r")
for line in contents:
	original = line.strip()
	filename_list = line.strip().split(".") # make list out of whole file name with extensions
	filename_wo_ext = filename_list[0]
	file_ext = "." + filename_list[1] + "." + filename_list[2]
	wordlist = filename_wo_ext.split("_") # split filename without extensions into parts by underscore
	newfilename = wordlist[0] + sys.argv[2] + "_" + wordlist[1]
	newfilename += file_ext
	string2 += "mv" + "\t" + original + "\t" + newfilename + "\n"

rename_w_lib_shell.write(string2)
rename_w_lib_shell.close()
contents.close()

# call renaming shell script
subprocess.call(["sh rename_w_lib_shell.txt"], shell = True)
```


20161211NL

