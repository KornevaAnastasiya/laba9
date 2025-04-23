from PIL import Image
import os


def main():
    original_file_name = 'D:\букет.png'
    try:
        directory = os.path.dirname(original_file_name)

        image = Image.open(original_file_name)

        reduced_size = tuple(size // 3 for size in image.size)
        resized_image = image.resize(reduced_size)
        resized_image.save(os.path.join(directory, 'измененный_размер.png'))

        horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal_mirror.save(os.path.join(directory, 'горизонталь_зеркало.png'))

        vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
        vertical_mirror.save(os.path.join(directory, 'вертикаль_зеркало.png'))

        print("Все изображения сохранены успешно!")

    except FileNotFoundError:
        print("Оригинальный файл не найден")
    except Exception as e:
        print(f"Возникла ошибка: {e}")


if __name__ == "__main__":
    main()
#os определяет директорию исходного файла
#directory=os.path.dirname.. извлекает каталог в которм лежит исходник