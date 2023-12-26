#     billbot - a very random discord bot
#     Copyright (C) 2023  williamist
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import io

from PIL import Image

import billbot.util as util

TEMPLATE = Image.open("resources/1984base.png").convert("RGBA")
MASK = Image.open("resources/1984mask.png").convert("RGBA")


def process_frame(frame: Image) -> Image:
    frame = frame.convert("LA").convert("RGBA")

    # crop
    if frame.width > frame.height:
        frame = frame.crop((frame.width // 2 - frame.height // 2, 0, frame.width // 2 + frame.height // 2, frame.height))
    elif frame.width < frame.height:
        frame = frame.crop((0, frame.height // 2 - frame.width // 2, frame.width, frame.height // 2 + frame.width // 2))

    # squishy squash
    frame.thumbnail((165, 165))

    # translucency
    frame.putalpha(125)

    # mask
    frame.paste(0, mask=MASK)

    return frame

def do(image_bytes: bytes) -> io.BytesIO:
    in_image = Image.open(io.BytesIO(image_bytes))

    if not getattr(in_image, "is_animated", False):
        out_image = TEMPLATE.copy()
        out_image.alpha_composite(process_frame(in_image), (90, 18))

        return util.imageToBytesIO(out_image)
    else:
        # fancy-schmancy gif stuff
        out_frames = []
        for i in range(in_image.n_frames):
            in_image.seek(i)
            new_frame = TEMPLATE.copy()
            new_frame.alpha_composite(process_frame(in_image), (90, 18))

            out_frames.append(new_frame)

        return util.imageToBytesIO(out_frames[0], "GIF", save_all=True, append_images=out_frames[1:], duration=(in_image.info['duration'] or 100), loop=(in_image.info['loop'] or 0))


