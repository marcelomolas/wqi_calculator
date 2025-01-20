# WQIPlugin

WQIPlugin is a **QGIS** plugin that allows automatic calculation of the **Water Quality Index (WQI)** using raster data of various physicochemical parameters as input.

## Requirements

- **QGIS**: Version 3.38.2 or higher
- **Dependencies**:
  - `QgsRasterCalculator`
  - Algorithm `gdal:gridinversedistance`

## Usage

1. Create a QGIS Project
2. Load the project with the raster layers of the physicochemical parameters to be used.
3. If you do not have raster layers but only vector layers, you can use the "Interpolate with IDW ()" to quickly generate raster layers.
4. Access the plugin from the toolbar or `Plugins > WQIPlugin`.
5. Select the input layers and adjust the parameters as needed.
6. Click "Generate WQI" to generate the water quality index raster layer.

## Example of Use

1. Choose your raster layers.
   
![imagen](https://github.com/user-attachments/assets/058433ff-a401-4c8b-ae55-b84229ff08ad)

3. Map the raster layers with physicochemical parameters. Use pre-established values or custom ones.
   
![imagen](https://github.com/user-attachments/assets/137c294e-5b1b-4565-b7db-1f17a4d46e26)

## License

This plugin is distributed under the **GNU General Public License v3.0**.

## Credits

Developed by: **Marcelo Molas and Carin Martínez**

## Contact

To report bugs or suggestions, you can contact us at: **marcemolas@gmail.com or carinme97@gmail.com**

Issue tracker: [GitHub Issues](https://github.com/marcelomolas/wqi_plugin/issues)

