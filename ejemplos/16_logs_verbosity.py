# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install argparse
# 2. Ejecuta el script: python 16_logs_verbosity.py
# 3. Cambia el nivel de verbosity con --log-level (DEBUG, INFO, WARNING, ERROR)
# python logs_verbosity.py --log-level DEBUG

import argparse
import logging

parser = argparse.ArgumentParser(description="Nivel de verbosity")
parser.add_argument('--log-level', type=str, default='INFO',
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])

args = parser.parse_args()
logging.basicConfig(level=args.log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('logger')

logger.info('Ejemplo info')
logger.debug('Ejemplo debug')
logger.warning('Ejemplo warning')