from src.backend_api.lib.barchartlib import barchart
from src.backend_api.lib.piechartlib import piechart

data = {'Red': 5, 'Blue': 3, 'Yellow': 132, 'Pink': 2}
barchart.drawchart(data)

occupied = 3
piechart.drawchart(occupied)
