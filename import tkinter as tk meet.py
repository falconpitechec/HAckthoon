import tkinter as tk
from tkinter import messagebox
import hashlib
import requests
import webbrowser

# Configuration
WHITE = "#FFFFFF"
SKY_BLUE = "#87CEEB"
BLACK = "#000000"
FONT = ("Helvetica", 12)

# User roles
ROLES = ["student", "teacher", "admin"]

# OAuth credentials
GOOGLE_CLIENT_ID = "your_google_client_id"
GOOGLE_CLIENT_SECRET = "your_google_client_secret"
FACEBOOK_CLIENT_ID = "your_facebook_client_id"
FACEBOOK_CLIENT_SECRET = "your_facebook_client_secret"

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Authentication and Authorization")
        self.configure(background=WHITE)

        # Create frames
        self.registration_frame = tk.Frame(self, bg=WHITE)
        self.registration_frame.pack(fill="both", expand=True)

        self.login_frame = tk.Frame(self, bg=WHITE)
        self.login_frame.pack(fill="both", expand=True)

        self.oauth_frame = tk.Frame(self, bg=WHITE)
        self.oauth_frame.pack(fill="both", expand=True)

        # Registration frame
        tk.Label(self.registration_frame, text="Register", font=FONT, bg=WHITE).pack()
        tk.Label(self.registration_frame, text="Username:", font=FONT, bg=WHITE).pack()
        self.username_entry = tk.Entry(self.registration_frame, font=FONT, width=20)
        self.username_entry.pack()
        tk.Label(self.registration_frame, text="Password:", font=FONT, bg=WHITE).pack()
        self.password_entry = tk.Entry(self.registration_frame, font=FONT, width=20, show="*")
        self.password_entry.pack()
        tk.Label(self.registration_frame, text="Role:", font=FONT, bg=WHITE).pack()
        self.role_var = tk.StringVar()
        self.role_var.set(ROLES[0])
        self.role_menu = tk.OptionMenu(self.registration_frame, self.role_var, *ROLES)
        self.role_menu.pack()
        tk.Button(self.registration_frame, text="Register", command=self.register_user, font=FONT, bg=SKY_BLUE).pack()
        
        # Login frame
        tk.Label(self.login_frame, text="Login", font=FONT, bg=WHITE).pack()
        tk.Label(self.login_frame, text="Username:", font=FONT, bg=WHITE).pack()
        self.login_username_entry = tk.Entry(self.login_frame, font=FONT, width=20)
        self.login_username_entry.pack()
        tk.Label(self.login_frame, text="Password:", font=FONT, bg=WHITE).pack()
        self.login_password_entry = tk.Entry(self.login_frame, font=FONT, width=20, show="*")
        self.login_password_entry.pack()
        tk.Button(self.login_frame, text="Login", command=self.login_user, font=FONT, bg=SKY_BLUE).pack()

        # OAuth frame
        tk.Label(self.oauth_frame, text="Login with social media", font=FONT, bg=WHITE).pack()
        tk.Button(self.oauth_frame, text="Google", command=self.google_oauth, font=FONT, bg=SKY_BLUE).pack()
        tk.Button(self.oauth_frame, text="Facebook", command=self.facebook_oauth, font=FONT, bg=SKY_BLUE).pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        if username and password:
            # Hash password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            # Store user credentials in a database or file
            # For demonstration purposes, we'll store it in a dictionary
            users = {"username": username, "password": hashed_password, "role": role}
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def login_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if username and password:
            # Check if user exists in database or file
            # For demonstration purposes, we'll check the dictionary
            users = {"username": "john", "password": "hashed_password", "role": "student"}
            if username == users["username"] and hashlib.sha256(password.encode()).hexdigest() == users["password"]:
                messagebox.showinfo("Success", "Login successful!")
                # Grant access based on user role
                if users["role"] == "student":
                    # Student dashboard
                    self.student_dashboard()
                elif users["role"] == "teacher":
                    # Teacher dashboard
                    self.teacher_dashboard()
                elif users["role"] == "admin":
                    # Admin dashboard
                    self.admin_dashboard()
            else:
                messagebox.showerror("Error","Invalid username or password!")
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def google_oauth(self):
        # Redirect user to Google OAuth authorization URL
        auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri=http://localhost&response_type=code&scope=openid%20email%20profile"
        webbrowser.open(auth_url)

    def facebook_oauth(self):
        # Redirect user to Facebook OAuth authorization URL
        auth_url = f"https://www.facebook.com/v3.3/dialog/oauth?client_id={FACEBOOK_CLIENT_ID}&redirect_uri=http://localhost&response_type=code&scope=public_profile%20email"
        webbrowser.open(auth_url)

    def student_dashboard(self):
        # Student dashboard implementation
        pass

    def teacher_dashboard(self):
        # Teacher dashboard implementation
        pass

    def admin_dashboard(self):
        # Admin dashboard implementation
        pass

    def _init_(self):
        super()._init_()
        self.title("Interactive Learning Platform")
        self.configure(background=SKY_BLUE)

        # Create frames
        self.lesson_frame = tk.Frame(self, bg=SKY_BLUE)
        self.lesson_frame.pack(fill="both", expand=True)

        self.collaboration_frame = tk.Frame(self, bg=SKY_BLUE)
        self.collaboration_frame.pack(fill="both", expand=True)

        self.gamification_frame = tk.Frame(self, bg=SKY_BLUE)
        self.gamification_frame.pack(fill="both", expand=True)

        # Lesson frame
        tk.Label(self.lesson_frame, text="Multimedia Lessons", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.lesson_frame, text="Video Lesson", command=self.play_video, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.lesson_frame, text="Interactive Simulation", command=self.launch_simulation, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.lesson_frame, text="Quiz", command=self.take_quiz, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.lesson_frame, text="Game", command=self.play_game, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

        # Collaboration frame
        tk.Label(self.collaboration_frame, text="Collaborative Tools", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.collaboration_frame, text="Group Project", command=self.create_project, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.collaboration_frame, text="Discussion Forum", command=self.open_forum, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.collaboration_frame, text="Peer Review", command=self.review_peer, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

        # Gamification frame
        tk.Label(self.gamification_frame, text="Gamification", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.gamification_frame, text="Earn Badges", command=self.earn_badge, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.gamification_frame, text="View Leaderboard", command=self.view_leaderboard, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()
        tk.Button(self.gamification_frame, text="Redeem Rewards", command=self.redeem_reward, font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def play_video(self):
       webbrowser.open("https://www.phet.colorado.edu/sims # Play video lesson")

       

    def launch_simulation(self):
        # Launch interactive simulation
        ("/html/gravity-lab/latest/gravity-lab_en.html")

    def take_quiz(self):
        # Take quiz
        quiz_window = tk.Toplevel(self)
        quiz_window.title("QUIZ FOR 1ST STANDARD")
        quiz_window.configure(background=SKY_BLUE)
        tk.Label(quiz_window, text="WHAT IS YOUR NAME ", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def play_game(self):
        # Play game
        game_window = tk.Toplevel(self)
        game_window.title("Game")
        game_window.configure(background=SKY_BLUE)
        webbrowser.open("https://www.education.com/games/first-grade/")

    def create_project(self):
        # Create group project
        project_window = tk.Toplevel(self)
        project_window.title("A GROUP PROJECT MAKER")
        project_window.configure(background=SKY_BLUE)
         
        

    def open_forum(self):
        # Open discussion forum
        forum_window = tk.Toplevel(self)
        forum_window.title("Discussion Forum")
        forum_window.configure(background=SKY_BLUE)
        tk.Label(forum_window, text="Discussion forum will appear here!", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def review_peer(self):
        # Review peer work
        review_window = tk.Toplevel(self)
        review_window.title("Peer Review")
        review_window.configure(background=SKY_BLUE)
        tk.Label(review_window, text="Peer review tool will appear here!", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def earn_badge(self):
        # Earn badge
        badge_window = tk.Toplevel(self)
        badge_window.title("Badge Earned")
        badge_window.configure(background=SKY_BLUE)
        tk.Label(badge_window, text="You earned a badge!VERY GOOD,We All are proud of you Child.Keep it up and WE WILL ALWAYS SUPPORT YOU", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def view_leaderboard(self):
        # View leaderboard
        leaderboard_window = tk.Toplevel(self)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.configure(background=SKY_BLUE)
        tk.Label(leaderboard_window, text="Leaderboard will appear here!", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

    def redeem_reward(self):
        # Redeem reward
        reward_window = tk.Toplevel(self)
        reward_window.title("Reward Redeemed")
        reward_window.configure(background=SKY_BLUE)
        tk.Label(reward_window, text="YOUR PROGRESS HAS BEEN MIND BLOWING.KEEP YOUR HEADS UP AND MAKE YOUR PARENTS FEEL PROUD", font=FONT, bg=SKY_BLUE, fg=BLACK).pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()