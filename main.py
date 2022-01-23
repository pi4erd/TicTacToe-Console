import os
from random import randint

a = [[0]*3 for _ in range(3)]
def sf(s):
    l = [' ', 'x', 'o']
    return l[s]
def render_mtx(m):
    print(f"""{sf(m[0][0])}|{sf(m[1][0])}|{sf(m[2][0])}
{sf(m[0][1])}|{sf(m[1][1])}|{sf(m[2][1])}
{sf(m[0][2])}|{sf(m[1][2])}|{sf(m[2][2])}
""")

def ai_output():
    x = randint(0, 2)
    y = randint(0, 2)
    while a[x][y] != 0:
        x = randint(0, 2)
        y = randint(0, 2)
    a[x][y] = 2

def check_win_o():
    cols = a[0][0] == a[0][1] == a[0][2] == 2 or \
        a[1][0] == a[1][1] == a[1][2] == 2 or \
        a[2][0] == a[2][1] == a[2][2] == 2
    rows = a[0][0] == a[1][0] == a[2][0] == 2 or \
        a[0][1] == a[1][1] == a[2][1] == 2 or \
        a[0][2] == a[1][2] == a[2][2] == 2
    diags = a[0][0] == a[1][1] == a[2][2] == 2 or \
        a[0][2] == a[1][1] == a[2][0] == 2
    return cols or rows or diags
def check_win_x():
    cols = a[0][0] == a[0][1] == a[0][2] == 1 or \
        a[1][0] == a[1][1] == a[1][2] == 1 or \
        a[2][0] == a[2][1] == a[2][2] == 1
    rows = a[0][0] == a[1][0] == a[2][0] == 1 or \
        a[0][1] == a[1][1] == a[2][1] == 1 or \
        a[0][2] == a[1][2] == a[2][2] == 1
    diags = a[0][0] == a[1][1] == a[2][2] == 1 or \
        a[0][2] == a[1][1] == a[2][0] == 1
    return cols or rows or diags

def clr_scr():
    os.system("cls")
def player_input():
    win = False
    while True:
        try:
            clr_scr()
            render_mtx(a)
            print("You are 'x'\n")
            x = int(input("Выберите столбец (1-3): "))-1
            y = int(input("Выберите строку (1-3): "))-1
            if a[x][y] != 0:
                raise ValueError
        
            a[x][y] = 1
            xw = check_win_x()
            ow = check_win_o()

            if xw or ow:
                clr_scr()
                txt = "x Won!" if xw else "o Won!"
                render_mtx(a)
                print(txt)
                break

            ai_output()
        except ValueError:
            clr_scr()
            print("That wasn't valid input. Try again!")
            input()

player_input()
input() # dull input to prevent from instant exit