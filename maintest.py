import pytest
import tkinter as tk
from main import swap_val

def test_swap_val():
    """Pytest for testing the swap_val function"""
    root = tk.Tk()
    
    #Create test Label widgets with initial text
    label1 = tk.Label(root, text="2")
    label2 = tk.Label(root, text="3")
    
    #Use swap_val function to swap the text of the two labels
    swap_val(label1, label2)
    
    #Assert that the texts have been swapped
    assert label1.cget("text") == "3"
    assert label2.cget("text") == "2"

    root.destroy()

if __name__ == "__main__":
    pytest.main()
