#v = ['A','B','C','D','E']
#a = [[0,2,3,0,0],[0,0,0,1,4],[0,0,0,2,0],[0,0,0,0,2],[0,0,0,0,0]]
#v = ['1','2','3','4','5']
#a = [[0,100,30,0,0],[0,0,20,0,0],[0,0,0,10,60],[0,15,0,0,50],[0,0,0,0,0]]

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
        for i in range(len(self.dijkstra)):
            self.costo = self.dijkstra[i][2] + self.costo
        return self.costo

    def algoritmo_dijkstra(self):

        first_iteracion = True
        peso = 0
        destinopaso = ''
        visitados = []
        existe = False

        if self.origen != self.destino:
            llegada = False

        while not llegada:
            for i in range(len(self.matriz)):
                if self.matriz[i][0] != self.matriz[i][1]:
                    if self.origen == self.matriz[i][0]:
                        if first_iteracion:
                            peso = self.matriz[i][2] + 1
                            first_iteracion = False
                        if peso > self.matriz[i][2] and self.matriz[i] not in self.dijkstra and not existe:
                            peso = self.matriz[i][2]
                            destinopaso = self.matriz[i][1]
                        else:
                            if existe:
                                peso = self.matriz[i][2]
                                destinopaso = self.matriz[i][1]
                            existe = True

            first_iteracion = True
            existe = False
            self.dijkstra.append([self.origen, destinopaso, peso])
            visitados.append(self.origen)
            self.origen = destinopaso
            if destinopaso == self.destino:
                llegada = True
        return self.dijkstra




