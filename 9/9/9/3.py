from PIL import Image, ImageFilter
import os

input_dir = 'D:\фото'
output_dir = 'D:\фото2'
os.makedirs(output_dir, exist_ok=True)
# Фильтр контурирование
filter_type = ImageFilter.CONTOUR
for i in range(1, 6):
    input_file = f"{i}.jpg"
    try:
        img = Image.open(os.path.join(input_dir, input_file))
        filtered_img = img.filter(filter_type)
        output_file = f'{i}_новый.jpg'
        filtered_img.save(os.path.join(output_dir, output_file))
        print(f'Файл {input_file} успешно обработан.')
    except FileNotFoundError:
        print(f'Файл {input_file} не найден!')
    except Exception as e:
        print(f'Ошибка обработки файла {input_file}: {e}')
