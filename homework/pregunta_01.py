import os
import zipfile
from pathlib import Path

import pandas as pd


def pregunta_01():
    # 1. Descomprimir el archivo input.zip en la carpeta raíz
    zip_path = Path("files/input.zip")
    extract_to = Path(".")  # se extrae en el directorio actual

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_to)

    # 2. Definir rutas base
    base_input = Path("input")  # asumiendo que el zip crea esta carpeta
    splits = ["train", "test"]
    sentiments = ["negative", "positive", "neutral"]

    # 3. Asegurar que existe la carpeta de salida
    output_dir = Path("files/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 4. Procesar cada split
    for split in splits:
        data = []
        split_path = base_input / split

        for sentiment in sentiments:
            folder = split_path / sentiment
            if not folder.exists():
                continue
            for txt_file in folder.glob("*.txt"):
                with open(txt_file, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()
                data.append({"phrase": phrase, "target": sentiment})

        # Crear DataFrame y guardar CSV
        df = pd.DataFrame(data)
        output_file = output_dir / f"{split}_dataset.csv"
        df.to_csv(output_file, index=False)