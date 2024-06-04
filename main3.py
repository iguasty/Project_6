import tkinter as tk
import random


def sort_step():
    """shows the steps of the comparison and value swapping by highlighting"""
    global current_index, sorted_index
    if sorted_index == 0:
        label_list[0].config(bg="green")
        print("Sorting complete!")
        print_array()
        return
    
    # Clear any previous highlights
    for i in range(len(label_list)):
        if i >= sorted_index:
            label_list[i].config(bg="green")
        else:
            label_list[i].config(bg="SystemButtonFace")
    
    # Highlight the current labels being compared
    if current_index < sorted_index:
        label_list[current_index].config(bg="pink") #highlight value that may be swapped with value to the right 
        label_list[current_index + 1].config(bg="cyan") #highlight value that may be swapped with value to the left
        
        # Compare and swap if necessary
        if int(label_list[current_index].cget("text")) > int(label_list[current_index + 1].cget("text")):
            swap_val(label_list[current_index], label_list[current_index + 1])
            label_list[current_index].config(bg="yellow") #highlight value that will be swapped
            print("Swapping " + str(label_list[current_index + 1].cget("text")) + " with " + str(label_list[current_index].cget("text")))
        current_index += 1 #increase index
    else:
        sorted_index -= 1
        current_index = 0
    
    root.after(delay, sort_step)

def swap_val(val1, val2):
    """swaps val1 with val2"""
    temp_text = val1.cget("text")
    val1.config(text=val2.cget("text"))
    val2.config(text=temp_text)

def gen_array():
    """creates a list of boxes with 10 random numbers within the range 0-100"""
    global label_list
    label_list = []
    for i in range(2):
        for j in range(5):
            random_number = str(random.randint(0, 100))
            number = tk.Label(root, text=random_number, padx=15, pady=5, borderwidth=1, relief="groove")
            number.grid(row=i, column=j, padx=15, pady=5)
            label_list.append(number)
    
    global sorted_index, current_index
    sorted_index = len(label_list) - 1
    current_index = 0
    print("Generating new array...")

def print_array():
    """copies value of sorted array to array that can be printed out to terminal. can also be used for easier testing"""
    printable_array = []
    for i in range(len(label_list)):
        number = label_list[i].cget("text")
        printable_array.append(number)
    print("Here is the sorted array:")
    print(printable_array, sep=", ")
    
#main loop
root = tk.Tk()
root.title("Sort Values")
delay = 250

sort_button = tk.Button(root, text="Sort", command=sort_step)
sort_button.grid(row=12, column=5, columnspan=1, pady=10)

gen_button = tk.Button(root, text="Generate Array", command=gen_array)
gen_button.grid(row=12, column=6, columnspan=1, pady=10)

gen_array()

root.mainloop()
