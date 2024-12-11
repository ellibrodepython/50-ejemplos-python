# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install bokeh
# 2. Ejecuta el script: bokeh serve 41_interactivo_bokeh.py
# 3. Abre el navegador y observa el resultado en http://localhost:5006/

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(height=400, width=400, y_range=[-2.5, 2.5])
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

amplitud = Slider(title="amplitud", value=1.0, start=-5.0, end=5.0, step=0.1)
frecuencia = Slider(title="frecuencia", value=1.0, start=0.1, end=5.1, step=0.1)

def update_data(attrname, old, new):
    a = amplitud.value
    k = frecuencia.value

    x = np.linspace(0, 4*np.pi, N)
    y = a*np.sin(k*x)

    source.data = dict(x=x, y=y)

for w in [amplitud, frecuencia]:
    w.on_change('value', update_data)

curdoc().add_root(
    column(amplitud,
           frecuencia,
           plot, width=800))