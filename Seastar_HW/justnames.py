import sys
myfile = open(sys.argv[1], "r")				
new_file = open("justnames.txt", "w") 
for line in myfile:						   
	linelist=line.strip().split(" ")		   
	new_file.write(linelist[0] + "\n")
myfile.close()
new_file.close()
