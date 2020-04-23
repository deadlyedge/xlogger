import xlogger
logger = xlogger.xlogger.get_my_logger(__name__)


def main():
    logger.info('这是一条中文消息')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error('Faild to get result', exc_info=True)
    logger.info('Finish')
    logger.debug('Hello %s, %s!' % ('World', 'Congratulations'))
    logger.critical('Hello %s, %s!' % ('World', 'Congratulations'))


if __name__ == '__main__':
    main()
