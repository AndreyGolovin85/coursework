import requests
from random import shuffle
from classes.basicword import BasicWord
from classes.player import Player


def load_random_word() -> dict:
    """
    Функция из внешнего источника загружает игровые слова.
    :return: dict
    """
    load_word = requests.get("https://jsonkeeper.com/b/RIYJ")
    list_word = eval(load_word.text)
    shuffle(list_word)
    return list_word[0]


def main():
    """
    Главная игровая функция.
    :return:
    """
    game_dict = load_random_word()
    word = game_dict["word"]
    subwords = game_dict["subwords"]
    basic_word = BasicWord(word, subwords)
    print("Ввведите имя игрока:")
    user_name = input()
    player = Player(user_name)
    print(player.greeting_user())
    print(f"Составьте {len(basic_word.sub_words)} слов из слова {basic_word.original_word.upper()}")
    print(f"Слова должны быть не короче {len(basic_word.sub_words[3])} букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'стоп'")
    print("Поехали, ваше первое слово?")
    
    for word in basic_word.sub_words:
        answer = input()
        if answer == "стоп":
            break
        else:
            if answer in player.list_used_words:
                print("Это слово уже было!")
            elif basic_word.checking_enter_word(answer):
                print("Верно!")
                player.add_used_word(answer)
            else:
                print("Неверно, попробуйте ещё!")

    print("Слова закончились, игра завершена!")
    print(f"вы угадали {player.count_words()} слов!")
