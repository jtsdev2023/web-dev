from typing import Tuple
import os
import json
import yaml


def read_yaml_file() -> Tuple[int, str]:
    """DOC STRING"""
    yaml_file = 'web-layout.yaml'
    directory_content_list = os.listdir()

    if yaml_file in directory_content_list:
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            return (0, file_content)
        except FileExistsError as error:
            print(error)
            return (1, error)
    else:
        error_msg = f'File {yaml_file} does not exist.'
        print(error_msg)
        return (1, error_msg)


def generate_yaml_obj(yaml_input_string: str) -> Tuple[int, list]:
    """DOC STRING"""
    try:
        yaml_object = yaml.safe_load(yaml_input_string)
        return (0, yaml_object)
    except Exception as error:
        print(error)
        return (1, error)


def convert_yaml_to_json(yaml_input_object: list) -> Tuple[int, str]:
    """DOC STRING"""
    try:
        json_string = json.dumps(yaml_input_object)
        return (0, json_string)
    except Exception as error:
        print(error)
        return (1, error)


def main():
    """DOC STRING"""
    error, yaml_string = read_yaml_file()
    if error == 0:
        try:
            yaml_object = generate_yaml_obj(yaml_string)
            json_string = convert_yaml_to_json(yaml_object)
            return (0, json_string)
        except Exception as error:
            print(error)
            return (1, error)
    else:
        return (1, error)


if __name__ == '__main__':
    main()
