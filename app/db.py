import logging

logger = logging.getLogger(__name__)


def connect_to_db():
    logger.info("Connecting to the database")
    # 數據庫連接邏輯...
    logger.info("Connected to the database")


def query_db(query):
    logger.debug(f"Executing query: {query}")
    # 查詢邏輯...
    logger.info("Query executed successfully")
