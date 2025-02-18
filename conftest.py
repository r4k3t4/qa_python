import pytest

from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    # добавляем одну книгу
    collector.add_new_book('Гордость и предубеждение и зомби')
    # устанавливаем книге жанр
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    # добавляем вторую книгу
    collector.add_new_book('Шрек')
    # устанавливаем второй книге жанр
    collector.set_book_genre('Шрек', 'Мультфильмы')
    # добавляем третью книгу
    collector.add_new_book('Маска')
    # устанавливаем третьей книге жанр
    collector.set_book_genre('Маска', 'Комедии')
    return collector