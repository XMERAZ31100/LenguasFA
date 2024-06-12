import matplotlib.pyplot as pit  # type: ignore

#ESTE CODIGO CREA UN GRAFO CON 4 VERTICES (A , B , C , D )
#CREAMOS UN GRAFO VACIO 
grafo = {}

#AGREGAMOS VERTICES AL GRAFO 
grafo["A"] = ["B" , "C"]
grafo["B"] = ["D"]
grafo["C"] = ["D"] 
grafo["D"] = []

#IMPRIME EL GRAFO 
print("El grafo es:")

for vertice , adyacente in grafo.items():
    print(f"Vertice {vertice} -> {adyacente}")