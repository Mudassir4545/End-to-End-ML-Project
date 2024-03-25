from ml_project.config.configuration import configurationManager
from ml_project.components.data_valiation import DataValidation

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_validation = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation)
        data_validation.validate_all_columns()

    
if __name__ == '__main__':
    try:
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()
    except Exception as e:
        raise e 