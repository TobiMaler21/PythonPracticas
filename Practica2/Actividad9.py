valores = [ (['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1),
            (['d', 'g'], 2),
            (['b', 'c', 'm', 'p'], 3),
            (['f', 'h', 'v', 'w', 'y'], 4),
            (['k'], 5),
            (['j', 'x'], 8),
            (['q', 'z'], 10)
            ]
palabra = input('Ingrese una palabra').lower()
score = 0

for i in palabra:
    for n in valores:
        if i in n[0]:
            score = score + n[1]

print (f'puntaje = {score}')             


    
