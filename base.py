import fitz
import random

### COLORS in rgb, 0 --> 1
salmon = (0.1176, 0.3255, 0.4000)
pink = (0.1451, 0.4275, 0.5059)
cream = (0.0000, 0.0588, 0.1490)
dark_br = (0.5686, 0.7137, 0.7529)
brown = (0.3373, 0.5843, 0.7882)

### STORE COLORS IN A LIST
colors = [salmon, pink, cream, dark_br, brown]

### CREATE EMPTY DICTIONARY & ALPHABET STRING
values = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

### ASSIGN COLORS TO LETTERS BY RANDOMIZING 
for l in alphabet:
    values[l] = colors[random.randint(0,4)]

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

