# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WQIPlugin
                                 A QGIS plugin
 Complemento para calcular de forma automática el WQI
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-07-04
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Carin Martinez; Marcelo Molas
        email                : marcemolas@fpuna.edu.py
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis._core import QgsMapLayer
from qgis.core import QgsProject, QgsMessageLog, QgsMapLayerType
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QTableWidgetItem, QAbstractItemView
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .wqi_plugin_wizard import WQIPluginWizard
import os.path


class WQIPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'WQIPlugin_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&WQIPlugin')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('WQIPlugin', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/wqi_plugin/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'WQI Plugin'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&WQIPlugin'),
                action)
            self.iface.removeToolBarIcon(action)

    def capa_ya_seleccionada(self, capa_seleccionada):
        if(self.dlg.SelectedCapas.count() != 0):
            for fila in range(0,self.dlg.SelectedCapas.count()):
                capa = self.dlg.SelectedCapas.item(fila).text()
                if(capa == capa_seleccionada):
                    return True
        return False

    def seleccionar_capas(self):
        """Transfiere las capas de la tabla de AllCapas a la tabla de Seleccionados"""
        capas_seleccionadas = self.dlg.AllCapas.selectedItems()
        indice = self.dlg.SelectedCapas.count()

        for capa in capas_seleccionadas:
            if not self.capa_ya_seleccionada(capa.text()):
                self.dlg.SelectedCapas.addItem(capa.text())
                self.dlg.DatosAdicionales.setRowCount(indice+1)
                self.dlg.DatosAdicionales.setItem(indice,0,QTableWidgetItem(capa.text()))
                indice+=1

    def remover_capas(self):
        """Remueve las capas de la tabla de SelectedTablas """
        capas_seleccionadas = self.dlg.SelectedCapas.selectedItems()

        for capa in capas_seleccionadas:
            #para la lista de seleccionados
            num_fila = self.dlg.SelectedCapas.row(capa)
            self.dlg.SelectedCapas.takeItem(num_fila)
            self.dlg.DatosAdicionales.removeRow(num_fila)

    def calcular_wqi(self):

        layers_seleccionados = []
        peso_total = 0
        for fila in range(0,self.dlg.DatosAdicionales.rowCount()):
            peso_total += int(self.dlg.DatosAdicionales.item(fila,3).text())
            for layer in self.layers:
                if layer.name() == self.dlg.DatosAdicionales.item(fila,0).text():
                    layers_seleccionados.append(layer.layer())

        entries = []
        formula = ""

        for fila in range(0,len(layers_seleccionados)):
            entry = QgsRasterCalculatorEntry()
            entry.bandNumber = 1
            entry.raster = layers_seleccionados[fila]
            entry.ref = layers_seleccionados[fila].name() + "@1"
            entries.append(entry)


            concentracion = entry.ref
            estandar = self.dlg.DatosAdicionales.item(fila, 1).text()
            valor_ideal = self.dlg.DatosAdicionales.item(fila,2).text()
            peso_relativo = int(self.dlg.DatosAdicionales.item(fila, 3).text())/peso_total
            quality_rating = f"(({concentracion} - {valor_ideal}) / ({estandar} - {valor_ideal})) * {peso_relativo} * 100"


            if fila == 0:
                formula += quality_rating
            else:
                formula += "+ " + quality_rating
        calculadora = QgsRasterCalculator(formulaString=formula,outputFile="C:\\Users\\User\\Documents\\prueba_2.tif",outputFormat="GTiff",rasterEntries=entries, outputExtent=layers_seleccionados[0].extent(), nOutputColumns=layers_seleccionados[0].width(), nOutputRows=layers_seleccionados[0].height())
        calculadora.processCalculation()
        QgsMessageLog.logMessage(formula, "tag", 0)

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started

        if self.first_start == True:
            self.first_start = False
            self.dlg = WQIPluginWizard()
            self.dlg.AllCapas.clear()
            self.dlg.AddCapas.clicked.connect(self.seleccionar_capas)
            self.dlg.RemoveCapas.clicked.connect(self.remover_capas)
            self.dlg.AllCapas.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.dlg.SelectedCapas.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.dlg.CalcularWQI.clicked.connect(self.calcular_wqi)

            self.layers = QgsProject.instance().layerTreeRoot().children()
            self.dlg.AllCapas.addItems([layer.name() for layer in self.layers if layer.layer().type() == QgsMapLayer.RasterLayer])

        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass