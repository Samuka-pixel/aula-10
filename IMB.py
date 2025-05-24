from tkinter import *
from tkinter import messagebox

def calcular_bmi():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        bmi = peso / (altura ** 2)
        resultado = f"BMI: {bmi:.2f} - {classificar_bmi(bmi)}"
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def classificar_bmi(bmi):
    if bmi < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= bmi < 25:
        return "Peso normal"
    elif 25 <= bmi < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

janela = Tk()
janela.title("Calculadora de BMI")

Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_peso = Entry(janela)
entrada_peso.grid(row=0, column=1, padx=10, pady=5)

Label(janela, text="Altura (m):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_altura = Entry(janela)
entrada_altura.grid(row=1, column=1, padx=10, pady=5)

botao_calcular = Button(janela, text="Calcular BMI", command=calcular_bmi)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = Label(janela, text="BMI: ")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

janela.mainloop()
