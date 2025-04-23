from PIL import Image

base_image_path = 'D:\фото3\logo.jpg'
watermark_path = 'D:\фото3\water.png'
output_path = 'result_watermark.jpg'
base_image = Image.open(base_image_path).convert('RGBA')
watermark = Image.open(watermark_path).convert('RGBA')

base_width, base_height = base_image.size
scale_factor = 0.2
new_size = (int(base_width * scale_factor), int(base_height * scale_factor))
watermark_resized = watermark.resize(new_size, Image.Resampling.LANCZOS)# Масштабируем водяной знак

position = (base_width - new_size[0], base_height - new_size[1])# Расположение водяного знака

final_image = Image.new('RGBA', base_image.size)
final_image.paste(base_image, (0, 0))
final_image.paste(watermark_resized, position, mask=watermark_resized)# Добавляем водяной знак поверх изображения

final_image_rgb = final_image.convert('RGB')
final_image_rgb.save(output_path)

print(f"Водяной знак добавлен и сохранен в '{output_path}'")
