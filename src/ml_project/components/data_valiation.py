import os
import urllib.request as request
import zipfile
from ml_project.logging import logger
import pandas as pd
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    #making function validate all columns
    def validate_all_columns(self)->bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation staus: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation staus: {validation_status}")
            return validation_status
        except Exception as e:
            raise e