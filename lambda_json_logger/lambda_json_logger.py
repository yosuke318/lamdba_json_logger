from logging import getLogger, StreamHandler, DEBUG, CRITICAL, ERROR, WARNING, INFO
import logging ,json

LOG_LEVELS = {
    "CRITICAL" : CRITICAL,
    "ERROR"    : ERROR,
    "WARNING"  : WARNING,
    "INFO"     : INFO,
    "DEBUG"    : DEBUG,
}


def getLambdaJsonLoggerInstance(level=DEBUG, context=None, stage=None):
    # Getting logger instance
    logger = getLogger("lambda_json_logger")
    logger.setLevel(level)

    if not logger.handlers:
        stream_handler = StreamHandler()

        class LambdaJsonFormatter(logging.Formatter):
            def format(self, record):
                record = {
                    "time": self.formatTime(record),
                    "level": record.levelname,
                    "message": record.getMessage(),
                    "function_name": record.funcName,
                    "module": record.module,
                    "aws_request_id": context.aws_request_id if context else None,
                    "stage": stage,
                }
                return json.dumps(record)

        stream_handler.setFormatter(LambdaJsonFormatter())
        logger.addHandler(stream_handler)

    return logger