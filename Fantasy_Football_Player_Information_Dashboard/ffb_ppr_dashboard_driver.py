"""
Name: Matt Staskal
Program: Fantasy football player dashboard - Application code
The purpose of this program is to create an instance of the PlayerCard Class in a Tkinter window, which will run
the player information program
"""


from ffb_ppr_dashboard_class_definitions import *

if __name__ == '__main__':
    root = tk.Tk() # create Tkinter window
    root.geometry("850x800")
    base_card = PlayerCard(root) # instantiate instance of PlayerCard in window
    root.mainloop()
