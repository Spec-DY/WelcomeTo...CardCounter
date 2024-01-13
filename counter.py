import tkinter as tk
from tkinter import font

# Global variable
dic = {str(i): 3 if i in [1, 2, 14, 15] else 4 if i in [3, 13] else 5 if i in [4, 12] else 6 if i in [5, 11] else 7 if i in [6, 10] else 8 if i in [7, 9] else 9 for i in range(1, 16)}
last_three_inputs = []


def reset_dic():
    """Reset the global dictionary `dic` to its initial state and update the display."""
    global dic
    dic = {str(i): 3 if i in [1, 2, 14, 15] else 4 if i in [3, 13] else 5 if i in [4, 12] else 6 if i in [5, 11] else 7 if i in [6, 10] else 8 if i in [7, 9] else 9 for i in range(1, 16)}
    update_display()


def update(card: str):
    """Update the card count based on the selected card, manage the last three inputs, or revert the last input."""
    global dic, last_three_inputs
    if card == "re":
        reset_dic()
        last_three_inputs = []
    elif card == "bk":
        if last_three_inputs:
            last_input = last_three_inputs.pop()
            dic[last_input] += 1
    else:
        if dic[card] > 0:
            dic[card] -= 1
            last_three_inputs.append(card)
            if len(last_three_inputs) > 3:
                last_three_inputs.pop(0)
    update_display()


def update_display():
    """Update the text display to show the current state of the card table and the last three inputs."""
    global text_display, last_inputs_display
    display_text = "\nCard Table\nCard ----- Count\n" + '-' * 20 + "\n"
    for card, number in dic.items():
        display_text += f"{card.rjust(4)} ----- {number}\n"
    text_display.delete('1.0', tk.END)
    text_display.insert(tk.END, display_text)
    last_inputs_display.config(text="Last Inputs: " + ", ".join(last_three_inputs))


def setup_buttons(root, button_font):
    """Set up the buttons for the card game."""
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)
    for card in list(dic.keys()) + ["re", "bk"]:
        button = tk.Button(button_frame, text=card, command=lambda c=card: update(c), font=button_font)
        button.pack(side=tk.TOP, padx=2, pady=2)


def setup_card_table_display(root, text_font, small_text_font):
    """Set up the display for the card table and the last three inputs."""
    global text_display, last_inputs_display
    card_table_frame = tk.Frame(root)
    card_table_frame.pack(side=tk.LEFT, padx=10, pady=10)
    text_display = tk.Text(card_table_frame, height=20, width=50, font=text_font)
    text_display.pack(side=tk.TOP, pady=10)
    last_inputs_display = tk.Label(card_table_frame, text="Last Inputs: ", font=small_text_font)
    last_inputs_display.pack(side=tk.TOP, pady=5)


def main():
    """Main function to set up the tkinter GUI layout and start the application."""
    root = tk.Tk()
    root.title("Card Game")
    button_font = font.Font(size=12, weight='bold')
    text_font = font.Font(size=14, weight='bold')
    small_text_font = font.Font(size=10)  # Smaller font for last three inputs display
    setup_buttons(root, button_font)
    setup_card_table_display(root, text_font, small_text_font)
    update_display()
    root.mainloop()


if __name__ == "__main__":
    main()
