import logging

log = logging.getLogger('module1')
log.setLevel(logging.DEBUG)
log1 = logging.getLogger('module2')
log1.setLevel(logging.error)


# logging.basicConfig(
#                     level=logging.DEBUG,
#                     format='%(asctime)s-%(levelname)s-%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )

# log.debug("This is a debug message")
# log1.error("This is a error message")

