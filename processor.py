import json
import pyautogui
import typing

type TabletConfig = typing.Dict[{'max_width': int, 'max_height': int}]
type Position = typing.NamedTuple('position', [('x', int), ('y', int)])


def process_result():
    with open('tablet-config.json', 'r') as f:
        tablet_config = json.load(f)
    with open('storage.json', 'r') as f:
        data = json.load(f)
    raw_dimension = get_dimension(data)
    convert_result_to_play_area(raw_dimension, tablet_config)


def get_corners(data: list[Position]) -> typing.Tuple[Position, Position, Position, Position]:
    min_x = min(data, key=lambda x: x[0])[0]
    max_x = max(data, key=lambda x: x[0])[0]
    min_y = min(data, key=lambda x: x[1])[1]
    max_y = max(data, key=lambda x: x[1])[1]

    top_left = (min_x, max_y)
    top_right = (max_x, max_y)
    bottom_left = (min_x, min_y)
    bottom_right = (max_x, min_y)

    return top_left, top_right, bottom_left, bottom_right


def get_dimension( data: list[Position] ) -> typing.Tuple[int, int]:
    corners = get_corners(data)
    top_left, top_right, bottom_left, bottom_right = corners
    width = top_right[0] - top_left[0]
    height = top_left[1] - bottom_left[1]
    return width, height


def convert_result_to_play_area(dimension: typing.Tuple[int, int], tablet_config: TabletConfig):
    monitor_size = pyautogui.size()
    tablet_height = tablet_config['max_height']
    tablet_width = tablet_config['max_width']
    area_height = tablet_height * (dimension[1] / monitor_size.height)
    #monitor is 16:9, osu play area is 4:3 so we multiply by 1.33
    area_width = tablet_width * (dimension[0] / monitor_size.width) * 1.33

    print(f'Play area dimension: {area_width} x {area_height}')
