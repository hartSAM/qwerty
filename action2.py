import unittest
from main import is_even, divide

class TestFunctions(unittest.TestCase):
    def test_is_even(self):
        """Тест для функции is_even"""
        self.assertTrue(is_even(4))  # Четное число
        self.assertFalse(is_even(5))  # Нечетное число

    def test_divide(self):
        """Тест для функции divide"""
        self.assertEqual(divide(10, 2), 5)  # Обычное деление
        with self.assertRaises(ValueError):  # Проверка деления на ноль
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
