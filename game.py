import tkinter as tk
from tkinter import messagebox
root = tk.Tk(); root.title("Tic Tac Toe")
player, btns = "X", []
def click(i):
    global player
    if btns[i]["text"]=="": btns[i]["text"]=player
    if win(): messagebox.showinfo("Win",f"{player} wins!"); reset()
    elif all(b["text"] for b in btns): messagebox.showinfo("Draw","Game Over"); reset()
    else: player="O" if player=="X" else "X"
def win():
    c=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(btns[a]["text"]==btns[b]["text"]==btns[c]["text"]!="" for a,b,c in c)
def reset():
    global player; player="X"
    for b in btns: b["text"]=""
for i in range(9):
    b=tk.Button(root,text="",font=("Arial",20),width=5,height=2,command=lambda i=i:click(i))
    b.grid(row=i//3,column=i%3); btns.append(b)
root.mainloop()
