import os
from pathlib import Path

from PIL import Image as im
from PIL import ImageDraw as imd


def make_title_collage(
    image_paths: list[Path], save_path: Path, per_row: int
) -> im.Image:
    _total_images = len(image_paths)
    _images = [im.open(_image_path) for _image_path in image_paths]
    print(_total_images)
    _max_w = max(_image.size[0] for _image in _images)
    _max_h = max(_image.size[1] for _image in _images)

    print(_max_w, _max_h)

    _row_count = (
        _total_images // per_row + 1
        if _total_images % per_row != 0
        else _total_images // per_row
    )
    _shift = 20

    _width = per_row * _max_w + _shift * (per_row + 1)
    _height = _row_count * _max_h + _shift * (_row_count + 1)
    print(_width, _height)
    _result = im.new(mode="RGB", size=(_width, _height))
    _result.save(save_path)

    _image_draw = imd.Draw(_result)
    _current_col = 0

    _data = list(zip(_images, image_paths))
    print(len(_data), _data)
    for i, _w in enumerate(range(_shift, _width, _max_w + _shift)):
        for j, _h in enumerate(range(_shift, _height, _max_h + _shift)):
            idx = i * per_row + j
            if not (idx < len(_data)):
                continue

            _image, _image_path = _data[idx]

            _caption = _image_path.stem

            _offset = (_h, _w)
            print(f"pasting {idx}. {_image_path.stem} at {_offset}")

            _result.paste(_image, _offset)
            _image_draw.text((_offset[0], _offset[1] - _shift), _caption)
            _current_col += 1

    _result.save(save_path)


if __name__ == "__main__":
    _save_path = Path.cwd() / "imgs/voronoi.png"
    if _save_path.exists():
        os.remove(_save_path)

    make_title_collage(
        sorted(list((Path.cwd() / "imgs").glob("voronoi*.png"))),
        _save_path,
        4,
    )
