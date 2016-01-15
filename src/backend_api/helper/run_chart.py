from src.backend_api.lib.barchartlib import barchart

data= dict(Red=5, Blue = 3, Yellow = 132, Pink=2)
barchart.drawchart(data)


from src.backend_api.lib.piechartlib import piechart

occupied = 3
piechart.drawchart(occupied)