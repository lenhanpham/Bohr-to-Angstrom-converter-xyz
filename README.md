# Unit converter from Bohr to Angstrom and vice versa  
It is boring to convert xyz Cartesian cooridantes of chemical systems from Bohr to Angstrom and vice versa, use this script to do jobs automatically.
Place all xyz coordinates to be converted to a directory, and then run the script "Coordinate-converter.shell" by typing "bash Coordinate-converter.shell".
All original coordinates of Bohr units will be copied to a directory called original.

If you want to convert only one xyz file from Bohr to Angstrom, just type "python3 Bohr_to_Angstrom_xyz.py your_xyz_file.xyz"

The reverse conversion from Angstrom to Bohr can be done easily by changing the converting factor in the python script.

### The code was written in python 3, so Python 3 should be used 

### The script will automaticaly convert all atoms represented by atomic numbers to element names, such as 6 to C, 8 to O, and so on. 

