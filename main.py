import tkinter

window = tkinter.Tk()
window.title('Mile to Km converter')
#window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def convert():
    mile = float(entry.get())
    km = round((mile * 1.609344), 2)
    result_label.config(text=str(km))


mile_label = tkinter.Label(text='Miles')
mile_label.grid(column=2, row=0)
km_label = tkinter.Label(text='km')
km_label.grid(column=2, row=1)
equal_label = tkinter.Label(text='is equal to')
equal_label.grid(column=0, row=1)
cal_button = tkinter.Button(text='Calculate', command=convert)
cal_button.grid(column=1, row=2)
entry = tkinter.Entry(justify='center')
entry.insert(tkinter.END, string='enter the miles')
entry.focus()
entry.grid(column=1, row=0)
result_label = tkinter.Label(text='0')
result_label.grid(column=1, row=1)

window.mainloop()
