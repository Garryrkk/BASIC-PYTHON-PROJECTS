import tkinter as tk
from tkinter import ttk, StringVar, IntVar
import random
from math import sin, cos, radians
import time

class ModernRPSGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Epic RPS Battle")
        self.root.geometry("500x600")
        self.root.configure(bg='#2C2F33')

        # Game state
        self.wins = IntVar(value=0)
        self.streak = IntVar(value=0)
        self.max_streak = IntVar(value=0)
        self.result_var = StringVar(value='Ready to play? 😎')
        
        # Emoji mappings
        self.choices = {
            1: ("🪨", "Rock"),
            2: ("📄", "Paper"),
            3: ("✂️", "Scissors"),
            4: ("🖖", "Spock"),
            5: ("🦎", "Lizard")
        }

        self.setup_ui()
        self.animate_title()

    def setup_ui(self):
        # Title with animation
        self.title_label = tk.Label(
            self.root,
            text="Epic RPS Battle",
            font=("Arial", 24, "bold"),
            fg='#7289DA',
            bg='#2C2F33'
        )
        self.title_label.pack(pady=20)

        # Score display with modern styling
        score_frame = tk.Frame(self.root, bg='#2C2F33')
        score_frame.pack(pady=10)

        tk.Label(
            score_frame,
            textvariable=self.wins,
            font=("Arial", 36),
            fg='#43B581',
            bg='#2C2F33'
        ).pack()

        tk.Label(
            score_frame,
            text="wins",
            font=("Arial", 14),
            fg='#FFFFFF',
            bg='#2C2F33'
        ).pack()

        # Streak display
        streak_label = tk.Label(
            self.root,
            textvariable=StringVar(value=lambda: f"🔥 Streak: {self.streak.get()}"),
            font=("Arial", 12),
            fg='#FFA500',
            bg='#2C2F33'
        )
        streak_label.pack()

        # Game buttons
        buttons_frame = tk.Frame(self.root, bg='#2C2F33')
        buttons_frame.pack(pady=20)

        button_style = {
            "width": 8,
            "height": 2,
            "font": ("Arial", 16),
            "borderwidth": 0,
            "relief": "flat",
            "cursor": "hand2"
        }

        colors = ['#7289DA', '#43B581', '#FFA500', '#FF0000', '#9B59B6']
        
        for i, (choice_num, (emoji, name)) in enumerate(self.choices.items()):
            btn = tk.Button(
                buttons_frame,
                text=f"{emoji}\n{name}",
                command=lambda x=choice_num: self.play(x),
                bg=colors[i],
                fg='white',
                **button_style
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            
            # Hover effect
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#36393F'))
            btn.bind('<Leave>', lambda e, b=btn, c=colors[i]: b.configure(bg=c))

        # Result display
        tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 14),
            fg='#FFFFFF',
            bg='#2C2F33',
            wraplength=400
        ).pack(pady=20)

        # Reset button
        tk.Button(
            self.root,
            text="↺ Reset Score",
            command=self.reset_score,
            bg='#36393F',
            fg='white',
            relief='flat',
            cursor='hand2'
        ).pack(pady=10)

    def animate_title(self):
        def update_position(angle):
            y = sin(radians(angle)) * 5
            self.title_label.place_configure(rely=0.1 + y/100)
            self.root.after(50, update_position, (angle + 5) % 360)
        update_position(0)

    def play(self, user_choice):
        computer = random.randrange(1, 6)
        user_move = self.choices[user_choice][1]
        comp_move = self.choices[computer][1]
        
        # Win conditions dictionary
        win_conditions = {
            ('Rock', 'Scissors'): True,
            ('Rock', 'Lizard'): True,
            ('Paper', 'Rock'): True,
            ('Paper', 'Spock'): True,
            ('Scissors', 'Paper'): True,
            ('Scissors', 'Lizard'): True,
            ('Lizard', 'Spock'): True,
            ('Lizard', 'Paper'): True,
            ('Spock', 'Scissors'): True,
            ('Spock', 'Rock'): True
        }

        if user_move == comp_move:
            result = f"Draw! 🤝\nBoth chose {self.choices[user_choice][0]}"
            self.streak.set(0)
        elif (user_move, comp_move) in win_conditions:
            self.wins.set(self.wins.get() + 1)
            self.streak.set(self.streak.get() + 1)
            if self.streak.get() > self.max_streak.get():
                self.max_streak.set(self.streak.get())
            result = f"You win! 🎉\nYou: {self.choices[user_choice][0]} vs CPU: {self.choices[computer][0]}"
        else:
            self.streak.set(0)
            result = f"You lose! 😢\nYou: {self.choices[user_choice][0]} vs CPU: {self.choices[computer][0]}"

        # Animated result display
        def flash_result():
            self.result_var.set('')
            self.root.after(100, lambda: self.result_var.set(result))
        flash_result()

    def reset_score(self):
        self.wins.set(0)
        self.streak.set(0)
        self.result_var.set("Score reset! Ready for a new game? 😎")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = ModernRPSGame()
    game.run()