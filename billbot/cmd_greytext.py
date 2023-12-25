from PIL import Image, ImageFont, ImageDraw
import textwrap
import io

FONT = ImageFont.truetype("unifont.otf", size=16)


def helper_draw_lines(draw: ImageDraw.ImageDraw, lines: list[str], color: tuple[int, int, int], xy: tuple[int, int]):
    pixel_height = len(lines) * 16
    y = xy[1] - pixel_height // 2
    for line in lines:
        x = xy[0] - FONT.getlength(line) // 2
        draw.text((x, y), line, align="center", fill=color)
        y += 16


def do(text: str) -> io.BytesIO:
    # wrap text
    wrapped_lines = textwrap.wrap(text, width=35)

    # get size of text in pixels
    text_height = len(wrapped_lines) * 16

    # make new image
    image = Image.new(mode="RGB", size=(320, max(240, text_height + 80)), color=(127, 127, 127))

    # draw text onto image
    text_pos = (image.width // 2, image.height // 2)

    draw = ImageDraw.Draw(image)
    draw.font = FONT
    draw.fontmode = "1"
    helper_draw_lines(draw, wrapped_lines, (63, 63, 63), (text_pos[0] + 2, text_pos[1] + 2))
    helper_draw_lines(draw, wrapped_lines, (255, 255, 255), text_pos)

    b = io.BytesIO()
    image.save(b, "GIF")
    b.seek(0)

    return b
