# business_logic.py

from qgis.analysis import QgsRasterCalculatorEntry


class WQICalculatorLogic:
    """
    Capa de negocio:
    - Construye la fórmula del WQI.
    - Define las clases de interpretación del índice.
    No accede a la UI ni al sistema de archivos.
    """

    def build_wqi_formula(self, raster_layers, parametros):
        """
        :param raster_layers: lista de QgsRasterLayer, en el mismo orden que parametros.
        :param parametros: lista de dicts con claves:
                           'estandar' (float), 'ideal' (float), 'peso' (float)
        :return: (formula_str, entries_list)
        """
        if not raster_layers or not parametros:
            raise ValueError("No se proporcionaron capas ni parámetros para el cálculo del WQI.")

        if len(raster_layers) != len(parametros):
            raise ValueError("La cantidad de capas y parámetros no coincide.")

        peso_total = sum(p["peso"] for p in parametros)
        if peso_total == 0:
            raise ValueError("La suma de los pesos es cero. Verifique los valores ingresados.")

        entries = []
        partes = []

        for layer, p in zip(raster_layers, parametros):
            entry = QgsRasterCalculatorEntry()
            entry.bandNumber = 1
            entry.raster = layer
            entry.ref = f"{layer.name()}@1"
            entries.append(entry)

            estandar = p["estandar"]
            ideal = p["ideal"]
            peso_rel = p["peso"] / peso_total

            # Misma estructura que tu código original (con ABS, ponderación y *100)
            quality_rating = (
                f"((ABS({entry.ref} - {ideal}) / ({estandar} - {ideal}))"
                f" * {peso_rel} * 100)"
            )
            partes.append(quality_rating)

        formula = " + ".join(partes)
        return formula, entries

    def get_wqi_classes(self):
        """
        Define las clases del WQI.
        Esto es lógica de dominio, no de QGIS.
        """
        return [
            {
                "limite": 50,
                "label": "<= 50 (Excelente)",
                "color": (145, 203, 168),
            },
            {
                "limite": 100,
                "label": "50 - 100 (Buena)",
                "color": (221, 241, 180),
            },
            {
                "limite": 200,
                "label": "100 - 200 (Mala)",
                "color": (254, 223, 153),
            },
            {
                "limite": 300,
                "label": "200 - 300 (Muy mala)",
                "color": (245, 144, 83),
            },
            {
                "limite": float("inf"),
                "label": "> 300 (No apto para beber)",
                "color": (215, 25, 28),
            },
        ]
