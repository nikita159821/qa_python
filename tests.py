import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # 1 тест. Добавить название книги и жанр, который есть в списке
    # books_genre и genre

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Гордость и предубеждение и зомби 2','Фантастика'],
                                 ['Оно', 'Ужасы'],
                                 ['Звонок', 'Ужасы']
                             ]
    )
    def test_set_book_genre_existing_genre(self,name, genre):
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == {name: genre}

    # 2 тест. Добавить жанр книги которого нет в списке
    # books_genre и genre
    def test_set_book_genre_nonexistent_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'
        genre = 'Фантастический'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги которой нет в списке
        collector.set_book_genre(name, genre)

        # проверяем, что жанр не добавился
        assert collector.get_books_genre() == {name: ''}


    # 3 тест. Добавить жанр без книги
    # books_genre и genre
    def test_set_book_genre_no_book(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'
        genre = 'Фантастика'

        # добавляем жанр книги
        collector.set_book_genre(name,genre)

        # проверяем, что жанр не добавился
        assert collector.get_books_genre() == {}


    # 4 тест. Проверка вывода жанра книги
    def test_get_book_genre_correct_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'
        genre = 'Фантастика'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)
        # Получаем жанр по названию книги
        collector.get_book_genre(name)

        # Проверяем, что жанр "Фантастика"
        assert collector.books_genre.get(name) == 'Фантастика'


    # 5 тест. Проверка вывода книг с определённым жанром
    def test_get_books_with_specific_genre_fantasy(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'
        genre = 'Фантастика'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)
        # выводим список книг с определенным жанром
        get_books_genre = collector.get_books_with_specific_genre(genre)

        # Проверяем, что фильм "Гордость и предубеждение и зомби 2"
        assert get_books_genre == ['Гордость и предубеждение и зомби 2']

    # 6 тест. Проверка, что возвращаются книги, подходящие детям
    def test_get_books_for_children_output_validation(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'
        genre = 'Фантастика'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Получаем результат с помощью тестируемого метода
        actual_result = collector.get_books_for_children()

        assert actual_result == ['Гордость и предубеждение и зомби 2']


    # 7 тест. Проверка, что не возвращаются книги, не подходящие детям
    def test_get_books_for_children_negative_genre_shows_no_result(self):
        collector = BooksCollector()
        name = 'Оно'
        genre = 'Ужасы'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книги
        collector.set_book_genre(name, genre)

        # Получаем результат с помощью тестируемого метода
        actual_result = collector.get_books_for_children()


        # Проверяем, что ничего не выведено
        assert actual_result == []


    # 8 тест. Добавляем книгу в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)

        # проверяем, что книга добавилась в избранное
        assert collector.get_list_of_favorites_books() == [name]

    # 9 тест. Удаляем книгу из избранного
    def test_delete_book_from_favorites_success(self,):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites(name)


        assert collector.get_list_of_favorites_books() == []


    # 10 тест. Получаем список Избранных книг
    def test_get_list_of_favorites_books_success(self,):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби 2'

        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)

        # получаем список избранных книг
        favorites_list = collector.get_list_of_favorites_books()

        # проверяем, что книга добавилась в избранное
        assert name in favorites_list
