
palavras_positivas = ["ótimo", "bom", "excelente", "maravilhoso", "gostei", "satisfeito",
    "eficiente", "agradável", "funciona", "recomendo", "feliz",
    "incrível", "perfeito", "rápido", "top"]
palavras_negativas = ["ruim", "péssimo", "lento", "não gostei", "horrível", "insatisfeito",
    "problema", "triste", "erro", "demora", "bugado", "defeito",
    "decepcionado", "inútil", "fraco""]


input = "Meu foi frustrado, porém bom!!"


positivo = sum(1 for palavra in palavras_positivas if palavra in texto.lower())
negativo = sum(1 for palavra in palavras_negativas if palavra in texto.lower())


if positivo > negativo:
    print("Esse texto é positivo!")
elif negativo > positivo:
    print("Esse texto é negativo!")
else:
    print("Esse texto é neutro!")
