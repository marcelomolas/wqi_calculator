# WQIPlugin

WQIPlugin is a **QGIS** plugin that allows automatic calculation of the **Water Quality Index (WQI)** using raster data of various physicochemical parameters as input.

## Requirements

- **QGIS**: Version 3.38.2 or higher
- **Dependencies**:
  - `QgsRasterCalculator`
  - Algorithm `gdal:gridinversedistance`

## Installation

### From the Official QGIS Repository

1. Open QGIS and go to `Plugins > Manage and Install Plugins`.
2. Search for `WQIPlugin` in the search bar.
3. Click "Install".

### Manual Installation

1. Download the source code from the official repository.
2. Copy the plugin folder to:
   - On Windows: `C:\Users\<user>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`  
   - On Linux/Mac: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
3. Restart QGIS and enable the plugin from the plugin manager.

## Usage

1. Load the raster layers of the required physicochemical parameters into QGIS.
2. Access the plugin from the toolbar or `Plugins > WQIPlugin`.
3. Select the input layers and adjust the parameters as needed.
4. Click "Calculate" to generate the water quality index.

## Example of Use

(Add screenshots or step-by-step workflow)

## Configuration

(Specify if any prior configurations are needed, such as projections, units, etc.)

## License

This plugin is distributed under the **GNU General Public License v3.0**.

## Credits

Developed by: **(Your name or team)**

## Contact

To report bugs or suggestions, you can contact us at: **(Email or project page link)**

Issue tracker: [GitHub Issues](https://github.com/marcelomolas/wqi_plugin/issues)

