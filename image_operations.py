from PIL import Image, ImageDraw, ImageFont

def create_text_to_image(text_parts, width=240, height=280, background_color=(0, 0, 0), font_paths=None, font_sizes=None, text_colors=None, output_file="speed_data.png", drive_letter="D"):
    output_file = f"{drive_letter}:\\{output_file}"
    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)

    y = 65  # Starting y position

    if not font_paths:
        font_paths = ["MontserratBlack-3zOvZ.ttf"] * len(text_parts)
    if not font_sizes:
        font_sizes = [20] * len(text_parts)
    if not text_colors:
        text_colors = [(255, 255, 255)] * len(text_parts)

    for i, text in enumerate(text_parts):
        font = ImageFont.truetype(font_paths[i], font_sizes[i])
        text_bbox = draw.textbbox((0, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2
        draw.text((text_x, y), text, font=font, fill=text_colors[i])
        y += text_height + 10  # Increment y position for the next line of text, plus an extra line space

    image.save(output_file)

def generate_image(download_speed, upload_speed, drive_letter):
    text_parts = [
        "Download speed:",
        f"{download_speed:.2f} Mb/s",
        "Upload speed:",
        f"{upload_speed:.2f} Mb/s"
    ]

    font_paths = ["MontserratBlack-3zOvZ.ttf"] * 4
    font_sizes = [20, 30, 20, 30]  
    text_colors = [(255, 255, 255), (0, 255, 0), (255, 255, 255), (0, 255, 0)] 

    create_text_to_image(
        text_parts=text_parts,
        font_paths=font_paths,
        font_sizes=font_sizes,
        text_colors=text_colors,
        drive_letter=drive_letter
    )