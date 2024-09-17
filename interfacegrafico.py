import arquivo as pc
from tkinter import *

main_window = Tk()

main_window.title("Black")
main_window.geometry("500x700")

main_window.grid()

frame = Frame(main_window)
frame.grid()

l_indentif = Label(frame, text="Insira uma mensagem aqui: ")
l_indentif.grid(row=0, column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)

frame2 = Frame(main_window)
frame2.grid(row=1, column=0)

v = StringVar()
Label(frame2, textvariable=v).grid()

nome_maquina = "Black"

v.set("Qual seu nome?")

entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""
historico_conversa = ""

def roda_Chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario

    texto = e_mensagem.get()
    e_mensagem.delete(0, END)  # Limpa o campo de entrada após pegar o texto

    if entrada_nome_usuario:
        nome_usuario = texto
        saudacao = pc.saudacao(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        entrada_nome_usuario = False
    else:
        historico_conversa += "\n" + nome_usuario + ": " + texto
        if entrada_sugestao:
            pc.salvar_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\n Agora aprendi! Vamos continuar nossa conversa... \n"
        else:
            resposta = pc.buscaResposta("Cliente: " + texto + "\n")
            if resposta == "Me desculpe, não sei o que falar":
                historico_conversa += "\nMe desculpe, não sei o que falar. O que você esperava? \n"
                entrada_sugestao = True
            else:
                historico_conversa += "\n" + pc.exibeResposta(texto, resposta, nome_maquina)
                v.set(historico_conversa)
    
    v.set(historico_conversa)

Button(frame, text="Clique", command=roda_Chatbot).grid(row=0, column=2)

main_window.mainloop()
