if __name__ == "__main__":
    import lambda_json_logger
    print(dir(lambda_json_logger))
    lg = lambda_json_logger.getLambdaJsonLoggerInstance(aws_request_id="1234", stage="dev")
    lg.info("This is an info message")