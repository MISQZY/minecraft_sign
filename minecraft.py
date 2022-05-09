from PIL import Image, ImageDraw, ImageFont
from settings import text_for_sign, color, first, second, third, four
def start():
    start_input = input("Для начала работы напишите start\n")
    if start_input == "start":
        main()
    else:
        start()

def main():
    x = 885
    input_text = str.strip(text_for_sign)
    char_count = len(input_text)
    if (first is not None and second is None and third is None and four is None) or (char_count > 0 and char_count <= 15):
        strings = 1
    else:
        if(second is not None and third is None and four is None) or (char_count > 15 and char_count <= 30):
            strings = 2
        else:
            if(third is not None and four is None) or (char_count > 30 and char_count <= 45):
                strings = 3
            else:
                if (four is not None) or (char_count > 45 and char_count <= 60):
                    strings = 4
                else:
                    if char_count > 60:
                        strings = 5

    if first is None:
        first_text = input_text[:15]
    else:
        first_text = first[:15]
    first_text = str.strip(first_text)
    char_count = len(first_text)
    first_char = char_count * 42 
    first_locate = (x - first_char, 80)

    if second is None:
        second_text = input_text[15:30]
    else:
        second_text = second[:15]
    second_text = str.strip(second_text)
    char_count = len(second_text)
    second_char = char_count * 42
    second_locate = (x - second_char, 280)

    if third is None:
        third_text = input_text[30:45]
    else:
        third_text = third[:15]
    third_text = str.strip(third_text)
    char_count = len(third_text)
    third_char = char_count * 42
    third_locate = (x - third_char, 480)

    if four is None:
        four_text = input_text[45:60]
    else:
        four_text = four[:15]
    four_text = str.strip(four_text)
    char_count = len(four_text)
    four_char = char_count * 42
    four_locate = (x - four_char, 680)

    img_create(strings, first_locate, first_text,  second_locate, second_text, third_locate, third_text, four_locate, four_text)

def img_create(strings, first_locate, first_text,  second_locate, second_text, third_locate, third_text, four_locate, four_text):
    image = Image.open("./other/mine.jpg")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('./other/minecraft.ttf', size = 115)
    if strings == 1:
        draw.text(first_locate, text = first_text, font=font, fill= color)
    elif strings == 2:
        draw.text(first_locate, text = first_text, font=font, fill= color)
        draw.text(second_locate, text = second_text, font=font, fill= color)
    elif strings == 3:
        draw.text(first_locate, text = first_text, font=font, fill= color)
        draw.text(second_locate, text = second_text, font=font, fill= color) 
        draw.text(third_locate, text = third_text, font=font, fill= color)
    elif strings == 4:
        draw.text(first_locate, text = first_text, font=font, fill= color)
        draw.text(second_locate, text = second_text, font=font, fill= color) 
        draw.text(third_locate, text = third_text, font=font, fill= color)
        draw.text(four_locate, text = four_text, font=font, fill= color)      
    else:
        draw.text(first_locate, text = first_text, font=font, fill= color)
        draw.text(second_locate, text = second_text, font=font, fill= color) 
        draw.text(third_locate, text = third_text, font=font, fill= color)
        draw.text(four_locate, text = four_text, font=font, fill= color)
        print("Обрезал лишнее")
    image.save("mine_done.jpg")

if __name__ == "__main__":
   start()
