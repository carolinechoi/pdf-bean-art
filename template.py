import fitz
import random

### COLORS in rgb, 0 --> 1 
## TO-DO: fill in your colors on line 7 onwards. 
## example: my_color = (r, g, b)
MY_FIRST_COLOR = (0,0,0)

### STORE COLORS IN A LIST
## TO-DO: fill in color variables in list
colors = []

### CREATE EMPTY DICTIONARY, NUMBER STRING AND ALPHABET STRING
## do not modify!
values = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

### ASSIGN COLORS TO LETTERS & DIGITS BY RANDOMIZING 
## do not modify!
maxi = len(colors) - 1

for l in alphabet:
    values[l] = colors[random.randint(0,maxi)]

for n in digits:
    values[n] = colors[random.randint(0,maxi)]

### READ IN PDF
## TO-DO: write your pdf path name in the parentheses on line 30
doc = fitz.open("MY_INPUT_PDF.pdf")

for page in doc:

    for key in values:

        ### SEARCH
        text_instances = page.search_for(key)
        
        ### DRAW CIRCLE
        for inst in text_instances:
            circle = page.add_circle_annot(inst)
            circle.set_colors(stroke = values[key], fill = values[key])
            circle.update()

### OUTPUT
## TO-DO: write what name you want your output file to have in line 48
doc.save("MY_OUTPUT_PDF.pdf", garbage=0, deflate=True, clean=True)

