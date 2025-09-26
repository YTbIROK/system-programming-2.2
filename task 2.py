import shutil
import os
import zipfile

print("Задание 9: Написать программу, которая создает резервную копию директории, упаковывая ее в zip-архив с сохранением структуры.")


folder = input("Введите путь к папке для архивации: ") or "C:/Student/131-23"
# C:/Student/131-23
zip_name = input("Введите путь для сохранения архива: ") or "backup.zip"
# C:/Student/4321-23
with zipfile.ZipFile(zip_name, 'w') as z:
    for f in os.listdir(folder):
        z.write(os.path.join(folder, f))
print("Создана резервная копия")
