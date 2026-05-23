def add(a, b):
    """Возвращает сумму a и b"""
    return a + b

def subtract(a, b):
    """Возвращает разность a и b"""
    return a - b

def multiply(a, b):
    """Возвращает произведение a и b"""
    return a * b

def divide(a, b):
    """Возвращает частное a и b, проверяет деление на ноль"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

if __name__ == "__main__":
    print("Калькулятор")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")  # Конфликт разрешен
