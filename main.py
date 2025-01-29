from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_1_data_ingestion_pipeline import (
    DataIngestionTrainingPipeline,
)
from src.TextSummarizer.pipeline.stage_2_data_transformation_pipeline import (
    DataTransformationTraningPipeline,
)


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataTransformationTraningPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e
