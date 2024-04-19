import pandas as pd

lista_valores = [19,19,29,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22]

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
df_resultado = analisis_estadistico(lista_valores)
print("Resultado del análisis estadístico:\n", df_resultado)