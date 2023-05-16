import json
from typing import Callable
from jinja2 import Template


def read_file(path: str) -> str:
    """
    This function takes a path for the file and read it

    Args:
        path: [str] path of the file

    Raises:
        OSError: exceptions to handling files

    Returns: [str] contents of the file


    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except OSError as error:
        raise error


def render_mapping(path: str,
                   number_of_replicas: int,
                   number_of_shards: int,
                   render: Callable[[str], str] = read_file) -> dict:
    """
    this function for parsing  the file content
    and makes it to be admissible for indexed in ES

    Args:
        path: [str] path of the file
        number_of_replicas: [int] number of replicas
        number_of_shards: [int] number of shards
        render: [Callable] callable for read file

    Return: [dict] content of the mapping
    """
    file_content = render(path)

    template = Template(file_content)
    render_template = template.render(NumberOfReplicas=number_of_replicas, NumberOfShards=number_of_shards)

    # convert the render template to a dictionary format
    try:
        mapping = json.loads(render_template)
        return mapping
    except json.JSONDecodeError as error:
        raise error
