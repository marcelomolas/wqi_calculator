# Guía de Usuario - WQICalculator

## Introducción
**WQICalculator** es un complemento para QGIS que permite calcular automáticamente el Índice de Calidad del Agua (WQI) a partir de capas ráster de varios parámetros fisicoquímicos. 

Esta guía proporciona instrucciones detalladas sobre la instalación, configuración y uso del plugin.

---

## Instalación
1. Abre QGIS y ve a **Complementos > Administrar e instalar complementos**.
2. En la pestaña **Todos**, busca "WQICalculator".
3. Selecciona el complemento y haz clic en **Instalar complemento**.
4. Una vez instalado, el complemento estará disponible en la barra de herramientas y en el menú **Complementos**.

---

## Requisitos
- QGIS 3.0.0 o superior.
- Un proyecto creado con capas ráster con datos de parámetros fisicoquímicos del agua (pH, sodio, sólidos totales disueltos, entre otros).

---

## Uso del Complemento

### 1. Abrir WQICalculator
- Una vez instalado, accede al complemento desde **Complementos > WQI Calculator** o a través del icono en la barra de herramientas.

![imagen](https://github.com/user-attachments/assets/0ee168ad-a0b4-49a3-ae1f-3ddc657756a7)

### 2. Seleccionar Capas de Entrada
- Cualquier capa que sea agregada al proyecto aparecerá en el listado de capas dentro del plugin, pero solo podrán ser elegidas las capas que sean del tipo ráster.
- No existen restricciones para los nombres de las capas.
- Asegúrate de que las capas tengan el mismo sistema de referencia espacial (CRS) para mejores resultados.
- Haz clic en la capa o haz clic y arrastra el mouse para seleccionar varias capas a la vez.
- Haz clic en el botón "Agregar capas" para seleccionar las capas a utilizarse en el cálculo de WQI.

![imagen](https://github.com/user-attachments/assets/f0cf9a8a-e93f-41fa-93ef-fc877c43830c)

![imagen](https://github.com/user-attachments/assets/0c253747-0cf1-4cdc-a147-9dc32b253379)

### 2.1 Interpolar capa vectorial (Opcional) 
- En caso de que solo cuentes con una capa vectorial con información de múltiples parámetros fisicoquímicos, tendrás la opción de interpolar la capa con IDW (Distancia Inversa Ponderada) usando el algoritmo QGIS "gdal:gridinversedistance".
- Selecciona la capa vectorial y luego haz clic en "Interpolar con IDW".
- Revisa la documentación oficial de QGIS para más información sobre este algoritmo y su funcionamiento: [Inverse Distance to a Power](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/gdal/rasteranalysis.html#grid-inverse-distance-to-a-power).

![imagen](https://github.com/user-attachments/assets/61d84d99-50bc-410d-9edc-4220dda0c004)

### 3. Configurar los Parámetros
- En la interfaz del complemento, selecciona el parámetro correspondiente a cada capa usando la lista desplegable en la columna Parámetro o escribe de forma personalizada los valores ideales, estándar y los pesos de cada parámetro elegido.

![imagen](https://github.com/user-attachments/assets/665288c9-dcbf-4446-be32-53bce180470d)

![imagen](https://github.com/user-attachments/assets/dc798006-3b4f-4ea7-97d8-ddc26cfd3979)

### 4. Escoger el destino de la capa WQI y calcular el Índice de Calidad del Agua
- Haz clic en el botón "..." para elegir la carpeta destino y el nombre del archivo .tif a generarse.
- Haz clic en el botón "Generar WQI".
- El complemento generará una capa ráster con los valores del Índice de Calidad del Agua y se agregará de forma automática al proyecto abierto con el nombre "WQI".

![imagen](https://github.com/user-attachments/assets/5b2866db-6d1f-430e-b397-d0f9eeff52fb)

![imagen](https://github.com/user-attachments/assets/79df9a90-73b4-4559-8c50-4be5b0e11517)
