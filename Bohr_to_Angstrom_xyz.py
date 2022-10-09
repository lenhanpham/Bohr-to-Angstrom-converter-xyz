#!/usr/bin/env python3
import sys

FACTOR = 0.52917721067   # Bohr to Angstrom 
#FACTOR = 1.8897268777744 # Angstrom to Bohr 

def get_lines(filename):

    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines

def coordlines_to_data(line):

    coorItems = line.split()

    x = float(coorItems[1]) * FACTOR
    y = float(coorItems[2]) * FACTOR
    z = float(coorItems[3]) * FACTOR
    atom_type = coorItems[0] 
    if   atom_type ==   "1" : atom_type = "H "
    elif atom_type ==   "2" : atom_type = "He"
    elif atom_type ==   "3" : atom_type = "Li"
    elif atom_type ==   "4" : atom_type = "Be"
    elif atom_type ==   "5" : atom_type = "B "
    elif atom_type ==   "6" : atom_type = "C "
    elif atom_type ==   "7" : atom_type = "N "
    elif atom_type ==   "8" : atom_type = "O "
    elif atom_type ==   "9" : atom_type = "F "
    elif atom_type ==  "10" : atom_type = "Ne"
    elif atom_type ==  "11" : atom_type = "Na"
    elif atom_type ==  "12" : atom_type = "Mg"
    elif atom_type ==  "13" : atom_type = "Al"
    elif atom_type ==  "14" : atom_type = "Si"
    elif atom_type ==  "15" : atom_type = "P "
    elif atom_type ==  "16" : atom_type = "S "
    elif atom_type ==  "17" : atom_type = "Cl"
    elif atom_type ==  "18" : atom_type = "Ar"
    elif atom_type ==  "19" : atom_type = "K "
    elif atom_type ==  "20" : atom_type = "Ca"
    elif atom_type ==  "21" : atom_type = "Sc"
    elif atom_type ==  "22" : atom_type = "Ti"
    elif atom_type ==  "23" : atom_type = "V "
    elif atom_type ==  "24" : atom_type = "Cr"
    elif atom_type ==  "25" : atom_type = "Mn"
    elif atom_type ==  "26" : atom_type = "Fe"
    elif atom_type ==  "27" : atom_type = "Co"
    elif atom_type ==  "28" : atom_type = "Ni"
    elif atom_type ==  "29" : atom_type = "Cu"
    elif atom_type ==  "30" : atom_type = "Zn"
    elif atom_type ==  "31" : atom_type = "Ga"
    elif atom_type ==  "32" : atom_type = "Ge"
    elif atom_type ==  "33" : atom_type = "As"
    elif atom_type ==  "34" : atom_type = "Se"
    elif atom_type ==  "35" : atom_type = "Br"
    elif atom_type ==  "36" : atom_type = "Kr"
    elif atom_type ==  "37" : atom_type = "Rb"
    elif atom_type ==  "38" : atom_type = "Sr"
    elif atom_type ==  "39" : atom_type = "Y "
    elif atom_type ==  "40" : atom_type = "Zr"
    elif atom_type ==  "41" : atom_type = "Nb"
    elif atom_type ==  "42" : atom_type = "Mo"
    elif atom_type ==  "43" : atom_type = "Tc"
    elif atom_type ==  "44" : atom_type = "Ru"
    elif atom_type ==  "45" : atom_type = "Rh"
    elif atom_type ==  "46" : atom_type = "Pd"
    elif atom_type ==  "47" : atom_type = "Ag"
    elif atom_type ==  "48" : atom_type = "Cd"
    elif atom_type ==  "49" : atom_type = "In"
    elif atom_type ==  "50" : atom_type = "Sn"
    elif atom_type ==  "51" : atom_type = "Sb"
    elif atom_type ==  "52" : atom_type = "Te"
    elif atom_type ==  "53" : atom_type = "I "
    elif atom_type ==  "54" : atom_type = "Xe"
    elif atom_type ==  "55" : atom_type = "Cs"
    elif atom_type ==  "56" : atom_type = "Ba"
    elif atom_type ==  "57" : atom_type = "La"
    elif atom_type ==  "58" : atom_type = "Ce"
    elif atom_type ==  "59" : atom_type = "Pr"
    elif atom_type ==  "60" : atom_type = "Nd"
    elif atom_type ==  "61" : atom_type = "Pm"
    elif atom_type ==  "62" : atom_type = "Sm"
    elif atom_type ==  "63" : atom_type = "Eu"
    elif atom_type ==  "64" : atom_type = "Gd"
    elif atom_type ==  "65" : atom_type = "Tb"
    elif atom_type ==  "66" : atom_type = "Dy"
    elif atom_type ==  "67" : atom_type = "Ho"
    elif atom_type ==  "68" : atom_type = "Er"
    elif atom_type ==  "69" : atom_type = "Tm"
    elif atom_type ==  "70" : atom_type = "Yb"
    elif atom_type ==  "71" : atom_type = "Lu"
    elif atom_type ==  "72" : atom_type = "Hf"
    elif atom_type ==  "73" : atom_type = "Ta"
    elif atom_type ==  "74" : atom_type = "W "
    elif atom_type ==  "75" : atom_type = "Re"
    elif atom_type ==  "76" : atom_type = "Os"
    elif atom_type ==  "77" : atom_type = "Ir"
    elif atom_type ==  "78" : atom_type = "Pt"
    elif atom_type ==  "79" : atom_type = "Au"
    elif atom_type ==  "80" : atom_type = "Hg"
    elif atom_type ==  "81" : atom_type = "Tl"
    elif atom_type ==  "82" : atom_type = "Pb"
    elif atom_type ==  "83" : atom_type = "Bi"
    elif atom_type ==  "84" : atom_type = "Po"
    elif atom_type ==  "85" : atom_type = "At"
    elif atom_type ==  "86" : atom_type = "Rn"
    elif atom_type ==  "87" : atom_type = "Fe"
    elif atom_type ==  "88" : atom_type = "Ra"
    elif atom_type ==  "89" : atom_type = "Ac"
    elif atom_type ==  "90" : atom_type = "Th"
    elif atom_type ==  "91" : atom_type = "Pa"
    elif atom_type ==  "92" : atom_type = "U "
    elif atom_type ==  "93" : atom_type = "Np"
    elif atom_type ==  "94" : atom_type = "Pu"
    elif atom_type ==  "95" : atom_type = "Am"
    elif atom_type ==  "96" : atom_type = "Cm"
    elif atom_type ==  "97" : atom_type = "Bk"
    elif atom_type ==  "98" : atom_type = "Cf"
    elif atom_type ==  "99" : atom_type = "Es"
    elif atom_type == "100" : atom_type = "Fm"
    elif atom_type == "101" : atom_type = "Md"
    elif atom_type == "102" : atom_type = "No"
    elif atom_type == "103" : atom_type = "Lr"
    elif atom_type == "104" : atom_type = "Rf"
    elif atom_type == "105" : atom_type = "Db"
    elif atom_type == "106" : atom_type = "Sg"
    elif atom_type == "107" : atom_type = "Bh"
    elif atom_type == "108" : atom_type = "Hs"
    elif atom_type == "109" : atom_type = "Mt"
    elif atom_type == "110" : atom_type = "Ds"
    elif atom_type == "111" : atom_type = "Rg"
    elif atom_type == "112" : atom_type = "Cn"
    elif atom_type == "113" : atom_type = "Uut"
    elif atom_type == "114" : atom_type = "Fl"
    elif atom_type == "115" : atom_type = "Uup"
    elif atom_type == "116" : atom_type = "Lv"
    elif atom_type == "117" : atom_type = "Uus"
    elif atom_type == "118" : atom_type = "Uuo"
    else : atom_type = atom_type.title() 
    return (atom_type, x, y, z)


if __name__ == "__main__":

    coord_filename = sys.argv[1]

    lines = get_lines(coord_filename)

    print(len(lines) - 2)
    print("xyz Cartesian Coordinate in Angstrom generated from file:", coord_filename)
    #print(lines[0], end = "")
    for line in lines[2:]:
        (atom_type, x, y, z) = coordlines_to_data(line)
        print(" %-2s    %20.12f %20.12f %20.12f" % (atom_type, x, y, z))

