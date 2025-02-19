# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

from main import BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # проверяем, что добавилось именно две
        # словарь books_genre имеет длину 2
        assert len(collector.books_genre.keys()) == 3

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_add_genre(self, collector):

        # проверяем что в словаре books_genre
        assert 'Гордость и предубеждение и зомби' in collector.books_genre.keys() and 'Ужасы' in collector.books_genre.values()

    def test_get_book_genre_name_book(self, collector):

        assert 'Гордость и предубеждение и зомби' in collector.books_genre.keys()

    def test_get_books_with_specific_genre_books_with_specific_genre(self, collector):

        assert 'Гордость и предубеждение и зомби' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_all_book(self, collector):

        assert 'Гордость и предубеждение и зомби' and 'Шрек' and 'Маска' in collector.books_genre

    def test_get_books_for_children_books_for_children(self, collector):

        assert 'Шрек' and 'Маска' in collector.get_books_for_children()

    def test_add_book_in_favorites_book_in_favorites(self, collector):

        collector.add_book_in_favorites('Шрек')

        assert 'Шрек' in collector.favorites and collector.books_genre

    def test_delete_book_from_favorites_delete_favorites(self, collector):

        collector.add_book_in_favorites('Шрек')
        collector.add_book_in_favorites('Маска')
        collector.delete_book_from_favorites('Шрек')
        assert 'Шрек' not in collector.favorites

    def test_get_list_of_favorites_books_favorites_books(self, collector):

        collector.add_book_in_favorites('Шрек')
        collector.add_book_in_favorites('Маска')

        assert 'Шрек' and 'Маска' in collector.favorites

    def test_add_new_book_title_book_and_duplicate(self, collector):
        collector = BooksCollector()
        # добавляем одну книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем дубликат
        collector.add_new_book('Гордость и предубеждение и зомби')

        list_book_genre = list(collector.books_genre.keys())

        assert len(collector.books_genre.keys()) == 1 and len(list_book_genre[0]) <= 40
