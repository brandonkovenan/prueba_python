# src/processor.py

import pandas as pd

class DataProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def extract_top_products(self, output_file: str, top_n: int = 10):
        # Leer el archivo Excel
        df = pd.read_excel(self.input_file, sheet_name=1, skiprows=7)
        df.columns = df.columns.str.strip()
        
        # Columnas requeridas
        required_columns = ["Nombre producto", "Marca", "Precio Reportado", "Cantidades vendidas"]
        df["Cantidades vendidas"] = pd.to_numeric(df["Cantidades vendidas"], errors="coerce")

        # Filtrar los productos más vendidos
        top_products = (
            df[required_columns]
            .sort_values(by="Cantidades vendidas", ascending=False)
            .head(top_n)
        )

        # Calcular totales
        total_all_products = df["Precio Reportado"].sum()
        total_top_10_products = top_products["Precio Reportado"].sum()
        percentage_top_10 = (total_top_10_products / total_all_products) * 100 if total_all_products else 0

        # Guardar el archivo procesado
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            top_products.to_excel(writer, index=False, sheet_name='Top 10 Productos')
            workbook = writer.book
            worksheet = writer.sheets['Top 10 Productos']
            worksheet.write(len(top_products) + 1, 0, 'Total')
            worksheet.write(len(top_products) + 1, 2, total_top_10_products)

        # Retornar los cálculos para el resumen
        return total_all_products, total_top_10_products, percentage_top_10
