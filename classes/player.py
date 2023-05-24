class Player:
    """
    Класс принимает имя пользователя
    """
    def __init__(self, user_name):
        self.user_name = user_name

        self.list_used_words = []

    def greeting_user(self) -> str:
        """
        Метод просто так, что-бы использовать user_name для приветствия игрока
        :return: str
        """
        return f"Привет, {self.user_name.title()}!"

    def count_words(self) -> int:
        """
        Метод вычисляет длинну списка с отгаданными словами.
        :return: int
        """
        return len(self.list_used_words)

    def add_used_word(self, word):
        """
        Метод добавляет отгаданное слово в список
        :param word: user input
        :return:
        """
        if not self.check_used_word(word):
            self.list_used_words.append(word)

    def check_used_word(self, word) -> bool:
        """
        Метод проверяет введенное слово в списке отгаданых слов
        :param word: user input
        :return: bool
        """
        return word in self.list_used_words
