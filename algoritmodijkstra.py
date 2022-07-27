#v = ['A','B','C','D','E']
#a = [[0,2,3,0,0],[0,0,0,1,4],[0,0,0,2,0],[0,0,0,0,2],[0,0,0,0,0]]
#v = ['1','2','3','4','5']
#a = [[0,100,30,0,0],[0,0,20,0,0],[0,0,0,10,60],[0,15,0,0,50],[0,0,0,0,0]]

#clase dijkstra
class dis:
    def __init__(self):
        self.matriz = []
        self.dijkstra = []
        self.costo = 0

    def setMatriz(self):
        for ac in range(len(self.v)):
            for fc in range(len(self.v)):
                if self.a[ac][fc] != 0:
                    self.matriz.append([self.v[ac], self.v[fc], self.a[ac][fc]])

    def getCosto(self):
        #funcion para determinar el costo del algoritmo dijkstra
        self.costo = 0
        for i in range(len(self.dijkstra)):
            self.costo = self.dijkstra[i][2] + self.costo
        return self.costo

    def algoritmo_dijkstra(self,origen,destino,matriz):
        self.matriz = matriz
        self.dijkstra = []
        contadorProceso = 0
        #funcion algoritmo dijksra
        peso = 0
        destinopaso = ''
        existe = False
        llegada = True
        #se verifica si el vertice origen y el vertice destino son diferentes
        if origen != destino:
            llegada = False
        else:
            for i in range(len(self.matriz)):
                if self.matriz[i][0] == self.matriz[i][1] and self.matriz[i][0] == origen:
                    self.dijkstra.append([origen,destino,self.matriz[i][2]])
            if len(self.dijkstra) == 0:
                self.dijkstra.append([origen,destino,0])

        #ciclo para encontrar la ruta, no para hasta encontrar la ruta
        while not llegada:
            #for para recorrer toda la matriz de aristas
            for i in range(len(self.matriz)):
                #verifica si la arista no apunta al mismo vertice
                if self.matriz[i][0] != self.matriz[i][1]:
                    #verifica si el origen actual coincide con las aristas que se estan iterando en el for
                    if origen == self.matriz[i][0]:
                        if self.matriz[i][1] == destino:
                            peso = self.matriz[i][2]
                            destinopaso = self.matriz[i][1]
                            break
                        else:
                            #para comparar los pesos, en cada inicio del for se crea la variable peso para comparar despues
                            if peso == 0:
                                peso = self.matriz[i][2] + 1
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


            self.dijkstra.append([origen, destinopaso, peso])
            peso = 0
            existe = False
            origen = destinopaso
            if destinopaso == destino:
                llegada = True
            contadorProceso = contadorProceso + 1
            if contadorProceso == 10000:
                return False
        return self.dijkstra


