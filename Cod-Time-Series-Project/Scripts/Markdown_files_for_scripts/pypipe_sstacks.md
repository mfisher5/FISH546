## pypipe_sstacks.py

<br>
##### Purpose
``sstacks`` is a program in the ``Stacks`` pipeline that genotypes each individual using a catalog of loci created in ``cstacks``. It creates .matches files.

##### Documentation
The most important command line arguments for ``sstacks`` are 

Here is more information on the other main command line arguments for ``sstacks``:

sstacks -b batch_id -c catalog_file -s sample_file [-s sample_file_2 ...] [-o path] [-p num_threads] [-g] [-x] [-v] [-h]
<br>p — enable parallel execution with num_threads threads.
<br>b — MySQL ID of this batch.
<br>c — TSV file from which to load the catalog loci.
<br>s — TSV file from which to load sample loci.
<br>o — output path to write results.
<br>g — base matching on genomic location, not sequence identity.
<br>x — don’t verify haplotype of matching locus.
<br>v — print program version.
<br>h — display this help messsage.


You can read the Stacks manual entry for ``sstacks`` [here](http://catchenlab.life.illinois.edu/stacks/comp/sstacks.php).

Example code:
<br>
```$	sstacks -b 3 -c stacks_b3/batch_3 -s stacks_b3/2010_213_1 -p 10```

##### Running ``sstacks`` using a custom script

I wrote a script for producing a ``sstacks`` shell script and running it. The command line arguments are [i] a text file with the names of the files that came out of ``process_radtags``, each on its own line, [ii] batch number, [iii] filepath to catalog name, [iv] filepath of input files, and [v] number of threads to use.

Example code:
<br>
```$	python pypipe_sstacks.py prd_out_filenames.txt 3 stacks_b3 stacks_b3 10```
<br>
<br>
The meat of this script:

```
# --- [A] call necessary modules

import subprocess
import sys 





# --- [B] make shell script for sstacks

trim_names = [] # initiate list

filenames = open(sys.argv[1], "r") # open file w filenames 

for line in filenames:
	name = line.strip()
	trim_name = name.rsplit(".",2)[0]
	trim_names.append(trim_name)

print trim_names # CHECK^

filenames.close()

numsamples = len(trim_names)

print "You are working with " + str(numsamples) + " samples."

newfile = open("sstacks_shell.txt", "w") # create new file for shell script

filestring = ""

for i in range(0,numsamples):
	filestring += "sstacks -b " + sys.argv[2] + " -c " + sys.argv[3]
	substr = " -s " + sys.argv[4] + "/" + trim_names[i] + " -p " + sys.argv[5] + "\n"
	filestring += substr	

# print filestring # ^CHECK

newfile.write(filestring)
newfile.close()





# --- [C] run shell script for sstacks

subprocess.call(["sh sstacks_shell.txt"], shell=True)

```

20161211NL