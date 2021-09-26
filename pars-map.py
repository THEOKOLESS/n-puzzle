#!/usr/bin/env python
import sys
import re

def main():
    lines = []
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
        lines = clear_comments(lines)
        check_map_validity(lines)

        #print(f"YYYEEEES {lines}")
        
    else:
        print("usage : incorrect")

def check_map_validity(lines):
    count = 0
    all_nbr = []
    check_validity_nbr = 0
    j = 0
    if re.match("^[0-9 ]+$", lines[0]):
        n = int(lines[0])
        nxn = n * n
       
        if n >= 3 and len(lines) - 1 == n: #puzzle and row number are coherent
            for line in lines:
                if count > 0:
                    if re.match("^[0-9 ]+$", line):
                        i = 0
                        while i < len(line.split()):
                            all_nbr.append(int(line.split()[i]))
                            i+=1
                        #print(line)
                    else:
                        print("invalid map")
                        exit() 
                count += 1
        else:
            print("invalid map")
            exit() 
    if len(all_nbr) == len(set(all_nbr)) and len(all_nbr) == nxn: # pas de doublons et colones ok
        while j < nxn - 1:
            j+=1
            check_validity_nbr +=   j
        if check_validity_nbr != sum(all_nbr):
            print("invalid map")
            exit()
    else:
        print("invalid map")
        exit() 
    #         print (f"{check_validity_nbr}, {j}" )

    print(all_nbr)
    # print(sum(all_nbr))

def clear_comments(lines):
    ret = []
    for line in lines:
        new_line = line.split("#")
        if len(new_line) > 1:
            if new_line[0] != '':
                ret.append(new_line[0].strip()) 
        elif len(new_line) == 1:
            #print(f" LINE IN THE LOOP -> {new_line}")
            ret.append(new_line[0].strip()) 
    return ret

if __name__ == "__main__":
    main()