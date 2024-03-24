import pytest

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

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    def test_set_book_genre_existing_genre(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)
        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        assert collector.books_genre == {name: genre}

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастический'],
        ]
    )
    # 2 тест. Добавить жанр книги которого нет в списке
    # books_genre и genre
    def test_set_book_genre_nonexistent_genre(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги которой нет в списке
        collector.set_book_genre(name, genre)

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # проверяем, что жанр не добавился
        assert collector.books_genre == {name: ''}

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    # 3 тест. Добавить жанр без книги
    # books_genre и genre
    def test_set_book_genre_no_book(self, name, genre):
        collector = BooksCollector()

        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # проверяем, что жанр не добавился
        assert collector.books_genre == {}

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    # 4 тест. Проверка вывода жанра книги
    def test_get_book_genre_correct_genre(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)
        # Получаем жанр по названию книги
        get_book_genre = collector.get_book_genre(name)

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.get_book_genre(name))

        # Проверяем, что жанр "Фантастика"
        assert get_book_genre == 'Фантастика'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    # 5 тест. Проверка вывода книг с определённым жанром
    def test_get_books_with_specific_genre_fantasy(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)
        # выводим список книг с определенным жанром
        get_books_genre = collector.get_books_with_specific_genre(genre)

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.get_books_with_specific_genre(genre))

        # Проверяем, что фильм "Гордость и предубеждение и зомби 2"
        assert get_books_genre == ['Гордость и предубеждение и зомби 2']

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    # 6 тест. Проверка вывода cловаря books_genre
    def test_get_books_genre_output_validation(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Выводим содержимое словаря books_genre, это просто для себя, дебаг :))
        print(collector.books_genre)

        # Проверяем, что выводятся данные из словаря books_genre
        assert collector.books_genre == {name: genre}

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби 2', 'Фантастика'],
        ]
    )
    # 7 тест. Проверка, что возвращаются книги, подходящие детям
    def test_get_books_for_children_output_validation(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Получаем результат с помощью тестируемого метода
        actual_result = collector.get_books_for_children()

        # это просто для себя, дебаг :))
        print(actual_result)

        assert actual_result == ['Гордость и предубеждение и зомби 2']

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Оно', 'Ужасы'],
        ]
    )
    # 8 тест. Проверка, что не возвращаются книги, не подходящие детям
    def test_get_books_for_children_negative_genre_shows_no_result(self, name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Получаем результат с помощью тестируемого метода
        actual_result = collector.get_books_for_children()

        # это просто для себя, дебаг :))
        print(actual_result)

        # Проверяем, что ничего не выведено
        assert actual_result == []

    # 9 тест. Добавляем товар в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()

        favorites = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(favorites)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(favorites)

        # это просто для себя, дебаг :))
        print(favorites)

        # проверяем, что книга добавилась в избранное
        assert 'Гордость и предубеждение и зомби 2' in collector.favorites

    # 10 тест. Удаляем книгу из избранного
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(name)

        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites(name)

        # это просто для себя, дебаг :))
        print(collector.favorites)

        assert 'Гордость и предубеждение и зомби 2' not in collector.favorites

    # 11 тест. Получаем список Избранных книг
    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()

        book_name = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(book_name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(book_name)

        # получаем список избранных книг
        favorites_list = collector.get_list_of_favorites_books()

        # это просто для себя, дебаг :))
        print(favorites_list)

        # проверяем, что книга добавилась в избранное
        assert book_name in favorites_list
