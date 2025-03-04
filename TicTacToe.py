import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()


# def sum(a, b, c ):
#     return a + b + c

# def printBoard(xState, zState):
#     zero = 'X' if xState[0] else ('O' if zState[0] else 0)
#     one = 'X' if xState[1] else ('O' if zState[1] else 1)
#     two = 'X' if xState[2] else ('O' if zState[2] else 2)
#     three = 'X' if xState[3] else ('O' if zState[3] else 3)
#     four = 'X' if xState[4] else ('O' if zState[4] else 4)
#     five = 'X' if xState[5] else ('O' if zState[5] else 5)
#     six = 'X' if xState[6] else ('O' if zState[6] else 6)
#     seven = 'X' if xState[7] else ('O' if zState[7] else 7)
#     eight = 'X' if xState[8] else ('O' if zState[8] else 8)
#     print(f"{zero} | {one} | {two} ")
#     print(f"--|---|---")
#     print(f"{three} | {four} | {five} ")
#     print(f"--|---|---")
#     print(f"{six} | {seven} | {eight} ") 

# def checkWin(xState, zState):
#     wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for win in wins:
#         if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
#             print("X Won the match")
#             return 1
#         if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
#             print("O Won the match")
#             return 0
#     return -1
    
# if __name__ == "__main__":
#     xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     turn = 1 # 1 for X and 0 for O
#     print("Welcome to Tic Tac Toe")
#     while(True):
#         printBoard(xState, zState)
#         if(turn == 1):
#             print("X's Chance")
#             value = int(input("Please enter a value: "))
#             xState[value] = 1
#         else:
#             print("O's Chance")
#             value = int(input("Please enter a value: "))
#             zState[value] = 1
#         cwin = checkWin(xState, zState)
#         if(cwin != -1):
#             print("Match over")
#             break
        
#         turn = 1 - turn