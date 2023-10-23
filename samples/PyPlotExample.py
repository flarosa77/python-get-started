import matplotlib.pyplot as plt

"""
Figura: il contenitore principale
Axes: il grafico (o i grafici) contenuto nella figura 
Axis: gli assi specifici di un grafico"""

# Contenitore principale
fig, _ = plt.subplots()
type(fig)

# Seleziono il grafico attivo contenuto nella figura
graph = fig.gca()  # Get Current Axes
type(graph)

# Prendiamo tutti i grafici disponibili
graph_list = fig.get_axes()
type(graph_list)

# Disegniamo il grafico
graph.plot([1, 2, 3])

plt.show()  # matplotlib.pytplot.show per gestire finestra
fig.savefig('name.png')  # per salvare immagine su file






