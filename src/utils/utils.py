import os 
import sys 
import numpy as np 
import pandas as pd
import dill

from src.utils.exception import CustomException

def save_object(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException("Error occurred while saving object", e, sys.exc_info())