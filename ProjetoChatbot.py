import arquivo as pc
nome_maquina = "Black"
pc.saudacao(nome_maquina)
while True:
    texto = pc.recebeTexto()
    resposta = pc.buscaResposta("client :"+texto+"\n")
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break