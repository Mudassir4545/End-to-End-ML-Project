from ml_project.config.configuration import configurationManager
from ml_project.components.model_training import ModelTrainer
from ml_project.logging import logger
STAGE_NAME = "Model Training stage"

STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
