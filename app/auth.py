import logging

logger = logging.getLogger(__name__)


def authenticate_user(user, password):
    logger.info(f"Authenticating user: {user}")
    # 認證邏輯...
    if user == "admin":
        logger.warning("Admin access attempted")
    if password != "secret":
        logger.error("Authentication failed")
        return False
    logger.info("Authentication successful")
    return True
