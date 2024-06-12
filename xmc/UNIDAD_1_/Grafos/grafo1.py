import matplotlib.pyplot as pit # type: ignore

#CREAMOS UN GRAFO VACIO
grafo = {}

#AGREGAMOS VERTICES AL GRAFO
grafo ["A"] = ["B" , "C"]
grafo ["B"] = ["D"]
grafo ["C"] = ["D"]
grafo ["D"] = []

#GRAFICAMOS AL GRAFO
fig, ax = pit.subplots()
vertices = list (grafo.keys ())
for i , vertice in enumerate(vertices):
    for adyacente in grafo (vertice):
        j = vertices.index(adyacente)
        ax.plot([i , j] , [0 , 1] , "b-", )
        ax.text((i + j)/2 , 0.5 , vertice +"->" + adyacente , ha = "center" , va = -10 )

ax.set_xlist(-0.5 , len (vertices) - 0.5 )
ax.set_ylim(-0.5 , 1.5 )
ax.set_xticks(range(len(vertices)))
ax.set_xticklabels(vertices)
ax.set_yticks([])
ax.set_title("Grafo_dirigido")