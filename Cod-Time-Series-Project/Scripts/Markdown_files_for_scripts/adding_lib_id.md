## Adding library identifiers to filenames

When analyzing data from multiple lanes that have redundant barcodes, it may be helpful to add a library identifier to the filename. I wrote a script to do this by adding "\_L1" or "_L2" to the end of the filename, before the file extensions.

##### [1] Checking to see if you've added a library identifier

You can use the following bash [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/check_lib_id.sh) to see whether there is already an "L" in any of the filenames in a given directory. This is useful because the script I wrote for adding the library identifier will add one even if there already has been one added, leading to annoying naming problems like filename_L1_L1_L1, etc. Also, this script assumes you're working with zipped fastq files, with file extensions .fq.gz, and that you want the filename followed by the library identifier followed by forward or reverse identifier (e.g., 2005_131_L1_1.fq.gz).

Navigate to the directory of files that you want to check for library identifiers. Then run the script.

Example code:
<br>
```
$	python check_lib_id.sh
```

Meat of the script:

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

##### [2] Adding library identifier

I wrote a custom [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/add_lib_to_filename.py) that will add a library identifier like\"_L1" or "_L2" to your filenames. 

Example code:
<br>
```
$	python add_lib_to_filename.py ../lane1/process_radtags_out _L1 
```

<br>
Meat of the script:

```
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