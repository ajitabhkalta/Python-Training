import logging

logging.basicConfig(level=logging.INFO)

logger1 = logging.getLogger('Alarm')
logger2 = logging.getLogger('Power')

logger1.warning('Not working')
logger1.info('Restored')
logger2.critical('Not working')