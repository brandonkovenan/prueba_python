import os
import pandas as pd
from src.processor import DataProcessor

def test_extract_top_products():
    input_file = './tests/mock_data.xlsx'
    output_file = './tests/output.xlsx'

    # Crear archivo de prueba
    data = {
        "Nombre producto": ["Producto A", "Producto B", "Producto C"],
        "Marca": ["Marca A", "Marca B", "Marca C"],
        "Precio Reportado": [1000, 2000, 3000],
        "Cantidades vendidas": [30, 20, 10],
    }
    df = pd.DataFrame(data)
    df.to_excel(input_file, index=False, sheet_name=0)

    # Instanciar y procesar
    processor = DataProcessor(input_file)
    top_products = processor.extract_top_products(output_file, top_n=2)

    # Verificar resultados
    assert len(top_products) == 2
    assert top_products.iloc[0]["Nombre producto"] == "Producto A"
    assert os.path.exists(output_file)

    # Limpiar
    os.remove(input_file)
    os.remove(output_file)
