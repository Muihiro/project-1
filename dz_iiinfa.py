from PIL import Image, ImageDraw

def reduce_nearest_neighbor(image, scale):

    old_width, old_height = image.size
    new_width = int(old_width * scale)
    new_height = int(old_height * scale)

    # Создаём новое изображение меньшего размера
    reduced = Image.new(image.mode, (new_width, new_height))
    draw_reduced = ImageDraw.Draw(reduced)
    pix = image.load()

    for x in range(new_width):
        for y in range(new_height):
            # Находим соответствующий пиксель в исходном (увеличенном) изображении
            src_x = int(x / scale)
            src_y = int(y / scale)

            # Ограничиваем координаты границами изображения
            src_x = min(src_x, old_width - 1)
            src_y = min(src_y, old_height - 1)

            # Копируем пиксель
            draw_reduced.point((x, y), pix[src_x, src_y])

    return reduced


def resize_area(image, scale):

    old_width, old_height = image.size
    new_width = int(old_width * scale)
    new_height = int(old_height * scale)

    resized = Image.new(image.mode, (new_width, new_height))
    draw_resized = ImageDraw.Draw(resized)
    pix = image.load()

    for x in range(new_width):
        for y in range(new_height):
            # Границы области в исходном изображении
            src_x1 = int(x / scale)
            src_y1 = int(y / scale)
            src_x2 = min(int((x + 1) / scale), old_width)
            src_y2 = min(int((y + 1) / scale), old_height)

            # Усредняем все пиксели в области
            r_sum, g_sum, b_sum = 0, 0, 0
            count = 0

            for sx in range(src_x1, src_x2):
                for sy in range(src_y1, src_y2):
                    px = pix[sx, sy]
                    r_sum += px[0]
                    g_sum += px[1]
                    b_sum += px[2]
                    count += 1

            if count > 0:
                r = r_sum // count
                g = g_sum // count
                b = b_sum // count
            else:
                r, g, b = 0, 0, 0

            draw_resized.point((x, y), (r, g, b))

    return resized

def main():
    print("1 метод ближайшего соседа")
    print("2 усреднение")

    method = int(input('выберите метод (1 или 2): '))
    scale = float(input('введите коэффициент уменьшения '))

    image = Image.open("ans.jpg")

    if image.mode != 'RGB':
        image = image.convert('RGB')

    print(f"исходный размер: {image.size[0]}x{image.size[1]}")


    if method == 1:
        print("используем: метод ближайшего соседа")
        image = reduce_nearest_neighbor(image, scale)
    elif method == 2:
        print("используем: усреднение")
        image = resize_area(image, scale)

    print(f"новый размер: {image.size[0]}x{image.size[1]}")

    image.save("ans_reduced.jpg", "JPEG")
    print("результат сохранён в ans_reduced.jpg")


if __name__ == "__main__":
    main()
