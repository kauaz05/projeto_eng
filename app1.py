import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Cadastro de Funcionários")

# Define a cor de fundo da janela
janela.configure(bg="#00FF7F")

# Define o tamanho da janela
janela.geometry("1000x900")

# Cria um rótulo com o título do cadastro
rotulo_titulo = tk.Label(janela, text="Cadastro de Funcionários", font=("Arial", 24), bg="#00FF7F", fg="black")
rotulo_titulo.pack(pady=20)

# Cria um frame para agrupar os campos do formulário
frame_formulario = tk.Frame(janela, bg="#00FF7F")
frame_formulario.pack(pady=20)

# Cria um campo de entrada para o nome do funcionário
rotulo_nome = tk.Label(frame_formulario, text="Nome:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_nome.grid(row=0, column=0, padx=10, pady=10)
entrada_nome = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

# Cria um campo de entrada para a data de nascimento do funcionário
rotulo_data_nascimento = tk.Label(frame_formulario, text="Data de Nascimento:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_data_nascimento.grid(row=1, column=0, padx=10, pady=10)
entrada_data_nascimento = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_data_nascimento.grid(row=1, column=1, padx=10, pady=10)

# Cria um campo de entrada para o CPF do funcionário
rotulo_cpf = tk.Label(frame_formulario, text="CPF:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_cpf.grid(row=2, column=0, padx=10, pady=10)
entrada_cpf = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_cpf.grid(row=2, column=1, padx=10, pady=10)

# Cria um campo de entrada para o RG do funcionário
rotulo_rg = tk.Label(frame_formulario, text="RG:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_rg.grid(row=3, column=0, padx=10, pady=10)
entrada_rg = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_rg.grid(row=3, column=1, padx=10, pady=10)

# Cria um campo de entrada para o sexo do funcionário
rotulo_sexo = tk.Label(frame_formulario, text="Sexo:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_sexo.grid(row=4, column=0, padx=10, pady=10)
entrada_sexo = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_sexo.grid(row=4, column=1, padx=10, pady=10)

rotulo_dataad = tk.Label(frame_formulario, text="Data de Admissão:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_dataad.grid(row=5, column=0, padx=10, pady=10)
entrada_dataad = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_dataad.grid(row=5, column=1, padx=10, pady=10)

rotulo_celular = tk.Label(frame_formulario, text="Celular:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_celular.grid(row=6, column=0, padx=10, pady=10)
entrada_celular = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_celular.grid(row=6, column=1, padx=10, pady=10)

rotulo_tel = tk.Label(frame_formulario, text="Telefone:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_tel.grid(row=7, column=0, padx=10, pady=10)
entrada_tel = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_tel.grid(row=7, column=1, padx=10, pady=10)

rotulo_cep = tk.Label(frame_formulario, text="CEP:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_cep.grid(row=8, column=0, padx=10, pady=10)
entrada_cep = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_cep.grid(row=8, column=1, padx=10, pady=10)

rotulo_email = tk.Label(frame_formulario, text="Email:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_email.grid(row=9, column=0, padx=10, pady=10)
entrada_email = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_email.grid(row=9, column=1, padx=10, pady=10)

rotulo_cargo = tk.Label(frame_formulario, text="Cargo:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_cargo.grid(row=10, column=0, padx=10, pady=10)
entrada_cargo = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_cargo.grid(row=10, column=1, padx=10, pady=10)

rotulo_login = tk.Label(frame_formulario, text="Login:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_login.grid(row_=11, column=0, padx=10, pady=10)
entrada_login = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_login.grid(row=11, column=1, padx=10, pady=10)

rotulo_senha = tk.Label(frame_formulario, text="Senha:", font=("Arial", 14), bg="#00FF7F", fg="black")
rotulo_senha.grid(row=12, column=0, padx=10, pady=10)
entrada_senha = tk.Entry(frame_formulario, font=("Arial", 14))
entrada_senha.grid(row=12, column=1, padx=10, pady=10)

botao_criar_cadastro = tk.Button(frame_formulario, text="Criar Cadastro", font=("Arial", 14), bg="#00FF7F", fg="black",)
botao_criar_cadastro.grid(row=16, column=0, columnspan=2, pady=20)



janela.mainloop()


