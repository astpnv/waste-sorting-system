import unittest

from src.main import get_container, search_waste, sort_waste


class WasteSortingTests(unittest.TestCase):
    """Тести бізнес-логіки сортування відходів."""

    def test_sort_waste_plastic(self):
        # звичайний сценарій: відомий предмет
        self.assertEqual(sort_waste("bottle"), "paper")

    def test_sort_waste_unknown_item(self):
        # граничний сценарій: невідомий та порожній ввід
        self.assertEqual(sort_waste("unknown"), "other")
        self.assertEqual(sort_waste(""), "other")

    def test_search_waste_finds_items(self):
        self.assertEqual(search_waste("gl"), ["glass"])

    def test_search_waste_no_match(self):
        # граничний сценарій: запит без збігів
        self.assertEqual(search_waste("xyz"), [])

    def test_get_container_known_category(self):
        self.assertEqual(get_container("paper"), "blue")

    def test_get_container_unknown_category(self):
        # граничний сценарій: невідома категорія
        self.assertEqual(get_container("metal"), "gray")


if __name__ == "__main__":
    unittest.main()
