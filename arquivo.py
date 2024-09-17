def exibeResposta(texto, resposta, nome):
    return resposta.replace("Chatbot", nome)

def saudacao(Black):
    import random
    frases = ["Bom dia, meu nome é Black", "Como vai?", "tudo bem?"]
    return frases[random.randint(0,2)]

def salvar_sugestao(sugestao):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")

def buscaResposta(texto):
    with open("BaseDeConhecimento.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "": 
                if jaccard(texto,viu) > 0.3:
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write(texto)
                return "Me desculpe, não sei o que falar"
                
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavra_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavra_em_comum += 1
        return palavra_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase


def recebeTexto(texto):
    texto = "Cliente: " + input("Cliente: ")
    palavraProibida = ["burro", 'corno', "desgraçado", "caralho", "viado"]
    for p in palavraProibida:
        if p in texto:
            print("Olha boca se não vou seguir você até o inferno")
            return recebeTexto()
        return texto