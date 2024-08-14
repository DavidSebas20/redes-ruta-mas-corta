# Aplicación de Ruta Más Corta en un Grafo

Esta es una aplicación de escritorio construida con `Tkinter` que permite a los usuarios interactuar con un grafo, agregar nodos y conexiones, y encontrar la ruta más corta entre dos nodos usando el algoritmo de Dijkstra.

## Características

- **Agregar Nodo**: Permite agregar nodos al grafo.
- **Agregar Conexión**: Permite definir conexiones entre nodos con una distancia asociada.
- **Ruta Más Corta**: Calcula y muestra la ruta más corta entre dos nodos usando el algoritmo de Dijkstra.
- **Visualización**: Muestra gráficamente el grafo con la ruta más corta resaltada.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio o descarga los archivos.

```bash
git clone https://github.com/tu_usuario/ruta-mas-corta-grafo.git
```

2. Navega al directorio del proyecto.

```bash
cd ruta-mas-corta-grafo
```

3. Instala las dependencias necesarias.

```bash
pip install requirements.txt
```
## Uso
Ejecuta la aplicación desde la línea de comandos utilizando Python:

```bash
python nombre_del_archivo.py
```

### Interfaz de Usuario

**Agregar Nodo:** Introduce el nombre del nodo y haz clic en "Agregar Nodo".

**Agregar Conexión:** Introduce dos nodos y una distancia en el formato Nodo1 Nodo2 Distancia y haz clic en "Agregar Conexión".

**Ruta Más Corta:**
Introduce el nodo de inicio y el nodo de fin.
Haz clic en "Mostrar Ruta Más Corta" para calcular y visualizar la ruta más corta.
La ruta más corta y su distancia se mostrarán en el área de texto inferior.

**Visualización del Grafo:** El grafo se muestra en una nueva ventana con la ruta más corta resaltada.