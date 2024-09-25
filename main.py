import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Navigation Example")
root.geometry("400x200")  # Optional: Set a fixed window size

# Page content (this could be text, images, or anything you'd like)
pages = [
    "EE Research Review TOC",
    "This is Page 2. Keep going!",
    "You are now on Page 3!",
    "Page 4: Almost there!",
    "This is Page 5, the final page."
]

# Track the current page index
current_page = 0

# Create a label with some text
label = tk.Label(root, text="Table of Contents")
label2 = tk.Label(root, text="EE Research")

# Display the label on the window
label.pack()
label2.pack()

# Function to update the label with the current page content
def update_page():
    label.config(text=pages[current_page])

# Function to go to the next page
def next_page():
    global current_page
    if current_page < len(pages) - 1:
        current_page += 1
        update_page()

# Function to go to the previous page
def previous_page():
    global current_page
    if current_page > 0:
        current_page -= 1
        update_page()

# Function to open a quiz pop-up with a question and multiple-choice answers
def open_quiz_popup(question, options, correct_answer):
    popup = tk.Toplevel(root)  # Create a new window for the quiz
    popup.title("Quiz")
    popup.geometry("300x250")

    # Add the question to the pop-up window
    label_question = tk.Label(popup, text=question, font=("Helvetica", 12))
    label_question.pack(pady=10)

    # Variable to store the selected answer
    selected_answer = tk.StringVar(value="")

    # Create radio buttons for each answer option
    for option in options:
        radio_button = tk.Radiobutton(popup, text=option, variable=selected_answer, value=option)
        radio_button.pack(anchor="w", padx=20)

    # Function to check the selected answer and provide feedback
    def submit_answer():
        if selected_answer.get() == correct_answer:
            print("Result", "Correct answer!")
        else:
            print("Result", "Incorrect answer. Try again!")

    # Submit button to check the answer
    submit_button = tk.Button(popup, text="Submit", command=submit_answer)
    submit_button.pack(pady=10)

    # Close button to close the pop-up
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)


# Sample question and answers for the quiz
question = "What is the capital of France?"
options = ["Berlin", "Madrid", "Paris", "Rome"]
correct_answer = "Paris"

# Create a button to open the quiz pop-up
quiz_button = tk.Button(root, text="Start Quiz",
                        command=lambda: open_quiz_popup(question, options, correct_answer))
quiz_button.pack(pady=50)

# Function to open an alternate pop-up window
# Function to open a pop-up window with custom content
def open_popup(content, title):
    popup = tk.Toplevel(root)  # Create a new window
    popup.title(title)
    popup.geometry("400x200")  # Set the size of the pop-up window

    # Add custom content to the pop-up window
    label_popup = tk.Label(popup, text=content)
    label_popup.pack(pady=20)

    # You can also add buttons to the pop-up window if needed
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Create buttons that open different pop-ups with unique content

leaderboard_button = tk.Button(root, text="Active Leaderboard",
                    command=lambda: open_popup("This is Pop-up 3!", "Pop-up 3"))
leaderboard_button.pack(side=tk.RIGHT, padx=5)

info_button = tk.Button(root, text="Additional Info",
                    command=lambda: open_popup("Code By: Max King, Content By: Ms. Harrison", "Additional Info"))
info_button.pack(side=tk.LEFT, padx=10)


# Start the GUI event loop
root.mainloop()
