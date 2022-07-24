#v = ['A','B','C','D','E']
#a = [[0,2,3,0,0],[0,0,0,1,4],[0,0,0,2,0],[0,0,0,0,2],[0,0,0,0,0]]
#v = ['1','2','3','4','5']
#a = [[0,100,30,0,0],[0,0,20,0,0],[0,0,0,10,60],[0,15,0,0,50],[0,0,0,0,0]]

#clase dijkstra
class dis:
    def __init__(self,v,matriz,origen,destino):
        self.v = v
        self.origen = origen
        self.destino = destino
        self.matriz = []
        self.dijkstra = []
        self.matriz = matriz
        self.costo = 0

    def setMatriz(self):
        for ac in range(len(self.v)):
            for fc in range(len(self.v)):
                if self.a[ac][fc] != 0:
                    self.matriz.append([self.v[ac], self.v[fc], self.a[ac][fc]])

    def getCosto(self):
        #funcion para determinar el costo del algoritmo dijkstra
        for i in range(len(self.dijkstra)):
            self.costo = self.dijkstra[i][2] + self.costo
        return self.costo

    def algoritmo_dijkstra(self):
        #funcion algoritmo dijksra
        first_iteracion = True
        peso = 0
        destinopaso = ''
        visitados = []
        existe = False
        #se verifica si el vertice origen y el vertice destino son diferentes
        if self.origen != self.destino:
            llegada = False

        #ciclo para encontrar la ruta, no para hasta encontrar la ruta
        while not llegada:
            #for para recorrer toda la matriz de aristas
            for i in range(len(self.matriz)):
                #verifica si la arista no apunta al mismo vertice
                if self.matriz[i][0] != self.matriz[i][1]:
                    #verifica si el origen actual coincide con las aristas que se estan iterando en el for
                    if self.origen == self.matriz[i][0]:
                        #para comparar los pesos, en cada inicio del for se crea la variable peso para comparar despues
                        if first_iteracion:
                            peso = self.matriz[i][2] + 1
                            first_iteracion = False
                        #se busca el peso menor y si la arista no ha sido registrada anteriormente (para evitar ciclos)
                        if peso > self.matriz[i][2] and self.matriz[i] not in self.dijkstra and not existe:
                            peso = self.matriz[i][2]
                            destinopaso = self.matriz[i][1]
                        else:
                            #se utiliza el segundo menor en caso de que exista un ciclo
                            if existe:
                                peso = self.matriz[i][2]
                                destinopaso = self.matriz[i][1]
                            existe = True

            #se reinician los booleanos necesarios
            first_iteracion = True
            existe = False
            #se guarda la arista en el camino dijkstra
            self.dijkstra.append([self.origen, destinopaso, peso])
            #se guarda el vertice origen para indicar que ya se visito
            visitados.append(self.origen)
            #se establece que el nuevo origen es la variable destino de la arista guardada
            self.origen = destinopaso
            #si ya la variable destinopaso es igual al destino original, se acaba el while
            if destinopaso == self.destino:
                llegada = True
        return self.dijkstra




