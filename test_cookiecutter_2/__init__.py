import logging
import test_cookiecutter_2._version


__version__ = test_cookiecutter_2._version.__version__



logger = logging.getLogger(__name__)
logger.info(f'Imported test_cookiecutter_2version: {__version__}')
