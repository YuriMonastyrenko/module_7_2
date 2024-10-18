def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем текущую позицию в байтах перед записью
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i, byte_position)] = string  # Сохраняем в словарь

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)