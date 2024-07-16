import logging

from . import auth, db

# logger = logging.getLogger(__name__)  # if this is not an entrypoint
logger = logging.getLogger("app")


def main():
    logger.info("Application started")
    auth.authenticate_user(user="max", password="pwd")
    db.connect_to_db()
    db.query_db(query="SELECT best_logger FROM MaxGithub")
    logger.info("Application finished")


if __name__ == "__main__":
    main()
