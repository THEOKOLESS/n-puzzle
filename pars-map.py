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
        target = build_target(n)
        is_it_solvable(target, lines)
        # print(lines)
       # print(f"target offi -> {target}")
        
    else:
        print("usage : incorrect")

def is_it_solvable(target, lines):
    puzzle = make_clean_list(lines[1:])
    
    n = int(lines[0]) 
    blank = puzzle.index(0)
    blank_offi = target.index(0)
    target_blank = abs(blank - blank_offi)

    inversion = 0

    for i in range(len(target)):
        pos = target[i]
        target_pos_list = target[i:]
        target_pos_list = target_pos_list[1:]
        puzzle_pos_list = puzzle[:puzzle.index(pos)]


        for i in target_pos_list:
            inversion += puzzle_pos_list.count(i)

    if n % 2 == 1:
        if target_blank % 2 == inversion % 2:
            print(f" n -> {n} and solvable")
        else:
            print(f" n -> {n} and UNsolvable")
    else:   
        if inversion % 2 == 0:
            print(f" n -> {n} and solvable")
        else : 
            print(f" n -> {n} and UNsolvable")



    

def build_target(n):
    a = 0
    target_index = 0
    target_filler = 1
    target = ['' for _ in range(n * n)]

    while a < n:
        target_index = horizontal_up(target, target_filler, n, a, target_index)
        target_filler += n - a
        a += 1
        if a == n:
             break
        target_index = vertical_down(target, target_filler, n, a, target_index)
     
        target_filler += n - a
      
        target_index = horizontal_down(target, target_filler, n, a, target_index)
        
        target_filler += n - a
     
        a += 1
        if a == n:
            break
        target_index = vertical_up(target, target_filler, n, a, target_index)
  
        target_filler += n - a

    return target
# def list_without_empty_strings(a_list):
#      filter_object = filter(lambda x: x != "", a_list)
#      return(list(filter_object))
def horizontal_up(target, target_filler, n, a, target_index):
    for _ in range(n - a):
        if target_filler == len(target):
            target_filler = 0
        target[target_index] = target_filler
        target_index += 1
        target_filler += 1
    return target_index - 1 


def horizontal_down(target, target_filler, n, a, target_index):
    for _ in range(n - a):
        if target_filler == len(target):
            target_filler = 0
        target[target_index] = target_filler
        target_index -= 1
        target_filler += 1
    return target_index + 1

def vertical_down(target, target_filler, n, a, target_index):
    for _ in range(n - a):
        target_index = target_index + n 
        target[target_index] = target_filler
        target_filler += 1
    return target_index - 1

def vertical_up(target, target_filler, n, a, target_index):
    for _ in range(n - a):
        target_index = target_index - n 
        target[target_index] = target_filler
        target_filler += 1
    return target_index + 1
def make_clean_list(lines):
    all_nbr = []
    for line in lines:
        if re.match("^[0-9 ]+$", line):
            i = 0
            while i < len(line.split()):
                all_nbr.append(int(line.split()[i]))
                i+=1            
        else:
            print("invalid map")
            return None
    return all_nbr
        




def check_map_validity(lines):
    all_nbr = []
    check_validity_nbr = 0
    j = 0
    if re.match("^[0-9 ]+$", lines[0]):
        n = int(lines[0])
        nxn = n * n
        #print(f"{lines[1:]} -> lines")
        if n >= 3 and len(lines) - 1 == n: #puzzle and row number are coherent
             all_nbr = make_clean_list(lines[1:])
             if all_nbr == None:
                exit() 
        else:
            print("invalid map")
            exit()
   # print(f"{all_nbr} -> all_nbr")
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

    #print(f"start -> {all_nbr}")
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