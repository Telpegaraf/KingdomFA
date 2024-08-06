import logging
from core.config import settings


def configure_logging():
    log_level = settings.log_level.upper()
    log_level = getattr(logging, log_level)
    logging.basicConfig(
        level=log_level,
        filename='kingdom.log',
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
