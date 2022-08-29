import fitz

### COLORS in rgb, 0 --> 1
black = (0, 0, 0)
pink = (1, 0.8, 0.8)
lilac = (0.9, 0.8, 0.9)
blue = (0.8, 0.9, 1)
mint = (0.8, 1, 0.7)


### READ IN PDF
doc = fitz.open("test_doc_in.pdf")

for page in doc:
    ### SEARCH
    text = "a" 
    text_instances = page.search_for(text) 

    text2 = "t"
    text2_instances = page.search_for(text2)

    ### DRAW CIRCLE
    for inst in text_instances:
        circle = page.add_circle_annot(inst)
        circle.set_colors(stroke = blue, fill = blue)
        circle.update()
    
    for inst2 in text2_instances:
        circle2 = page.add_circle_annot(inst2)
        circle2.set_colors(stroke = pink, fill = pink)
        circle2.update()

### OUTPUT
doc.save("test_doc_out.pdf", garbage=0, deflate=True, clean=True)
