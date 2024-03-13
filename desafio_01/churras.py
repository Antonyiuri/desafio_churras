#Desafio com If, Elif, Else 

'''
Crie um programa que dependendo da temperatura (em celcius) do stake 
ele retorna o ponto do cozimento em portugues. O usuário deverá 
fornocer a temperatura.

Temperaturas - cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium Well done (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''
#Desafio Crurras de domingo!
temperatura = float(input("Qual é a temperatura da carne?" ).replace(',','.'))
if temperatura < 48: print('crua')
elif temperatura >= 48 and temperatura< 54: print('Selada')
elif temperatura >= 54 and temperatura< 60: print('Ao ponto para mal')
elif temperatura >= 60 and temperatura< 65: print('Ao ponto')
elif temperatura >= 65 and temperatura< 71: print('Ao ponto para o bem')
elif temperatura >= 71 and temperatura< 76: print('Bem passada')
else: print('queimou a carne')

