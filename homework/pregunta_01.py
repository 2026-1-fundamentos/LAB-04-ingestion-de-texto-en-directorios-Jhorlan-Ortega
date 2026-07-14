# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""



def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:
    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    import re
    import pandas as pd

    filas = []
    with open("files/input/clusters_report.txt", encoding="utf-8") as file:
        lines = file.readlines()

    fila_actual = None
    for line in lines:
        m = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)", line)
        if m:
            if fila_actual is not None:
                filas.append(fila_actual)
            cluster, cantidad, porcentaje, palabras = m.groups()
            fila_actual = {
                "cluster": int(cluster),
                "cantidad_de_palabras_clave": int(cantidad),
                "porcentaje_de_palabras_clave": float(porcentaje.replace(",", ".")),
                "principales_palabras_clave": palabras.strip(),
            }
        elif (
            fila_actual is not None
            and line.strip() != ""
            and not line.startswith("---")
        ):
            fila_actual["principales_palabras_clave"] += " " + line.strip()

    if fila_actual is not None:
        filas.append(fila_actual)

    df = pd.DataFrame(filas)
    col = df["principales_palabras_clave"]
    col = col.str.replace(r"\s+", " ", regex=True)
    col = col.str.replace(r"\s*,\s*", ", ", regex=True)
    col = col.str.rstrip(".").str.strip()
    df["principales_palabras_clave"] = col
    return df