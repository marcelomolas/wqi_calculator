from owslib.swe.common import Boolean
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt, QRegExp, QLibraryInfo, QLocale, QTimer
from qgis._core import QgsMapLayer, QgsRasterLayer, QgsColorRampShader, QgsRasterShader, \
    QgsSingleBandPseudoColorRenderer
from qgis._gui import QgsFileWidget
from qgis.core import QgsProject, QgsMessageLog, QgsMapLayerType
from qgis.PyQt.QtGui import QIcon, QRegExpValidator, QColor
from qgis.PyQt.QtWidgets import QAction, QTableWidgetItem, QAbstractItemView, QHeaderView, QStyledItemDelegate, \
    QLineEdit, QWizard, QComboBox, QTableWidget, QWizardPage
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
import processing
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .wqi_calculator_wizard import WQICalculatorWizard
import os.path


class WQIDataManager:

    def abrir_plugin_interpolacion(self):
        processing.execAlgorithmDialog('gdal:gridinversedistance')

    def get_project_layers(self):
        """Devuelve todas las capas del proyecto QGIS."""
        return QgsProject.instance().layerTreeRoot().findLayers()

    def create_wqi_raster(self, formula, entries, output_path, reference_layer):
        calculadora = QgsRasterCalculator(
            formulaString=formula,
            outputFile=output_path,
            outputFormat="GTiff",
            rasterEntries=entries,
            outputExtent=reference_layer.extent(),
            nOutputColumns=reference_layer.width(),
            nOutputRows=reference_layer.height()
        )
        calculadora.processCalculation()
        return output_path

    def create_wqi_layer_with_symbology(self, raster_file_path, classes, layer_name="WQI"):
        raster_layer = QgsRasterLayer(raster_file_path, baseName=layer_name)
        if not raster_layer.isValid():
            return None

        dp = raster_layer.dataProvider()

        fnc = QgsColorRampShader()
        fnc.setColorRampType(QgsColorRampShader.Discrete)

        items = []
        for c in classes:
            limite = c["limite"]
            r, g, b = c["color"]
            label = c["label"]
            items.append(
                QgsColorRampShader.ColorRampItem(limite, QColor(r, g, b), label)
            )

        fnc.setColorRampItemList(items)

        shader = QgsRasterShader()
        shader.setRasterShaderFunction(fnc)

        renderer = QgsSingleBandPseudoColorRenderer(dp, 1, shader)
        raster_layer.setRenderer(renderer)

        QgsProject.instance().addMapLayer(raster_layer)
        return raster_layer