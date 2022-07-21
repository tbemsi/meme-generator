from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        out_path = f"{self.output_dir}/{random.randint(0, 1000000)}.png"
        img = Image.open(img_path)

        img_width, img_height = img.size
        height = int(img_height * width / img_width)
        img = img.resize((width, height))

        font_size = int(img.height / 20)

        text_position = random.choice(range(30, height - 50))
        draw = ImageDraw.Draw(img)

        try:
            draw.text((30, text_position), text, fill=(0, 0, 0))
        except UnicodeEncodeError:
            draw.text((30, text_position), text.encode('utf-8'), fill=(0, 0, 0))

        draw.text((int(33), text_position + font_size), " - " + author)

        img.save(out_path)

        return out_path
