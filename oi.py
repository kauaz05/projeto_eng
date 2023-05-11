import tkinter as tk
from typing import Self

class GerenciamentoEstoque(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Gerenciamento de Estoque")
        self.grid(row=0, column=0, sticky="nsew")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.create_widgets()
        self.config(bg="#00FF7F")

    def create_widgets(self):
        # rótulos
        tk.Label(self, text="ID do Produto").grid(row=0, column=0)
        tk.Label(self, text="Nome do Produto").grid(row=1, column=0)
        tk.Label(self, text="Quantidade").grid(row=2, column=0)
        tk.Label(self, text="Preço").grid(row=3, column=0)

        # campos de entrada
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1)
        self.produto_entry = tk.Entry(self)
        self.produto_entry.grid(row=1, column=1)
        self.quantidade_entry = tk.Entry(self)
        self.quantidade_entry.grid(row=2, column=1)
        self.preco_entry = tk.Entry(self)
        self.preco_entry.grid(row=3, column=1)

        # botões
        tk.Button(self, text="Adicionar", command=self.adicionar_produto).grid(row=5, column=0, sticky=tk.W)
        tk.Button(self, text="Remover", command=self.remover_produto).grid(row=5, column=1, sticky=tk.W)
        tk.Button(self, text="Alterar", command=self.alterar_produto).grid(row=5, column=2, sticky=tk.W)
        tk.Button.config(self, bg="#E0E0E0")

        # lista de produtos
        self.lista_produtos = tk.Listbox(self)
        self.lista_produtos.grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)
        self.lista_produtos.rowconfigure(0, weight=1)
        self.lista_produtos.columnconfigure(0, weight=1)
        self.lista_produtos.config(bg="#E0E0E0")

        self.text_produtos = tk.Text(self)
        self.text_produtos.grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S)
        self.text_produtos.config(bg="#00FF7F")

    def adicionar_produto(self):
        id_produto = self.id_entry.get()
        produto = self.produto_entry.get()
        quantidade = self.quantidade_entry.get()
        preco = self.preco_entry.get()

        if id_produto and produto and quantidade and preco:
            self.lista_produtos.insert(tk.END, f"ID: {id_produto} | {produto}: {quantidade} unidades | Preço: R${preco}")
            self.id_entry.delete(0, tk.END)
            self.produto_entry.delete(0, tk.END)
            self.quantidade_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)

    def remover_produto(self):
        selection = self.lista_produtos.curselection()

        if selection:
            self.lista_produtos.delete(selection)

    def alterar_produto(self):
        
        selection = self.lista_produtos.curselection()

        if selection:
        
            item = self.lista_produtos.get(selection[0])
            id_produto = item.split(" | ")[0].split(": ")[1]
            produto = item.split(" | ")[1].split(": ")[1].split(" unidades")[0]
            preco = item.split(" | ")[2].split(": ")[1].split("R$")[1]

            self.id_entry.delete(0, tk.END)
            self.produto_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)

            self.id_entry.insert(0, id_produto)
            self.produto_entry.insert(0, produto)
            self.preco_entry.insert(0, preco)

            # Não é necessário modificar a quantidade
            # self.quantidade_entry.delete(0, tk.END)
            # self.quantidade_entry.insert(0, quantidade)

            self.lista_produtos.delete(selection[0])



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = GerenciamentoEstoque(master=root)
    app.pack(expand=True, fill=tk.BOTH)
    app.mainloop()


            


