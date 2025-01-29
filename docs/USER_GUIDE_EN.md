# User Guide - WQICalculator

## Introduction
**WQICalculator** is a QGIS plugin that automatically calculates the Water Quality Index (WQI) from raster layers containing various physicochemical parameters. 

This guide provides detailed instructions on how to install, configure, and use the plugin.

---

## Installation
1. Open QGIS and go to **Plugins > Manage and Install Plugins**.
2. In the **All** tab, search for "WQICalculator".
3. Select the plugin and click **Install Plugin**.
4. Once installed, the plugin will be available in the toolbar and the **Plugins** menu.

---

## Requirements
- QGIS 3.0.0 or higher.
- A project with raster layers containing water quality physicochemical parameters (pH, sodium, total dissolved solids, among others).

---

## Using the Plugin

### 1. Open WQICalculator
- Once installed, access the plugin from **Plugins > WQI Calculator** or by clicking the icon in the toolbar.

![image](https://github.com/user-attachments/assets/0ee168ad-a0b4-49a3-ae1f-3ddc657756a7)

### 2. Select Input Layers
- Any layer added to the project will appear in the plugin's layer list, but only raster layers can be selected.
- There are no restrictions on layer names.
- Ensure that all layers share the same spatial reference system (CRS) for better results.
- Click on a layer or click and drag the mouse to select multiple layers at once.
- Click the "Add Layers" button to select the layers to be used in the WQI calculation.

![image](https://github.com/user-attachments/assets/f0cf9a8a-e93f-41fa-93ef-fc877c43830c)

![image](https://github.com/user-attachments/assets/0c253747-0cf1-4cdc-a147-9dc32b253379)

### 2.1 Interpolating a Vector Layer (Optional)
- If you only have a vector layer containing multiple physicochemical parameters, you have the option to interpolate it using IDW (Inverse Distance Weighted) with the QGIS algorithm "gdal:gridinversedistance".
- Select the vector layer and click "Interpolate with IDW".
- Check the official QGIS documentation for more information on this algorithm: [Inverse Distance to a Power](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/gdal/rasteranalysis.html#grid-inverse-distance-to-a-power).

![image](https://github.com/user-attachments/assets/61d84d99-50bc-410d-9edc-4220dda0c004)

### 3. Configure Parameters
- In the plugin interface, select the appropriate parameter for each layer using the dropdown list in the "Parameter" column, or manually enter the ideal values, standards, and weights for each selected parameter.

![image](https://github.com/user-attachments/assets/665288c9-dcbf-4446-be32-53bce180470d)

![image](https://github.com/user-attachments/assets/dc798006-3b4f-4ea7-97d8-ddc26cfd3979)

![image](https://github.com/user-attachments/assets/5b2866db-6d1f-430e-b397-d0f9eeff52fb)

### 4. Choose WQI Layer Destination and Calculate the Water Quality Index
- Click the "..." button to choose the destination folder and the name for the output .tif file.
- Click the "Generate WQI" button.
- The plugin will generate a raster layer with Water Quality Index values and automatically add it to the open project under the name "WQI".

![image](https://github.com/user-attachments/assets/d208fa0d-31b5-44e0-a93e-5771e751aa07)

![image](https://github.com/user-attachments/assets/79df9a90-73b4-4559-8c50-4be5b0e11517)
