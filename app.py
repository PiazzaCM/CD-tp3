import pandas as pd

# esta funcion lee un archivo csv y retorna una lista con los valores de la columna edades
def lista(csv_file, edades):
    df = pd.read_csv(csv_file)
    lista_valores = df[edades].tolist()
    return lista_valores
#esta funcion recibe una lista de valores y retorna un DataFrame con el analisis estadistico
def analisis_estadistico(lista_valores):
    if not lista_valores:
        return None
    # Calcular frecuencias absolutas solo para los valores presentes en la lista
    fi = {}
    for valor in lista_valores:
        fi[valor] = fi.get(valor, 0) + 1 # Incrementar la frecuencia del valor
    # Crear un DataFrame a partir de las frecuencias absolutas
    df = pd.DataFrame({'fi': list(fi.values())}, index=fi.keys())  # Usar los valores como índices
    # Calcular frecuencias acumuladas
    df['Fi'] = df['fi'].cumsum()
    # Calcular frecuencias relativas
    df['ri'] = df['fi'] / df["fi"].sum()
    # Calcular frecuencias relativas acumuladas
    df['Ri'] = df['ri'].cumsum()
    # Calcular probabilidades
    df['pi'] = df['ri'] * 100
    # Calcular probabilidades acumuladas
    df['Pi'] = df['Ri'] * 100
    
    return df

# Ejemplo de uso
csv_file = "edades.csv"
column_name = "edades"
lista_valores = lista(csv_file, column_name)
df_resultado = analisis_estadistico(lista_valores)
print("Resultado del análisis estadístico:\n", df_resultado)
