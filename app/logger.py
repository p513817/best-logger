import json
import logging
import logging.config
import os


def setup(log_path="config/logging.json", env_key="LOG_CFG") -> None:
    """
    setup logging

    Args:
        default_path (str, optional): _description_. Defaults to "config/logging.json".
        default_level (_type_, optional): _description_. Defaults to logging.INFO.
        env_key (str, optional): _description_. Defaults to "LOG_CFG".
    """
    env_log_path = os.getenv(env_key, None)
    if env_log_path:
        print(f"Detect 'LOG_CFG' was set, replace {log_path} to {env_log_path}")
        log_path = env_log_path

    if not os.path.exists(log_path):
        raise FileExistsError("The log's configuration not found.")

    with open(log_path, "rt") as f:
        config = json.load(f)

    for handler in config["handlers"].values():
        filename = handler.get("filename", None)
        if not filename:
            continue
        filedir = os.path.dirname(filename)
        os.makedirs(filedir, exist_ok=True)

    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("Setup Logger !")
