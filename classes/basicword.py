class BasicWord:
    """
    Класс принимает оригинальное слово и список слов которые можно составить.
    """
    def __init__(self, original_word, sub_words):
        self.original_word = original_word
        self.sub_words = sub_words

    def checking_enter_word(self, word) -> bool:
        """
        Функция принимает ввод пользователя и проверят наличие слова в списке
        :param word: input users
        :return: bool
        """
        return word in self.sub_words

    def count_sub_words(self) -> int:
        """
        Функция проверяет длинну списка слов
        :return: int
        """
        return len(self.sub_words)
