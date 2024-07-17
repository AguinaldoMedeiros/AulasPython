"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

secret_word = 'MAMAO'
letter_discovered = ''
trying_number = 0

while True:
    trying_number = trying_number + 1
    secret_word_discovered = ''

    for letter in secret_word:
        if letter in letter_discovered:
            secret_word_discovered += letter
        else:
            secret_word_discovered += '*'

    print(f'{secret_word_discovered}\n')

    if secret_word_discovered == secret_word:
        print("You've figured out the word, congratulations!")
        print('Thank you for play!')
        print(trying_number)
        break

    user_letter = input('Type a letter (or Exit): ')

    user_letter = user_letter.upper()

    if len(user_letter) > 1 and not user_letter == 'EXIT':
        print(f'Type one letter or type "Exit" to exit!\n')
        print(trying_number)
        continue
    elif user_letter == 'EXIT':
        print('Thank you for play!')
        print(trying_number)
        break

    if user_letter in secret_word:
        print(f'letter found\n')
        letter_discovered += user_letter

    print(trying_number)
