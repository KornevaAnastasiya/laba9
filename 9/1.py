from PIL import Image

file_path = 'D:\букет.png'
im= Image.open(r"D:\букет.png")
im.show()
try:
    with Image.open(file_path) as img:

        print(f"Размер изображения: {img.size}")
        print(f"Формат изображения: {img.format}")
        print(f"Цветовая модель: {img.mode}")
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
