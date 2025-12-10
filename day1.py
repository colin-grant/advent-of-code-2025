
import common.filereader as fr 
from math import floor


def first() -> None:

    lines = fr.readfile('input/dec_01_01.txt')

    pos = 50 
    counter = 0 

    for line in lines: 
        if line[0] == 'L':
            num_moves = int(line[1:])
            pos = pos - num_moves

            while pos < 0: 
                pos += 100
        elif line[0] == 'R':
            num_moves = int(line[1:]) 
            pos = (pos + num_moves) % 100 

        if pos == 0:
            counter += 1

    print(f'0 count = {counter}')    

def second() -> None:

    lines = fr.readfile('input/dec_01_01.txt')
    pos = 50 
    num_zeros = 0; 
    for line in lines:
        num_moves = int(line[1:]);
        if line[0] == 'R':
            new_pos = (pos + num_moves) % 100
            num_zeros += floor((pos + num_moves) / 100)
            pos = new_pos
            print(f"Moved Right {num_moves} pos = {pos} counter = {num_zeros}")

        elif line[0] == 'L':
            new_pos = pos - num_moves 
            if new_pos < 0: 
                new_pos = 100 - (abs(pos - num_moves) % 100)
                num_zeros += floor(((100 - pos) + num_moves) / 100)
                if pos == 0:
                    num_zeros -= 1 # fudge if we started on a zero
            else:
                if new_pos == 0:
                    num_zeros += 1
            pos = new_pos
            print(f"Moved Left {num_moves} pos = {pos} counter = {num_zeros}")

    print(f'0 count = {num_zeros}')    

def second_slow() -> None:

    lines = fr.readfile('input/dec_01_01.txt')
    pos = 50 
    num_zeros = 0; 
    inc = 0 

    for line in lines:
        num_moves = int(line[1:]);
        if line[0] == 'R':
            inc = 1 
        elif line[0] == 'L':
            inc = -1

        for _ in range(0,num_moves):
            pos += inc 

            if pos == 0 or pos == 100:
                num_zeros += 1

            if pos == -1:
                pos = 99
            if pos == 100:
                pos = 0  

        print(f"Moved {line[0]} {num_moves} pos = {pos} counter = {num_zeros}")

    print(f'0 count = {num_zeros}')    


if __name__ == "__main__": 


    first()
    second_slow() 

