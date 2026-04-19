from PIL import Image, ImageDraw
import numpy as np

mode = int(input('mode: '))
image = Image.open("e4def666f7ad5077ab5310cadd42e373.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()


if mode == 1:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))


elif mode == 2:
    channel = input('удалить канал (r/g/b): ').lower()
    for i in range(width):
        for j in range(height):
            r, g, b = pix[i, j][0], pix[i, j][1], pix[i, j][2]
            if channel == 'r':
                r = 0
            elif channel == 'g':
                g = 0
            elif channel == 'b':
                b = 0
            draw.point((i, j), (r, g, b))


elif mode == 3:
    direction = input('переворот (h=горизонтальный, v=вертикальный): ').lower()

    flipped = Image.new(image.mode, image.size)
    draw_flipped = ImageDraw.Draw(flipped)

    for i in range(width):
        for j in range(height):
            if direction == 'h':  # Горизонтальный: меняем X
                new_x = width - 1 - i
                new_y = j
            elif direction == 'v':  # Вертикальный: меняем Y
                new_x = i
                new_y = height - 1 - j
            else:
                new_x, new_y = i, j  # По умолчанию без изменений

            pixel = pix[i, j]
            draw_flipped.point((new_x, new_y), pixel)


    image = flipped
    draw = ImageDraw.Draw(image)

image.save("ans.jpg", "JPEG")
del draw
print("результат сохранён в ans.jpg")