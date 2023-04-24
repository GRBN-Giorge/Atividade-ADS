#1049
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

t1 = input('Termo 1: ')
t2 = input('Termo 2: ')
t3 = input('Termo 3: ')

animais = {
    'vertebrado': {
        'ave': {
            'canivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
    'anelideo': {
        'hematofago': 'sanguessuga',
        'onivoro': 'minhoca'
        }
    }
}

print(animais[t1][t2][t3])