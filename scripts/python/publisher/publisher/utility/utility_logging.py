

import datetime


def get_formatted_timestamp() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')

