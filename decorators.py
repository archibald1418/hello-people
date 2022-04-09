import logging

logging.basicConfig(filename=LOG_FILE,
                    level='INFO',
                    format='%(asctime)s:%(message)s',
                    datefmt='%y-%d-%m %H:%M:%S',
                    filemode='w')

# Creates a new decorator to print given log message
def decorator_factory(msg=None):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(msg)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return log_decorator 
