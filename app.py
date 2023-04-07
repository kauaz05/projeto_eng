import tkinter as tk

# Função para verificar se o usuário e a senha estão corretos
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

# Cria a janela principal
root = tk.Tk()
root.title("Hortifruti")
root.geometry("500x400")
root.configure(background="#6ED088")

# Define as cores e fontes dos widgets
font_label = ("Arial", 12)
font_entry = ("Arial", 10)
color_label = "#6ED088"
color_entry = "#C0C0C0"
color_button = "#32CD32"
color_title = "#6ED088"

# Cria um label para o título
label_title = tk.Label(root, text="HORTIFRUTI KMC", font=("Arial", 24), bg=color_title, fg="black")

# Cria os widgets da tela
label_username = tk.Label(root, text="Usuário", font=font_label, bg=color_label, fg="black")
label_password = tk.Label(root, text="Senha", font=font_label, bg=color_label, fg="black")
entry_username = tk.Entry(root, font=font_entry, bg=color_entry)
entry_password = tk.Entry(root, show="*", font=font_entry, bg=color_entry)
button_login = tk.Button(root, text="Login", font=font_label, bg=color_button, command=login)

# Posiciona os widgets na tela
label_title.place(relx=0.5, rely=0.2, anchor="center")
label_username.place(relx=0.5, rely=0.4, anchor="center")
entry_username.place(relx=0.5, rely=0.5, anchor="center")
label_password.place(relx=0.5, rely=0.6, anchor="center")
entry_password.place(relx=0.5, rely=0.7, anchor="center")
button_login.place(relx=0.5, rely=0.8, anchor="center") 

# Inicia o loop principal da aplicação
root.mainloop()
