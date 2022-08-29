import fitz
import random

### COLORS in rgb, 0 --> 1
black = (0, 0, 0)
pink = (1, 0.8, 0.8)
lilac = (0.9, 0.8, 0.9)
blue = (0.8, 0.9, 1)
mint = (0.8, 1, 0.7)

### STORE COLORS IN A LIST
colors = [black, pink, lilac, blue, mint]

### CREATE EMPTY DICTIONARY & ALPHABET STRING
values = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

### ASSIGN COLORS TO LETTERS BY RANDOMIZING 
for l in alphabet:
    values[l] = colors[random.randint(0,4)]

### READ IN PDF
doc = fitz.open("test_doc_in.pdf")

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
doc.save("test_doc_out.pdf", garbage=0, deflate=True, clean=True)
