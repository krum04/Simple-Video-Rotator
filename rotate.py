import tkinter as tk
from tkinter import filedialog, ttk
from moviepy.editor import VideoFileClip

# Create the main window
root = tk.Tk()

# Set Window title
root.title("Video Rotat")

# Lock the size of the window
root.resizable(width=False, height=False)

# Create a function that will be called when the user selects a video file
def rotate_video():
    # Ask the user to select a video file
    filepath = filedialog.askopenfilename()
    
    # Get the selected rotation angle
    angle = int(rotation_menu.get())
    
    # Open the video file
    video = VideoFileClip(filepath)
    
    # Rotate the video
    rotated_video = video.rotate(angle)
    
    # Save the rotated video to a file
    rotated_video.write_videofile("rotated_video.mp4")

# Create a label to prompt the user to select a rotation angle
label = tk.Label(root, text="Select a rotation angle:")
label.grid(row=0, column=0)

# Create a drop-down menu for the user to select a rotation angle
rotation_menu = ttk.Combobox(root, values=[90, 180, 270])
rotation_menu.current(0)
rotation_menu.grid(row=0, column=1)

# Create a button that will start the video rotation when clicked
button = tk.Button(root, text="Rotate & Save", command=rotate_video)
button.grid(row=1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
