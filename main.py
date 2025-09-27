import loguru
import sys

if __name__ == "__main__":
    logger = loguru.logger
    logger.remove()
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <lvl>{level: <8}</lvl> | {message}",
    )
