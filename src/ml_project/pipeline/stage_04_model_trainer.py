from ml_project.config.configuration import configurationManager
from ml_project.components.model_training import ModelTrainer

STAGE_NAME = "Model Training stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        self.conf = configurationManager()
        self.model_trainer = ModelTrainer(self.conf)
        self.model_trainer.train()
        

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config = model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
