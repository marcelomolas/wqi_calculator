
from qgis.PyQt.QtCore import QLocale

def parse_float_local(texto, locale=None):
    if locale is None:
        locale = QLocale()
    return locale.toDouble(texto)[0]

def format_float_local(valor, decimales=2, locale=None):
    if locale is None:
        locale = QLocale()
    return locale.toString(valor, 'f', decimales)
