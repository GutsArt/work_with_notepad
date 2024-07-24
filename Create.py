import os
from datetime import datetime

# Получаем сегодняшнюю дату
today_date = datetime.today().strftime('%d.%m.%Y')

# Формируем название файла
file_name = f"{today_date}.txt"

# Путь к рабочему столу (в Windows)
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'Desktop\ ')
# desktop_path = r'C:\Users\artem\Desktop\ '

# Полный путь к файлу
file_path = os.path.join(desktop_path, file_name)

# Создаем и открываем файл для записи
with open(file_path, 'a+') as file:
    # Перемещаем указатель в начало файла
    file.seek(0)
    # Читаем содержимое файла
    data = file.read()
    # Если файл пуст
    if not data:
        # Записываем текущее время
        dt = datetime.now()
        file.write(f"Текущее время: {dt}\n")
    else:
        # Добавляем номера итераций к содержимому файла
        file.write(f"\n")
    for i in range(20):
        file.write(f"\n{i + 1}.")

# Открываем файл в блокноте (подразумевается, что блокнот ассоциирован с .txt файлами)
os.system(f"notepad.exe {file_path}")
