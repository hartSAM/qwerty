def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0

def divide(a, b):
    """Делит два числа, выбрасывает ошибку при делении на ноль."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
