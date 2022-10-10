import fitz
import random

### COLORS in rgb, 0 --> 1 
salmon = (0.8, 0.4, 0.4)
pink = (0.9, 0.5, 0.7)
cream = (0.9, 0.9, 0.9)
dark_br = (0.4, 0.1, 0.1)
brown = (0.7, 0.5, 0)

### STORE COLORS IN A LIST
colors = [salmon, pink, cream, dark_br, brown]

### CREATE EMPTY DICTIONARY & ALPHABET STRING
values = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

### ASSIGN COLORS TO LETTERS BY RANDOMIZING 
for l in alphabet:
    values[l] = colors[random.randint(0,4)]

for n in digits:
    values[n] = colors[random.randint(0,4)]

### READ IN PDF
doc = fitz.open("emrata.pdf")

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
doc.save("emrata_out.pdf", garbage=0, deflate=True, clean=True)

