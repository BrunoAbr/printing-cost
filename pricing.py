from tkinter import *
from tkinter import messagebox


def calculate_value(
        filament_value,
        filament_quatity_value,
        price_watts_value,
        khw_text_value,
        time_print_value,
        fixed_cost_value,
        labor_value,
        profit_margin_value
):
    if not all([
        filament_value,
        filament_quatity_value,
        price_watts_value,
        khw_text_value,
        time_print_value
    ]):
        messagebox.showinfo(
            "Aviso",
            message="Existem campos obrigatórios vazios."
        )
        return

    flags = {
        "Bandeira verde": 0.85,
        "Bandeira amarela": 0.87,
        "Bandeira vermelha": 0.90
    }

    try:
        #Margem de lucro
        profit_margin = float(
            profit_margin_value.replace("%", "")
        ) / 100

        #Custos opcionais
        fixed_cost = (
            float(fixed_cost_value)
            if fixed_cost_value else 0
        )

        labor_cost = (
            float(labor_value)
            if labor_value else 0
        )

        #Valor do kWh conforme bandeira
        khw_price = flags.get(khw_text_value, 0.87)

        #Filamento
        filament_price_per_gram = (
            float(filament_value) / 1000
        )

        filament_cost = (
            filament_price_per_gram *
            float(filament_quatity_value)
        )

        #Energia
        energy_consumption = (
            float(price_watts_value) *
            float(time_print_value)
        ) / 1000

        energy_cost = (
            energy_consumption *
            khw_price
        )

        #Soma dos custos
        total_cost = (
            filament_cost +
            energy_cost +
            fixed_cost +
            labor_cost
        )

        #margem de lucro
        final_price = total_cost * (1 + profit_margin)

        top_lv = Toplevel()
        top_lv.title("Resultado")
        top_lv.geometry("350x300")
        top_lv.configure(bg="#1e1e1e")

        Label(
            top_lv,
            text="Resultado do orçamento",
            bg="#1e1e1e",
            fg="#4CAF50",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        Label(
            top_lv,
            text=f"Filamento: R$ {filament_cost:.2f}",
            bg="#1e1e1e",
            fg="white"
        ).pack()

        Label(
            top_lv,
            text=f"Energia: R$ {energy_cost:.2f}",
            bg="#1e1e1e",
            fg="white"
        ).pack()

        Label(
            top_lv,
            text=f"Custos Fixos: R$ {fixed_cost:.2f}",
            bg="#1e1e1e",
            fg="white"
        ).pack()

        Label(
            top_lv,
            text=f"Mão de Obra: R$ {labor_cost:.2f}",
            bg="#1e1e1e",
            fg="white"
        ).pack()

        Label(
            top_lv,
            text=f"Custo Total: R$ {total_cost:.2f}",
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=10)

        Label(
            top_lv,
            text=f"Preço Final: R$ {final_price:.2f}",
            bg="#1e1e1e",
            fg="#4CAF50",
            font=("Arial", 12, "bold")
        ).pack()

    except ValueError:
        messagebox.showwarning(
            "Aviso",
            message="Houve um erro. Verifique os valores informados."
        )