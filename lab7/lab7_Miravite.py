"""
Gabriel Miravite
Feb 19, 2026
Lab 7: Working with Data in Python
"""

# I was getting a FileNotFoundError at first in my codespace for this repo just cuz I forgot to cd into the correct location :PPP

print("\n============= Example 1: Read File =============")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

# Check that the file is closed.
print(f"Is the file closed? {file1.closed}")

print("\n============= Example 2: Readline File =============")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)

print("\n============= Example 3: Readlines File =============")
# readlines makes a list of each line in the text file
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines(30)
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)

print("\n============= Example 4: Loop Through Each Line in a File =============")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) # strip() removes \n in each line

print("\n============= Example 5: Create a File =============")
# w mode creates a file if the file doesn't exist
# w mode overwrites the data in the file if the file already exists
with open("Miravite.txt", "w") as file:
    file.write("Python Basics for Data Science\n")
    file.write("Gabriel Miravite")

print("\n============= Example 6: Append in a File =============")
# Append the date & time into "Miravite.txt"
from datetime import datetime
with open("Miravite.txt", "a") as file:
    file.write(f"\nLast Update: {datetime.now()}")

print("\n============= Example 7: Copy a File =============")
# Copy file "Miravite.txt" to a new file
with open("Miravite.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)

print("\n============= Example 8: Creating DataFrame with Pandas =============")
# ran pip3 install pandas in the terminal atp
import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

print("\n============= Example 9: Creating df with Pandas from an Excel File =============")
# ran pip3 install openpyxl in the terminal atp
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head()) # Wait what's the difference b/c I'm not sure



print("\nEnd of Examples, Start of EXERCISES")

print("\n============= Exercise:  =============")
# I think I should move this function right
def email_read():
        g, y, h = 0
        with open("user_email.txt", "r") as readfile:
            with open("user_email.txt", "w") as writefile:
                print("Work on this later")