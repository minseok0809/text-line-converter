import re
import clipboard
from tkinter import *

def get_original_line(): 

    original_line = clipboard.paste()

    return original_line

def get_case_sensitive_line(text, prepositions): 

    case_sensitive_line = ""
    words = re.split(' |\n|\r', text)

    for word in words:
        if any(word.lower() == preposition for preposition in prepositions):
            word = word.lower()
        else:
            word = word[:1].upper() + word[1:].lower() 
        case_sensitive_line += word + " " 
    
    case_sensitive_line = ' '.join(case_sensitive_line.split())
    case_sensitive_line = case_sensitive_line.strip() 

    return case_sensitive_line

def get_one_line(text): 

    one_line = ""
    words = text.replace("\n", " ")
    words = words.replace("\r", " ")

    if type(words) == list:
        for word in words:
            one_line += word 

    elif type(words) != list:
        one_line = words

    one_line = ' '.join(one_line.split())
    one_line = one_line.strip() 

    return one_line

def get_clean_line(text):

    clean_line = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', text)

    return clean_line   

def entry_line():        

    prepositions = ['aboard', 'about', 'above', 'across', 'after', 'against', 
            'along', 'amid', 'among', 'anti', 'around', 'as', 'at', 
            'before', 'behind', 'below', 'beneath', 'beside', 'besides', 
            'between', 'beyond', 'but', 'by', 'concerning', 'considering', 
            'despite', 'down', 'during', 'except', 'excepting', 'excluding', 
            'following', 'for', 'from', 'in', 'inside', 'into', 'like', 'minus',
            'near', 'of', 'off', 'on', 'onto', 'opposite', 'outside', 'over',
            'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than', 
            'through', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike', 
            'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without']

    original_line = get_original_line()
    case_sensitive_line = get_case_sensitive_line(original_line, prepositions)
    one_line = get_one_line(original_line)
    clean_line = get_clean_line(original_line)

    e1.delete(0, len(e1.get()))             
    e1.insert(0, original_line)  

    e2.delete(0, len(e2.get()))             
    e2.insert(0, case_sensitive_line)       

    e3.delete(0, len(e3.get()))             
    e3.insert(0, one_line)       

    e4.delete(0, len(e4.get()))             
    e4.insert(0, clean_line)  

    return case_sensitive_line, one_line, clean_line

def case_senstive():    
    case_sensitive_line, one_line, clean_line = entry_line()
    clipboard.copy(case_sensitive_line)

def one():    
    case_sensitive_line, one_line, clean_line = entry_line()
    clipboard.copy(one_line)

def clean():    
    case_sensitive_line, one_line, clean_line = entry_line()
    clipboard.copy(clean_line)

    
window = Tk()
window.title('Text Line Converter')
window_width = 800
window_height = 500
window_pos_x = 700
window_pos_y = 100
window.geometry("{}x{}+{}+{}".format(window_width, window_height, window_pos_x, window_pos_y))
window.resizable(width=False, height=False)

l1 = Label(window, text = 'Text Line Converter', fg = 'orange', font = 'helvetica 16 bold')
l2 = Label(window, text = 'Original Line ')
l3 = Label(window, text = 'Case Sensitive Line ')
l4 = Label(window, text = 'One Line ')
l5 = Label(window, text = 'Clean Line ')
l6 = Label(window, text = 'Copy Machine')
l1.place(x=20, y=10)
l2.place(x=20, y=60)
l3.place(x=20, y=140)
l4.place(x=20, y=220)
l5.place(x=20, y=300)
l6.place(x=20, y=380)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e1.place(x=175, y=60, width=400, height=50)
e2.place(x=175, y=140, width=400, height=50)
e3.place(x=175, y=220, width=400, height=50)
e4.place(x=175, y=300, width=400, height=50)

b1 = Button(window, text = "Case Sensitive Line", command=case_senstive)  
b2 = Button(window, text = "One Line", command=one)   
b3 = Button(window, text = "Clean Line", command=clean)
b1.place(x=20, y=420)
b2.place(x=155, y=420)
b3.place(x=240, y=420)
window.mainloop()