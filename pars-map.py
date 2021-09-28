#!/usr/bin/env python
import sys
import re

def main():
    lines = []
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as f:
                lines = f.readlines()
        except : 
            print(f"impossible d'ouvrir {sys.argv[1]}")
            exit()
        lines = clear_comments(lines)
        n = check_map_validity(lines)
        #print(f"n -> {n}")

        target = build_target(n) 
        print(f"target offi -> {target}")
        #print(f"YYYEEEES {lines}")
        
    else:
        print("usage : incorrect")
def build_target(n):
    # i = 0
    a = 0
    # b = 1
    # j = 2
    target_index = 0
    target_filler = 1
    target = ['' for i in range(n * n)]

    # while i < n:
    # for i in range(n):
    #     target[i] = target_filler
    #     target_filler += 1
        # i += 1
    # for x in range(n - a):
    #     target[n * j - b] = target_filler
    #     j+=1
    #     target_filler += 1
    # b += 1 
    # j -= 1
    # for x in range(n - a):
    #     test = (n * j) - x - b
    #     print(f"test->{test}")
    #     target[test] = target_filler
    #     target_filler += 1
    # a += 1
    # b += n - a
    # for x in range(n - a):
    #     j -= 1
    #     test = (n * j) - b 
    #     print(f"test2->{test}")
    #     target[test] = target_filler
    #     target_filler += 1
    # # a += 1
    # for x in range(n - a):
    #     target[test + x + 1] = target_filler
    #     target_filler += 1
    while target_filler <  len(target):
        target_index = horizontal_up(target, target_filler, n, a, target_index)
        target_filler += n - a
        a += 1
        
 

        target_index = vertical_down(target, target_filler, n, a, target_index)
        target_filler += n - a
      
        target_index = horizontal_down(target, target_filler, n, a, target_index)
        target_filler += n - a
     
        a += 1
        target_index = vertical_up(target, target_filler, n, a, target_index)
        target_filler += n - a
     
        print(f"target -> {target} target_filler -> {target_filler} target_index -> {target_index}")
        break

        # break
        # horizontal_down()
        # vertical_up()
        # horizontal_up()


        # for x in range(n - a):
        #     target_index = n * j - b
        #     target[target_index] = target_filler
        #     j+=1
        #     target_filler += 1
    return target
def horizontal_up(target, target_filler, n, a, target_index):
    for x in range(n - a):
       
        if target_filler == len(target):
            target_filler = 0
        target[target_index] = target_filler
        target_index += 1
        target_filler += 1
    return target_index - 1 


def horizontal_down(target, target_filler, n, a, target_index):
    for x in range(n - a):
        if target_filler == len(target):
            target_filler = 0
        # print(target_index)
        target[target_index] = target_filler
        target_index -= 1
        target_filler += 1
    return target_index + 1
def vertical_down(target, target_filler, n, a, target_index):
    # j = 1
    for x in range(n - a):
        target_index = target_index + n 
        target[target_index] = target_filler

        # j+=1
        target_filler += 1
    return target_index - 1
def vertical_up(target, target_filler, n, a, target_index):
    for x in range(n - a):
        target_index = target_index - n 
        target[target_index] = target_filler
        target_filler += 1
    return target_index

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
            check_validity_nbr += j
        if check_validity_nbr != sum(all_nbr):
            print("at least one number is akward")
            exit()  
    else:
        print("col not right or same number")
        sys.exit() 
    #         print (f"{check_validity_nbr}, {j}" )

    print(f"start -> {all_nbr}")
    return n
    # print(sum(all_nbr))

def clear_comments(lines):
    ret = []
    for line in lines:
        new_line = line.split("#")
        if len(new_line) >= 1:
            if new_line[0] != '':
                ret.append(new_line[0].strip()) 
    return ret

if __name__ == "__main__":
    main()