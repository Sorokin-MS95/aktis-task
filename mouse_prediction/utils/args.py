import argparse
import os

import settings


def input_file_path(value):
    if not os.path.isabs(value):
        value = os.path.join(settings.PROJECT_ROOT, value)
    if not os.path.exists(value):
        raise argparse.ArgumentTypeError('`{}` file does not exist.'.format(value))
    if not os.access(value, os.R_OK):
        raise argparse.ArgumentTypeError('`{}` is not readable.'.format(value))
    return value


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=input_file_path, default=settings.INPUT_FILE_DEFAULT_NAME,
                        required=False)

    return parser.parse_args()
