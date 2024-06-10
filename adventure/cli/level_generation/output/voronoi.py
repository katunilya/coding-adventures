import time
from pathlib import Path
from typing import Iterable

import rich
from PIL import Image as im
from PIL import ImageDraw as imd
from rich.live import Live
from tibia import curried

from adventure.cli.output.consts import Colors
from adventure.level_generation.generators import voronoi
from adventure.level_generation.utils import iter_positions, scale_size2


def voronoi_level2_to_rich_renderable(level: voronoi.VoronoiLevel2) -> str:
    _rows, _cols = level.size
    _result = [["  " for _ in range(_cols)] for _ in range(_rows)]

    for _position in iter_positions(level.size):
        _tile = level.get_at(_position)
        _color = (
            Colors.BLACK.as_color()
            if _tile == voronoi.DEFAULT_TILE
            else Colors.get_by_number(_tile + 16)
        )
        _row, _col = _position
        _result[_row][_col] = f"[on color({_color.as_number()})]  [/]"

    return "\n".join(["".join(_row) for _row in _result])


def voronoi_level2_to_pil_image(level: voronoi.VoronoiLevel2, scale: int) -> im.Image:
    _scaled_size = scale_size2(level.size, scale)
    _image = im.new("RGB", size=_scaled_size)
    _draw = imd.Draw(_image)

    for _position in iter_positions(level.size):
        _r, _c = _position
        _tile = level.get_at(_position)
        _color = (
            Colors.BLACK.as_color()
            if _tile == voronoi.DEFAULT_TILE
            else Colors.get_by_number(_tile + 16)
        )

        _draw.rectangle(
            [scale_size2((_c, _r), scale), scale_size2((_c + 1, _r + 1), scale)],
            fill=_color.as_triplet(),
        )

    return _image


def rich_show(level: voronoi.VoronoiLevel2) -> voronoi.VoronoiLevel2:
    rich.print(voronoi_level2_to_rich_renderable(level))

    return level


@curried
def rich_show_live(
    levels: Iterable[voronoi.VoronoiLevel2],
    frame_time: float,
) -> Iterable[voronoi.VoronoiLevel2]:
    with Live("") as _live:
        for _level in levels:
            _live.update(voronoi_level2_to_rich_renderable(_level))
            time.sleep(frame_time)
            yield _level


@curried
def maybe_image_save(
    level: voronoi.VoronoiLevel2,
    save_path: Path | None,
    scale: int = 10,
) -> voronoi.VoronoiLevel2:
    if save_path is None:
        return level

    voronoi_level2_to_pil_image(level, scale).save(save_path)
    return level


@curried
def maybe_image_save_live(
    levels: Iterable[voronoi.VoronoiLevel2],
    save_path: Path | None,
    duration: float,
    scale: int = 10,
) -> Iterable[voronoi.VoronoiLevel2]:
    if save_path is None:
        yield from levels
        return

    _images = list[im.Image]()

    for _level in levels:
        _images.append(voronoi_level2_to_pil_image(_level, scale))
        yield _level

    _images[0].save(
        save_path,
        save_all=True,
        append_images=_images[1:],
        optimize=False,
        duration=duration,
        loop=0,
    )
