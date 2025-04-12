
palavras_positivas = ["feliz", "ótimo", "incrível", "bom", "maravilhoso"]
palavras_negativas = ["triste", "horrível", "péssimo", "terrível", "frustrado"]


input = "Meu foi frustrado, porém bom!!"


positivo = sum(1 for palavra in palavras_positivas if palavra in texto.lower())
negativo = sum(1 for palavra in palavras_negativas if palavra in texto.lower())


if positivo > negativo:
    print("Esse texto é positivo!")
elif negativo > positivo:
    print("Esse texto é negativo!")
else:
    print("Esse texto é neutro!")
