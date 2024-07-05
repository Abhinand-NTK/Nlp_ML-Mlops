#Basic of logging importence and the use case
import logging

# logging.basicConfig(level=logging.DEBUG)

# # log messages
# logging.debug("This is a debuggging message")
# logging.info("This is a info message for the coders")
# logging.warning("This is a info warning for the coders")
# logging.error("This is an error message")
# logging.critical("This is an critical message")

#configuring logging

logging.basicConfig(
                    filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

# log messages
logging.debug("This is a debuggging message")
logging.info("This is a info message for the coders")
logging.warning("This is a info warning for the coders")
logging.error("This is an error message")
logging.critical("This is an critical message")

