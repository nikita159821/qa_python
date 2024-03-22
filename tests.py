from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # 1 тест. Добавить название книги и жанр, который есть в списке
    # books_genre и genre
    def test_set_book_genre_existing_genre(self):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        # добавляем жанр книги
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Фантастика')

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        assert collector.books_genre == {'Гордость и предубеждение и зомби 2': 'Фантастика'}

    # 2 тест. Добавить жанр книги которого нет в списке
    # books_genre и genre
    def test_set_book_genre_nonexistent_genre(self):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        # добавляем жанр книги которой нет в списке
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Фантастический')

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # проверяем, что жанр не добавился
        assert collector.books_genre == {'Гордость и предубеждение и зомби 2': ''}

    # 3 тест. Добавить жанр без книги
    # books_genre и genre
    def test_set_book_genre_no_book(self):
        collector = BooksCollector()

        # добавляем жанр книги
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Фантастика')

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # проверяем, что жанр не добавился
        assert collector.books_genre == {}
