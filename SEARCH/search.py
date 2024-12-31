import tkinter as tk
from tkinter import *
import webbrowser

# Define the main window
root = tk.Tk()
root.title("Search Engine")

# Set background color
root.configure(bg="black")

# Define the function for YouTube search
def search_youtube():
    query = entry.get()
    if query.strip():
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)

# Define the function for Google search
def search_google():
    query = entry.get()
    if query.strip():
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

# Define the function for Instagram search
def search_instagram():
    username = entry.get().replace("@", "").strip()
    if username:
        url = f"https://www.instagram.com/{username}"
        webbrowser.open(url)

# Create input field
Label(root, text="Enter your command:", bg="black", fg="white", font=("Arial", 12)).pack(pady=10)
entry = Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

# Create buttons
Button(root, text="Search on YouTube", command=search_youtube, bg="red", fg="white", font=("Arial", 10)).pack(pady=5)
Button(root, text="Search on Google", command=search_google, bg="blue", fg="white", font=("Arial", 10)).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram, bg="purple", fg="white", font=("Arial", 10)).pack(pady=5)

# Run the main loop
root.mainloop()
