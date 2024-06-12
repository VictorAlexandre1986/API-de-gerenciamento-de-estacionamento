import logging


# Configuração do formato do log
log_format = ('%(asctime)s - %(name)s - %(levelname)s - '
              '%(filename)s:%(lineno)d - %(message)s')

# Configuração do logging
logging.basicConfig(
    filename='Log.log',
    level=logging.DEBUG,
    format=log_format,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def set_logger_level(level,msg):
    print(logging.level(msg))

