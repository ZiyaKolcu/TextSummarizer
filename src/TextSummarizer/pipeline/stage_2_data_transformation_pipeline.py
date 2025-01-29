from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_transfromation import DataTransformation
from src.TextSummarizer.logging import logger


class DataTransformationTraningPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
