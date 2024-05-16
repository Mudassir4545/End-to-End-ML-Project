from ml_project.config.configuration import configurationManager
from ml_project.components.model_evaluation import ModelEvaluation
from ml_project.logging import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} stareted <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e