# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WQICalculator
                                 A QGIS plugin
 Complemento para calcular de forma automática el WQI
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-07-04
        copyright            : (C) 2024 by Carin Martinez; Marcelo Molas
        email                : marcemolas@fpuna.edu.py
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WQICalculator class from file WQICalculator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wqi_calculator import WQICalculator
    return WQICalculator(iface)
