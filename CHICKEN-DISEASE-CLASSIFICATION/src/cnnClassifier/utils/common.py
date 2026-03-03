import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create a list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """
    Saves data to a json file.
    Args:
        path (Path): Path to the json file.
        data (Any): Data to be saved.
    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file: {path} saved successfully")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a json file.
    Args:
        path (Path): Path to the json file.
    Returns:
        ConfigBox: data as class attributes instead of dict.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    Returns:
        None
    """
    joblib.dump(data, path)
    logger.info(f"binary file: {path} saved successfully")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file: {path} loaded successfully")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB, MB, or GB.
    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in KB, MB, or GB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    size_in_mb = round(size_in_kb / 1024)
    size_in_gb = round(size_in_mb / 1024)

    if size_in_gb > 0:
        return f"{size_in_gb} GB"
    elif size_in_mb > 0:
        return f"{size_in_mb} MB"
    else:
        return f"{size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        imageBytes = f.read()
        return base64.b64encode(imageBytes)