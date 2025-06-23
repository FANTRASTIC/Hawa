import tkinter as tk
from tkinter import ttk
import math
import random
import time

class YaleCongratulationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Congratulations Anangsha! 🎉")
        self.root.geometry("1000x700")
        self.root.configure(bg="#FF69B4")  # Cheerful pink background
        
        # Animation variables
        self.animation_step = 0
        self.confetti_particles = []
        self.sakura_petals = []
        self.text_colors = ["#FFFFFF", "#FFD700", "#FF69B4", "#00FF00", "#FF4500", "#9370DB"]
        self.current_color_index = 0
        
        # Create canvas for animations
        self.canvas = tk.Canvas(root, width=1000, height=700, bg="#FFB6C1", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Initialize particles
        self.init_confetti()
        self.init_sakura_petals()
        
        # Create UI elements
        self.create_ui_elements()
        
        # Create anime characters
        self.create_anime_characters()
        
        # Create cheerful background elements
        self.create_cheerful_background()
        
        # Start animations
        self.animate()
        
    def init_confetti(self):
        """Initialize confetti particles"""
        for _ in range(60):
            particle = {
                'x': random.randint(0, 1000),
                'y': random.randint(-100, 0),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(1, 4),
                'color': random.choice(['#FFD700', '#FF69B4', '#00FF00', '#FF4500', '#FFFFFF', '#FFFF00', '#9370DB']),
                'size': random.randint(3, 8)
            }
            self.confetti_particles.append(particle)
    
    def init_sakura_petals(self):
        """Initialize sakura petals for anime theme"""
        for _ in range(30):
            petal = {
                'x': random.randint(0, 1000),
                'y': random.randint(-200, 0),
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(0.5, 2),
                'rotation': random.uniform(0, 360),
                'size': random.randint(4, 10)
            }
            self.sakura_petals.append(petal)
    
    def create_ui_elements(self):
        """Create the main UI elements"""
        # Main congratulations text
        self.main_text = self.canvas.create_text(
            500, 80, 
            text="🎉 CONGRATULATIONS 🎉", 
            font=("Arial", 32, "bold"), 
            fill="#FFD700",
            anchor="center"
        )
        
        # Anangsha's name (larger and special)
        self.name_text = self.canvas.create_text(
            500, 130, 
            text="ANANGSHA", 
            font=("Arial", 40, "bold"), 
            fill="#FFFFFF",
            anchor="center"
        )
        
        # Yale text
        self.yale_text = self.canvas.create_text(
            500, 180, 
            text="FOR YALE UNIVERSITY!", 
            font=("Arial", 26, "bold"), 
            fill="#FFD700",
            anchor="center"
        )
        
        # Create Yale "Y" logo in the middle
        self.create_yale_logo()
        
        # Achievement message
        self.achievement_text = self.canvas.create_text(
            500, 580, 
            text="🌟 Your hard work and dedication have paid off! 🌟", 
            font=("Arial", 18, "italic"), 
            fill="#FFFFFF",
            anchor="center"
        )
        
        # Future message
        self.future_text = self.canvas.create_text(
            500, 620, 
            text="Welcome to the Bulldogs family! 🐕", 
            font=("Arial", 16), 
            fill="#FFD700",
            anchor="center"
        )
        
        # Date
        self.date_text = self.canvas.create_text(
            500, 660, 
            text="🎓 Class of 2029 🎓", 
            font=("Arial", 14, "bold"), 
            fill="#FFFFFF",
            anchor="center"
        )
    
    def create_yale_logo(self):
        """Create a stylized Yale 'Y' logo"""
        # Yale Y logo background circle
        self.canvas.create_oval(450, 250, 550, 350, fill="#FFFFFF", outline="#0F4C81", width=3)
        
        # Create the "Y" shape
        # Left branch of Y
        self.canvas.create_line(470, 270, 500, 300, fill="#0F4C81", width=8, capstyle="round")
        # Right branch of Y
        self.canvas.create_line(530, 270, 500, 300, fill="#0F4C81", width=8, capstyle="round")
        # Stem of Y
        self.canvas.create_line(500, 300, 500, 330, fill="#0F4C81", width=8, capstyle="round")
        
        # Add "YALE" text below the logo
        self.canvas.create_text(500, 370, text="YALE", font=("Arial", 22, "bold"), fill="#0F4C81")
        
        # Decorative elements around the logo
        for angle in range(0, 360, 45):
            x = 500 + 70 * math.cos(math.radians(angle))
            y = 300 + 70 * math.sin(math.radians(angle))
            self.canvas.create_text(x, y, text="⭐", font=("Arial", 14), fill="#FFD700")
    
    def create_anime_characters(self):
        """Create anime-style characters and Hanabi references"""
        # Left side - Anime girl celebrating
        self.create_anime_girl_left()
        
        # Right side - Hanabi (Mobile Legends) inspired character
        self.create_hanabi_character()
        
        # Add anime-style speech bubbles
        self.create_speech_bubbles()
    
    def create_anime_girl_left(self):
        """Create an anime girl character on the left"""
        # Head
        self.canvas.create_oval(80, 200, 140, 260, fill="#FFDBAC", outline="#000000", width=2)
        
        # Eyes
        self.canvas.create_oval(90, 220, 105, 235, fill="#000000")
        self.canvas.create_oval(115, 220, 130, 235, fill="#000000")
        self.canvas.create_oval(92, 222, 98, 228, fill="#FFFFFF")
        self.canvas.create_oval(117, 222, 123, 228, fill="#FFFFFF")
        
        # Mouth (happy)
        self.canvas.create_arc(105, 240, 115, 250, start=0, extent=180, fill="#FF69B4", width=2)
        
        # Hair (pink)
        self.canvas.create_polygon(70, 200, 150, 200, 140, 180, 80, 180, fill="#FF69B4", outline="#000000", width=2)
        
        # Body
        self.canvas.create_rectangle(95, 260, 125, 320, fill="#9370DB", outline="#000000", width=2)
        
        # Arms (celebrating pose)
        self.canvas.create_line(95, 280, 70, 260, fill="#FFDBAC", width=8, capstyle="round")
        self.canvas.create_line(125, 280, 150, 260, fill="#FFDBAC", width=8, capstyle="round")
        
        # Add sparkles around character
        sparkle_positions = [(60, 180), (160, 190), (50, 250), (170, 270)]
        for x, y in sparkle_positions:
            self.canvas.create_text(x, y, text="✨", font=("Arial", 12), fill="#FFD700")
        
        # Character label
        self.canvas.create_text(110, 340, text="Anime MC", font=("Arial", 10, "bold"), fill="#FFFFFF")
    
    def create_hanabi_character(self):
        """Create Hanabi-inspired character on the right"""
        # Head
        self.canvas.create_oval(860, 200, 920, 260, fill="#FFDBAC", outline="#000000", width=2)
        
        # Eyes (more detailed)
        self.canvas.create_oval(870, 220, 885, 235, fill="#4169E1")
        self.canvas.create_oval(895, 220, 910, 235, fill="#4169E1")
        self.canvas.create_oval(872, 222, 878, 228, fill="#FFFFFF")
        self.canvas.create_oval(897, 222, 903, 228, fill="#FFFFFF")
        
        # Mouth
        self.canvas.create_arc(885, 240, 895, 250, start=0, extent=180, fill="#FF1493", width=2)
        
        # Hair (black with blue highlights)
        self.canvas.create_polygon(850, 200, 930, 200, 920, 170, 860, 170, fill="#000080", outline="#000000", width=2)
        
        # Body (ninja-style outfit)
        self.canvas.create_rectangle(875, 260, 905, 320, fill="#000080", outline="#000000", width=2)
        
        # Arms
        self.canvas.create_line(875, 280, 850, 270, fill="#FFDBAC", width=8, capstyle="round")
        self.canvas.create_line(905, 280, 930, 270, fill="#FFDBAC", width=8, capstyle="round")
        
        # Hanabi's signature weapon (simplified)
        self.canvas.create_line(930, 270, 950, 250, fill="#FFD700", width=4)
        self.canvas.create_oval(945, 245, 955, 255, fill="#FF4500")
        
        # Add ninja stars around character
        star_positions = [(840, 180), (940, 190), (830, 250), (950, 270)]
        for x, y in star_positions:
            self.canvas.create_text(x, y, text="🌟", font=("Arial", 12), fill="#FFD700")
        
        # Character label
        self.canvas.create_text(890, 340, text="Hanabi Style", font=("Arial", 10, "bold"), fill="#FFFFFF")
    
    def create_speech_bubbles(self):
        """Create speech bubbles for characters"""
        # Left character speech bubble
        self.canvas.create_oval(150, 150, 250, 190, fill="#FFFFFF", outline="#000000", width=2)
        self.canvas.create_text(200, 170, text="Sugoi! 🎉", font=("Arial", 12, "bold"), fill="#000000")
        
        # Right character speech bubble
        self.canvas.create_oval(750, 150, 850, 190, fill="#FFFFFF", outline="#000000", width=2)
        self.canvas.create_text(800, 170, text="Omedeto! ⭐", font=("Arial", 12, "bold"), fill="#000000")
    
    def create_cheerful_background(self):
        """Create cheerful background elements"""
        # Rainbow arcs
        colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
        for i, color in enumerate(colors):
            self.canvas.create_arc(300, 400, 700, 500, start=0, extent=180, 
                                 outline=color, width=3, style="arc")
        
        # Hearts scattered around
        heart_positions = [
            (100, 100), (900, 100), (50, 400), (950, 400),
            (200, 50), (800, 50), (150, 450), (850, 450),
            (250, 120), (750, 120), (300, 500), (700, 500)
        ]
        
        for x, y in heart_positions:
            self.canvas.create_text(x, y, text="💖", font=("Arial", 16), fill="#FF1493")
        
        # Celebration balloons
        balloon_positions = [(80, 350), (920, 350), (150, 380), (850, 380)]
        balloon_colors = ["#FF69B4", "#FFD700", "#00FF00", "#9370DB"]
        
        for i, (x, y) in enumerate(balloon_positions):
            color = balloon_colors[i % len(balloon_colors)]
            # Balloon
            self.canvas.create_oval(x-15, y-25, x+15, y+5, fill=color, outline="#000000", width=2)
            # String
            self.canvas.create_line(x, y+5, x, y+40, fill="#000000", width=2)
        
        # Add more decorative elements
        self.create_decorative_borders()
    
    def create_decorative_borders(self):
        """Create decorative borders"""
        # Top border
        for x in range(0, 1000, 50):
            self.canvas.create_text(x, 20, text="🌸", font=("Arial", 14), fill="#FF69B4")
        
        # Bottom border
        for x in range(0, 1000, 50):
            self.canvas.create_text(x, 680, text="🌸", font=("Arial", 14), fill="#FF69B4")
        
        # Side borders
        for y in range(50, 650, 50):
            self.canvas.create_text(20, y, text="⭐", font=("Arial", 12), fill="#FFD700")
            self.canvas.create_text(980, y, text="⭐", font=("Arial", 12), fill="#FFD700")
    
    def update_confetti(self):
        """Update confetti particle positions"""
        for particle in self.confetti_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            
            # Reset particle if it goes off screen
            if particle['y'] > 700:
                particle['y'] = random.randint(-50, 0)
                particle['x'] = random.randint(0, 1000)
            
            if particle['x'] < 0 or particle['x'] > 1000:
                particle['vx'] *= -1
    
    def update_sakura_petals(self):
        """Update sakura petal positions"""
        for petal in self.sakura_petals:
            petal['x'] += petal['vx']
            petal['y'] += petal['vy']
            petal['rotation'] += 2
            
            # Reset petal if it goes off screen
            if petal['y'] > 700:
                petal['y'] = random.randint(-100, 0)
                petal['x'] = random.randint(0, 1000)
    
    def draw_confetti(self):
        """Draw confetti particles"""
        # Clear previous confetti
        self.canvas.delete("confetti")
        
        # Draw new confetti
        for particle in self.confetti_particles:
            self.canvas.create_oval(
                particle['x'] - particle['size']//2,
                particle['y'] - particle['size']//2,
                particle['x'] + particle['size']//2,
                particle['y'] + particle['size']//2,
                fill=particle['color'],
                outline="",
                tags="confetti"
            )
    
    def draw_sakura_petals(self):
        """Draw sakura petals"""
        # Clear previous petals
        self.canvas.delete("sakura")
        
        # Draw new petals
        for petal in self.sakura_petals:
            self.canvas.create_text(
                petal['x'], petal['y'],
                text="🌸",
                font=("Arial", petal['size']),
                fill="#FFB6C1",
                tags="sakura"
            )
    
    def animate_text(self):
        """Animate the main text colors"""
        self.current_color_index = (self.current_color_index + 1) % len(self.text_colors)
        new_color = self.text_colors[self.current_color_index]
        
        # Animate main congratulations text
        self.canvas.itemconfig(self.main_text, fill=new_color)
        
        # Make Anangsha's name pulse
        scale = 1 + 0.15 * math.sin(self.animation_step * 0.1)
        font_size = int(40 * scale)
        self.canvas.itemconfig(self.name_text, font=("Arial", font_size, "bold"))
    
    def animate_characters(self):
        """Animate the anime characters"""
        # Make characters bounce slightly
        bounce = 3 * math.sin(self.animation_step * 0.05)
        
        # This would move characters, but we'll keep them static for simplicity
        # and just add some sparkle effects instead
        if self.animation_step % 60 == 0:  # Every 3 seconds
            # Add sparkles around characters
            for _ in range(3):
                x = random.randint(50, 170)
                y = random.randint(180, 320)
                self.canvas.create_text(x, y, text="✨", font=("Arial", 8), fill="#FFD700", tags="temp_sparkle")
                
                x = random.randint(830, 950)
                y = random.randint(180, 320)
                self.canvas.create_text(x, y, text="⭐", font=("Arial", 8), fill="#FFD700", tags="temp_sparkle")
            
            # Remove temporary sparkles after a short time
            self.root.after(1000, lambda: self.canvas.delete("temp_sparkle"))
    
    def animate(self):
        """Main animation loop"""
        self.animation_step += 1
        
        # Update and draw particles
        self.update_confetti()
        self.draw_confetti()
        
        self.update_sakura_petals()
        self.draw_sakura_petals()
        
        # Animate text every 30 frames (about 0.6 seconds)
        if self.animation_step % 30 == 0:
            self.animate_text()
        
        # Animate characters
        self.animate_characters()
        
        # Schedule next animation frame
        self.root.after(50, self.animate)  # 20 FPS

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = YaleCongratulationsApp(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (1000 // 2)
    y = (root.winfo_screenheight() // 2) - (700 // 2)
    root.geometry(f"1000x700+{x}+{y}")
    
    # Make window non-resizable for consistent layout
    root.resizable(False, False)
    
    # Add multiple celebration popups
    def show_celebration():
        celebration_window = tk.Toplevel(root)
        celebration_window.title("🎊 CELEBRATION! 🎊")
        celebration_window.geometry("350x200")
        celebration_window.configure(bg="#FFD700")
        
        label = tk.Label(
            celebration_window, 
            text="🎊 AMAZING ACHIEVEMENT! 🎊\n\nYou did it, Anangsha!\nYale is lucky to have you!\n\n🌸 Anime girls are cheering! 🌸\n⭐ Hanabi sends her congratulations! ⭐",
            font=("Arial", 12, "bold"),
            bg="#FFD700",
            fg="#0F4C81",
            justify="center"
        )
        label.pack(expand=True)
        
        # Auto-close after 4 seconds
        celebration_window.after(4000, celebration_window.destroy)
        
        # Center the celebration window
        celebration_window.update_idletasks()
        x = root.winfo_x() + (1000 // 2) - (350 // 2)
        y = root.winfo_y() + (700 // 2) - (200 // 2)
        celebration_window.geometry(f"350x200+{x}+{y}")
    
    def show_anime_celebration():
        anime_window = tk.Toplevel(root)
        anime_window.title("🌸 Anime Celebration! 🌸")
        anime_window.geometry("300x150")
        anime_window.configure(bg="#FF69B4")
        
        label = tk.Label(
            anime_window,
            text="🌸 Kawaii! 🌸\n\nSugoi desu ne, Anangsha-chan!\nGanbatte at Yale! 💖",
            font=("Arial", 11, "bold"),
            bg="#FF69B4",
            fg="#FFFFFF",
            justify="center"
        )
        label.pack(expand=True)
        
        anime_window.after(3500, anime_window.destroy)
        
        # Position slightly offset from main celebration
        anime_window.update_idletasks()
        x = root.winfo_x() + 100
        y = root.winfo_y() + 100
        anime_window.geometry(f"300x150+{x}+{y}")
    
    # Show celebrations at different times
    root.after(2000, show_celebration)
    root.after(3000, show_anime_celebration)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
