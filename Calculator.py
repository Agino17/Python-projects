#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


def add_to_textbox(END,value):
    textbox.insert(END, value)


# In[4]:


window =Tk()
window.title('Calculator')
window.geometry('350x250')

textbox =Text(window, height=3, width=40)
textbox.grid(row=0, column=0, columnspan=6)

button1=Button(window, text='1', width=10, command=lambda: add_to_textbox(END,'1'))
button1.grid(row=1, column=0, pady=5)
button2=Button(window, text='2', width=10, command=lambda: add_to_textbox(END,'2'))
button2.grid(row=1, column=1, pady=5)
button3=Button(window, text='3', width=10, command=lambda: add_to_textbox(END,'3'))
button3.grid(row=1, column=2, pady=5)
button4=Button(window, text='+', width=10, command=lambda: add_to_textbox(END,'+')) 
button4.grid(row=1, column=3, pady=5)
button5=Button(window, text='4', width=10, command=lambda: add_to_textbox(END,'4'))  
button5.grid(row=2, column=0, pady=5)
button6=Button(window, text='5', width=10, command=lambda: add_to_textbox(END,'5'))  
button6.grid(row=2, column=1, pady=5)
button7=Button(window, text='6', width=10, command=lambda: add_to_textbox(END,'6'))  
button7.grid(row=2, column=2, pady=5)
button8=Button(window, text='-', width=10, command=lambda: add_to_textbox(END,'-'))  
button8.grid(row=2, column=3, pady=5)
button9=Button(window, text='7', width=10, command=lambda: add_to_textbox(END,'7'))  
button9.grid(row=3, column=0, pady=5)
button10=Button(window, text='8', width=10, command=lambda: add_to_textbox(END,'8'))  
button10.grid(row=3, column=1, pady=5)
button11=Button(window, text='9', width=10, command=lambda: add_to_textbox(END,'9'))  
button11.grid(row=3, column=2, pady=5)
button12=Button(window, text='*', width=10, command=lambda: add_to_textbox(END,'*'))  
button12.grid(row=3, column=3, pady=5)
button13=Button(window, text='Clear', font=('bold', 10), width=10, command=lambda: textbox.delete("1.0", END))
button13.grid(row=4, column=0, pady=5)
button14=Button(window, text='0', width=10, command=lambda: add_to_textbox(END,'0'))
button14.grid(row=4, column=1, pady=5)
button15=Button(window, text='.', width=10, command=lambda: add_to_textbox(END,'.'))
button15.grid(row=4, column=2, pady=5)
button16=Button(window, text='/', width=10, command=lambda: add_to_textbox(END,'/'))
button16.grid(row=4, column=3, pady=5)
button17=Button(window, text='Backspace', width=10, command=lambda: textbox.delete("end-2c", END))
button17.grid(row=5, column=0, pady=5)
equal_button = Button(window, text='=', width=10, command=lambda: textbox.insert(END, " = " + str(eval(textbox.get("1.0", "end-1c")))))
equal_button.grid(row=5, column=1, pady=5)


window.mainloop()


# In[ ]:




