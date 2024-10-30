import unittest

from main import CurrencyFetcher


class TestCurrencyFetcher(unittest.TestCase):
    """
    Тесты для класса CurrencyFetcher.
    """

    def setUp(self):
        """
        Устанавливает начальные условия для тестов.
        """
        self.fetcher = CurrencyFetcher()

    def test_invalid_id(self):
        """
        Тестирует случай с недействительным идентификатором валюты.
        """
        self.fetcher.set_currencies_ids(['R9999'])
        self.fetcher.fetch_currencies()
        self.assertEqual(self.fetcher.get_result(), [{'R9999': None}])

    def test_valid_ids(self):
        """
        Тестирует случай с действительными идентификаторами валют.
        """
        self.fetcher.set_currencies_ids(['R01035', 'R01335', 'R01700J', 'R01235', 'R01239'])
        self.fetcher.fetch_currencies()
        result = self.fetcher.get_result()
        self.assertTrue(any(valute['name'] == 'Фунт стерлингов Соединенного королевства' for valute in result))
        self.assertTrue(any(valute['name'] == 'Доллар США' for valute in result))
        self.assertTrue(any(valute['name'] == 'Евро' for valute in result))
        self.assertTrue(all(0 <= valute['value'] <= 999 for valute in result))


if __name__ == '__main__':
    unittest.main()