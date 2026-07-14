from tkinter import *
from pricing import *

def validate(value):
    if value == "":
        return True

    if value.count(".") > 1:
        return False

    allowed = "0123456789."

    return all(char in allowed for char in value)

window = Tk()

vcmd = (window.register(validate), "%P")

window.title("Calculadora de Preço 3D")
window.configure(bg="#1e1e1e")

# window.geometry("400x400")

guidance_text = Label(
    window,
    text="Programa para auxiliar no preço de peças 3D",
    bg="#1e1e1e",
    fg="white"
)
guidance_text.grid(column=2, row=0)

filament_label_text = Label(
    window,
    text="Filamento",
    bg="#1e1e1e",
    fg="#4CAF50"
)
filament_label_text.grid(column=0, row=1)

price_filament_text = Label(
    window,
    text="Preço do Quilo(Kg) do filamento:",
    bg="#1e1e1e",
    fg="white"
)
price_filament_text.grid(column=1, row=2)

filament_value = Entry(
    window,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    validate="key",
    validatecommand=vcmd
)
filament_value.grid(column=1, row=3)

filament_quatity_text = Label(
    window,
    text="Quantidade de filamento utilizada em grama",
    bg="#1e1e1e",
    fg="white"
)
filament_quatity_text.grid(column=2, row=2)

filament_quatity_value = Entry(
    window,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    validate="key",
    validatecommand=vcmd
)
filament_quatity_value.grid(column=2, row=3)

energy_label_text = Label(
    window,
    text="Tempo e Energia",
    bg="#1e1e1e",
    fg="#4CAF50"
)
energy_label_text.grid(column=0, row=4)

price_watts_text = Label(
    window,
    text="Consumo da impressora em Watts",
    bg="#1e1e1e",
    fg="white"
)
price_watts_text.grid(column=1, row=5)

price_watts_value = Entry(
    window,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    validate="key",
    validatecommand=vcmd
)
price_watts_value.grid(column=1, row=6)

khw_text = Label(
    window,
    text="Valor do kWh",
    bg="#1e1e1e",
    fg="white"
)
khw_text.grid(column=2, row=5)

khw_text_value = Listbox(
    window,
    height=3,
    bg="#2d2d2d",
    fg="white",
    selectbackground="#4CAF50",
    selectforeground="white",
    selectmode="single",
    exportselection=False
)

khw_text_value.insert(0, "Bandeira verde")
khw_text_value.insert(1, "Bandeira amarela")
khw_text_value.insert(2, "Bandeira vermelha")
khw_text_value.grid(column=2, row=6)

time_print_text = Label(
    window,
    text="Tempo de impressão",
    bg="#1e1e1e",
    fg="white"
)
time_print_text.grid(column=3, row=5)

time_print_value = Spinbox(
    window,
    from_=0.0,
    to=48,
    bg="#2d2d2d",
    fg="white",
    buttonbackground="#4CAF50",
    validate="key",
    validatecommand=vcmd
)
time_print_value.grid(column=3, row=6)

optional_label_text = Label(
    window,
    text="Opcionais",
    bg="#1e1e1e",
    fg="#4CAF50"
)
optional_label_text.grid(column=0, row=7)

fixed_cost_text = Label(
    window,
    text="Custos Fixos",
    bg="#1e1e1e",
    fg="white"
)
fixed_cost_text.grid(column=1, row=8)

fixed_cost_value = Entry(
    window,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    validate="key",
    validatecommand=vcmd
)
fixed_cost_value.grid(column=1, row=9)

labor_text = Label(
    window,
    text="Mão de obra",
    bg="#1e1e1e",
    fg="white"
)
labor_text.grid(column=2, row=8)

labor_value = Entry(
    window,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    validate="key",
    validatecommand=vcmd
)
labor_value.grid(column=2, row=9)

profit_margin_text = Label(
    window,
    text="Margem de lucro",
    bg="#1e1e1e",
    fg="white"
)
profit_margin_text.grid(column=3, row=8)

profit_margin_value = Listbox(
    window,
    height=3,
    bg="#2d2d2d",
    fg="white",
    selectbackground="#4CAF50",
    selectforeground="white",
    exportselection=False
)

profit_margin_value.insert(1, "10%")
profit_margin_value.insert(2, "20%")
profit_margin_value.insert(3, "30%")
profit_margin_value.insert(4, "40%")
profit_margin_value.insert(5, "50%")
profit_margin_value.insert(6, "60%")
profit_margin_value.insert(7, "70%")
profit_margin_value.insert(8, "80%")
profit_margin_value.insert(9, "90%")
profit_margin_value.insert(10, "100%")
profit_margin_value.insert(11, "150%")
profit_margin_value.insert(12, "200%")
profit_margin_value.insert(13, "250%")
profit_margin_value.insert(14, "300%")
profit_margin_value.insert(15, "350%")
profit_margin_value.insert(16, "400%")
profit_margin_value.insert(17, "450%")
profit_margin_value.insert(18, "500%")

profit_margin_value.grid(column=3, row=9)

send_button = Button(
    window,
    text="Calcular valores",
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    relief="raised",
    padx=10,
    pady=5,
    command=lambda: calculate_value(
        filament_value.get(),
        filament_quatity_value.get(),
        price_watts_value.get(),
        khw_text_value.get(khw_text_value.curselection()[0]),
        time_print_value.get(),
        fixed_cost_value.get(),
        labor_value.get(),
        profit_margin_value.get(
            profit_margin_value.curselection()[0]
        )
        )
)
send_button.grid(column=2, row=10)


window.mainloop()