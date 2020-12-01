import tkinter as tk


def ao_clicar_ok():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    op = operacao.get()

    res = None
    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        res = num1 / num2
    else:
        res = None

    if res == None:
        resultado["text"] = "Operação inválida"
    else:
        resultado["text"] = "Resultado: " + str(res)


window = tk.Tk()
window.geometry('500x250')
window.title('Minha Aplicação')

msg = tk.Label(text="Digite dois números para calcular")
msg.pack(pady=5, padx=5)

numero1 = tk.Entry(width=20)
numero1.pack(pady=5, padx=5)

operacao = tk.Entry(width=4)
operacao.pack(pady=5, padx=5)

numero2 = tk.Entry(width=20)
numero2.pack(pady=5, padx=5)

ok = tk.Button(text="Calcular", command=ao_clicar_ok)
ok.pack(pady=5, padx=5)

resultado = tk.Label(text="")
resultado.pack(pady=5, padx=5)

window.mainloop()
