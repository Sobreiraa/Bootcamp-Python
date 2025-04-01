from loguru import logger

logger.debug("Um aviso para o desenvolvedor.")
logger.info('Informação importante.')
logger.warning('Um aviso que algo vai aprar de funcionar no futuro.')
logger.error('Aconteceu uma falha.')
logger.critical('Aconteceu uma falha que pode abortar a aplicação.')