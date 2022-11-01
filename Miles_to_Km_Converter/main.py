import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window["background"] = "#DDD"

# MILE ENTRY
mile_input = tkinter.Entry(width=10, relief="solid", )
mile_input.grid(column=1, row=0)

# MILE LABEL
mile_label = tkinter.Label(text="Mile", background="#DDD", font=("JetBrains Mono", 8, "bold"))
mile_label.grid(column=2, row=0)

# is equal to LABEL
is_equal = tkinter.Label(text="is equal to", background="#DDD", font=("JetBrains Mono", 8, "bold"))
is_equal.grid(column=0, row=1)

# CONVERTED MILES
miles_to_km = tkinter.Label(text="", background="#DDD", font=("JetBrains Mono", 8, "bold"))
miles_to_km.grid(column=1, row=1)

# KM LABEL
km_label = tkinter.Label(text="Km", background="#DDD", font=("JetBrains Mono", 8, "bold"))
km_label.grid(column=2, row=1)


# CALCULATE BUTTON
def miles_km_convert():
    miles_to_km["text"] = f"{round(int(mile_input.get()) * 1.609)}"


calculate = tkinter.Button(text="Calculate", command=miles_km_convert)
calculate.grid(column=1, row=2)

# KEEP AT END OF PROGRAM!
window.mainloop()
