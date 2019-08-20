import random
import logging

LOG_FILENAME = 'log.txt'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
    filemode="a" #default is (a)append mode
)

logging.debug(f'Message:{random.randint(1,1000)}')
logging.debug(f'Message:{random.randint(1,1000)}')

with open(LOG_FILENAME, 'r') as f:
    body = f.read()

print('LOG-FILE:')
print(body)