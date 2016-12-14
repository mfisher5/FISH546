## pypipe_pstacks.py

##### Purpose
``pstacks`` is a program in the Stacks pipeline that extracts stacks of aligned reads from an alignment file, like a SAM file or bowtie files. Then, it produces the same outputs as ``ustacks``, for finding loci and calling SNPs individually.

##### Documentation

The most important command line arguments are [i] -p for number of threads, [ii] -t for file type, "sam" or "bowtie", [iii] -f for input file, [iv] -o for output filepath, [v] -i for SQL ID number, and [vi] for minimum stack depth.

Here is more information on the most important arguments for ``pstacks``:

pstacks -t file_type -f file_path [-o path] [-i id] [-m min_cov] [-p num_threads] [-h]
<br>t — input file Type. Supported types: bowtie, sam, or bam.
<br>f — input file path.
<br>o — output path to write results.
<br>i — SQL ID to insert into the output to identify this sample.
<br>m — minimum depth of coverage to report a stack (default 1).
<br>p — enable parallel execution with num_threads threads.
<br>h — display this help messsage.
<br>--pct_aln [num] — require read alignments to use at least this percentage of the read (default 85%).
<br>--keep_sec_alns — keep secondary alignments (default: false, only keep primary alignments).


Example code:
<br>
```$	pstacks -p 4 -t sam -f ../sample4.SAM -o ./scripts -i 3 -m 10```

##### Running ``pstacks`` using a custom script

I wrote a script for producing a ``pstacks`` shell script and running it. The command line arguments are [i] number of threads, [ii] file type, "sam" or "bowtie", [iii] input filepath directory, [iv] output filepath, [v] SQL ID number, [vi] min depth coverage, and [vii] text file with names of all SAM files, each on new line.

Example code:
```$	python pypipe_pstacks.py 4 sam ../ ./scripts 3 10 test_sams.txt```

The meat of the script:

```
import sys
import subprocess

namelist = []

names = open(sys.argv[7], "r")
for line in names:
	name = line.strip()
	namelist.append(name)
	
names.close()

string = ""
numnames = int(len(namelist))

for i in range(0,numnames):
	string += "pstacks -p " + sys.argv[1] + " -t " + sys.argv[2] + " -f " + sys.argv[3] + namelist[i] + " -o " + sys.argv[4] + " -i " + sys.argv[5] + " -m " + sys.argv[6] + "\n"
pstacks_shell = open("pstacks_shell.txt", "w")
pstacks_shell.write(string)
pstacks_shell.close()

subprocess.call(["sh pstacks_shell.txt"], shell = True)

print "Finished running pstacks_shell.txt script."
```

20161214NL