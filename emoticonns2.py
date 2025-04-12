
sentiment_dict = {
    "feliz": 2,
    "ótimo": 3,
    "incrível": 4,
    "bom": 2,
    "maravilhoso": 5,
    "triste": -2,
    "horrível": -4,
    "péssimo": -3,
    "terrível": -5,
    "frustrado": -3
}


texto = "péssimo e ótimo ao mesmo tempo!"


score = sum(sentiment_dict.get(palavra, 0) for palavra in texto.lower().split())

# Análise final
if score > 5:
    print("Esse texto é muito positivo!")
elif 1 <= score <= 5:
    print("Esse texto é positivo!")
elif -5 <= score <= -1:
    print("Esse texto é negativo!")
elif score < -5:
    print("Esse texto é muito negativo!")
else:
    print("Esse texto é neutro!")
