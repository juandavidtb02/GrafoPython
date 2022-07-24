#se importan las librerias necesarias
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#algoritmo dijkstra
from algoritmodijkstra import dis

#creacion de la ventana
ventana = tk.Tk()
#ajuste parametros ventanalaboratorio
ventana.title("Grafos")
ventana.geometry('640x580')
ventana.iconbitmap("icon.ico")
ventana.resizable(0,0)
bg_fondo = "#606060"
ventana.configure(background=bg_fondo)

#titulo principal
title = Label(ventana, text="LABORATORIO OPTIMIZACIÓN", font=("Ubuntu",20),bg=bg_fondo,fg='white')
title.pack(side=TOP,pady=10)


#titulo creacion del grafo
title2 = tk.Label(ventana, text="CREACIÓN DEL GRAFO", fg="white", font=('Ubuntu',14),bg=bg_fondo)
title2.pack()

#se declara un vector para guardar los vertices
frameContent = Frame(ventana,width=400,height=370,bg=bg_fondo)
frameContent.pack(pady=60)
#texto entradas
request = tk.Label(frameContent,text="Inserte numero de vertices",font=('Ubuntu',12),bg=bg_fondo,fg="white")
request.pack(pady=5)
#texto fallo
fail = tk.Label(frameContent,text="Ingrese un numero valido de vertices",font=('Arial',12),bg=bg_fondo,fg="white")


#entradas numero de vertices
gVertices = tk.Entry(frameContent, width=5, font=('Ubuntu',12),bg='#BFBFBF' )
gVertices.insert(0,'1')
gVertices.pack(ipadx=5,ipady=5,pady=2)

#entrada origen y destino dijkstra
frameOD = Frame(frameContent, width=200, height=200,bg=bg_fondo)
origen = Entry(frameOD, width=5, font=('Ubuntu',12),bg='#BFBFBF' )
destino = Entry(frameOD, width=5, font=('Ubuntu', 12), bg='#BFBFBF')

#creacion vectores necesarios para el algoritmo
#almacena las etiquetas del grafo
gEtiquetas = []
#almacena las etiquetas de los vertices para ponerlas de nombre en la matriz de adyacencia (destino)
matrizC = []
#almacena las etiquetas de los vertices para ponerlas de nombre en la matriz de adyacencia (origen)
matrizF = []
#guarda los valores de la matriz de adyacencia
matrizGrafica = []
valorEtiquetas = []
#numero de vertices
numv = 0
#matriz que contiene las aristas
matrizAristas = []
#objeto que guarda el grafo
Grafo = nx.DiGraph()
def dijkstra():
    frameBotones.pack_forget()
    frameOD.pack_forget()
    request.pack_forget()
    title2['text'] = 'Algoritmo Dijkstra'
    #creacion objeto dijkstra para realizar el algoritmo
    #el constructor de la clase requiere: las etiquetas, las aristas, el origen y el destino
    d = dis(valorEtiquetas,matrizAristas,origen.get(),destino.get())
    #se realiza el algoritmo dijkstra y se almacena el resultado
    resultado = d.algoritmo_dijkstra()
    frameResultado.pack()

    #creacion de las matrices necesaria para mostrar en pantalla el resultado
    matrizPasos = []
    matrizResultados = []
    for i in range(len(resultado)):
        matrizResultados.append([0] * 3)

    #Crecion de la matriz grafica para mostrar el dijkstra
    pasoTitulo = Label(frameResultado, text='Paso', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
    origenTitulo = Label(frameResultado,text='Origen', font=('Arial', 12), pady=3,bg=bg_fondo,fg="white")
    destinoTitulo = Label(frameResultado, text='Destino', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
    pesoTitulo = Label(frameResultado, text='Peso', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
    pasoTitulo.grid(row=0, column=0, padx=3, pady=1, ipadx=5, ipady=5)
    origenTitulo.grid(row=0, column=1,padx=3,pady=1,ipadx=5,ipady=5)
    destinoTitulo.grid(row=0, column=2,padx=3,pady=1,ipadx=5,ipady=5)
    pesoTitulo.grid(row=0,column=3,padx=3,pady=3,ipadx=5,ipady=5)
    for i in range(len(resultado)):
        matrizPasos.append(Label(frameResultado,text=i+1,font=('Arial', 12), pady=1, bg=bg_fondo, fg="white"))
        matrizPasos[i].grid(row=i+1, column=0)

    for i in range(len(resultado)):
        for j in range(3):
            matrizResultados[i][j] = Label(frameResultado,text=resultado[i][j],font=('Arial', 12), pady=1, bg=bg_fondo, fg="white")
            matrizResultados[i][j].grid(row=i+1,column=j+1,padx=3,pady=1,ipadx=5,ipady=5)

    costo = Label(frameContent,text=f'Costo total: {d.getCosto()}',font=('Arial', 12,'bold'), pady=6, bg=bg_fondo, fg="white")
    costo.pack()
    #print(resultado)
    #print(f'Costo: {d.getCosto()}')
    botonAlgoritmoD.grid_forget()
    frameBotones.pack()

def dijkstra_request():
    botonDijkstra.destroy()
    frameImage.pack_forget()
    frameBotones.pack_forget()
    frameContent.pack(pady=60)
    frameOD.pack(pady=5)
    #entrada origen y destino dijkstra
    request['text'] = 'Inserte origen y destino:'
    labelOrigen = Label(frameOD,text='Inserte origen: ', font=('Arial', 12), pady=3,bg=bg_fondo,fg="white")
    labelDestino = Label(frameOD,text='Inserte destino: ', font=('Arial', 12), pady=3,bg=bg_fondo,fg="white")

    labelOrigen.grid(row=0, column=0)
    labelDestino.grid(row=1, column=0)
    origen.grid(row=0, column=1,ipadx=5,ipady=5,pady=2)
    destino.grid(row=1, column=1,ipadx=5,ipady=5,pady=2)
    botonAlgoritmoD.grid(row=0,column=1)
    frameBotones.pack()




def grafo():
    global matrizAristas
    validarEtiquetas = True
    #verificacion si matriz de adyacencia es valida
    for a in range(numv):
        for fc in range(numv):
            value = matrizGrafica[fc][a].get()
            if value.isspace() or value == '' or not value.isdigit():
                validarEtiquetas = False

    if validarEtiquetas:
        fail.pack_forget()
        #almacenamiento de matriz de adyacencia
        for a in range(numv):
            for fc in range(numv):
                if int(matrizGrafica[fc][a].get()) != 0:
                    matrizAristas.append([valorEtiquetas[a],valorEtiquetas[fc],int(matrizGrafica[fc][a].get())])
                    #print(valorEtiquetas[a] + ' - ' + valorEtiquetas[fc] + ' - ' + matrizGrafica[fc][a].get())
                    #se añaden los vertices segun la matriz de adyacencia introducida
                    Grafo.add_edge(valorEtiquetas[a], valorEtiquetas[fc], weight=int(matrizGrafica[fc][a].get()))

        #print(matrizAristas)
        print(Grafo)
        #creacion de la imagen del grafo
        elarge = [(u, v) for (u, v, d) in Grafo.edges(data=True) if d["weight"] > 0.1]
        esmall = [(u, v) for (u, v, d) in Grafo.edges(data=True) if d["weight"] <= 0.5]
        pos = nx.spring_layout(Grafo, seed=1)  # positions for all nodes - seed for reproducibility

        # nodes
        nx.draw_networkx_nodes(Grafo, pos, node_size=600)

        # edges
        nx.draw_networkx_edges(Grafo, pos, edgelist=elarge, width=3, arrows=True,arrowsize=20)
        nx.draw_networkx_edges(Grafo, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed")

        # node labels
        nx.draw_networkx_labels(Grafo, pos, font_size=20, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(Grafo, "weight")
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("grafo.png")
        # plt.show()

        frameMatriz.destroy()
        botonMatriz.destroy()

        title2['text'] = "GRAFO CREADO"

        frameContent.pack_forget()
        frameImage.pack()
        frameImage.config(padx=120)

        image = Image.open("grafo.png")
        image = image.resize((350, 350))
        imagen = ImageTk.PhotoImage(image)
        Label(frameImage, image=imagen).place(x=0, y=0)

        frameBotones.pack()
        salir.grid(row=0,column=0,padx=5,pady=5)
        botonDijkstra.grid(row=0,column=1)
        #salir.pack(pady=5,ipady=5)
        #nuevoGrafo.pack()
    else:
        fail['text'] = 'Ingrese aristas validas'
        fail.pack(pady=1)

def matriz():
    #verificacion si etiquetas son validas
    validarEtiquetas = True
    for i in range(0,numv):
        value = gEtiquetas[i].get()
        if value.isspace() or value == '':
            validarEtiquetas = False
            break

    if validarEtiquetas:
        #matriz de adyacencia
        fail.pack_forget()
        request['text'] = "Ingrese la matriz de adyacencia"
        #se añaden las etiquetas al grafo para asi tener los vertices
        for i in range(0, numv):
            valorEtiquetas.append(gEtiquetas[i].get())
            Grafo.add_nodes_from(valorEtiquetas)

        frameEtiquetas.pack_forget()

        botonEtiquetas.destroy()
        frameContent.pack_forget()
        frameContent.pack(pady=10)
        frameMatriz.pack()
        #construccion de matriz de adyacencia grafica
        for i in range(numv):
            matrizGrafica.append([0] * numv)

        for i in range(0, numv):
            matrizC.append(Label(frameMatriz, text=valorEtiquetas[i],font=('Arial',12),pady=3,bg=bg_fondo,fg="white"))
            matrizC[i].grid(row=0, column=1 + i)

            matrizF.append(Label(frameMatriz, text=valorEtiquetas[i],font=('Arial',12),pady=3,bg=bg_fondo,fg="white"))
            matrizF[i].grid(row=1 + i, column=0)

        for i in range(numv):
            for j in range(numv):
                matrizGrafica[i][j] = Entry(frameMatriz, width=5, font=('Ubuntu',12),bg='#BFBFBF')
                matrizGrafica[i][j].grid(row=j + 1, column=i + 1,padx=3,pady=3,ipadx=5,ipady=5)
                matrizGrafica[i][j].insert(0, '0')

        botonMatriz.pack(pady=15,ipady=5)
    else:
        fail['text'] = "Ingrese etiquetas a los vertices"
        fail.pack(pady=1)


def numVertices():
    global vertices
    global numv
    #se almacena el numero de vertices introducido
    content = gVertices.get()
    #verificacion si es una entrada valida
    if content.isdigit() and content != '0':
        fail.pack_forget()
        numv = int(content)
        print(numv)
        #nuevo texto
        gVertices.destroy()
        boton1.pack_forget()
        request['text'] = "Ingrese las etiquetas"

        global gEtiquetas
        # entryEtiquetas = []
        # vector para almacenar las etiquetas
        etiqueta = []
        frameEtiquetas.pack(pady=5)
        #entradas etiquetas
        for i in range(0, numv):
            etiqueta.append(Label(frameEtiquetas, text=f"Vertice {i + 1}: ", font=('Arial', 12), pady=3,bg=bg_fondo,fg="white"))
            etiqueta[i].grid(row=i, column=0)

            gEtiquetas.append(Entry(frameEtiquetas, width=5, font=('Ubuntu',12),bg='#BFBFBF'))
            gEtiquetas[i].grid(row=i, column=1,ipadx=5,ipady=5,pady=2)

        botonEtiquetas.pack(pady=3, ipady=5)
    else:
        fail.pack(pady=1)


boton1 = tk.Button(frameContent, text="Crear", command=numVertices,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
boton1.pack(pady=10)

frameEtiquetas = Frame(frameContent, width=200, height=200,bg=bg_fondo)
botonEtiquetas = tk.Button(frameContent, text="Establecer vertices", command=matriz,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)


botonMatriz = tk.Button(frameContent, text="Establecer matriz adyacencia", command=grafo,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)

frameMatriz = Frame(frameContent, width=230, height=230,bg=bg_fondo)
frameImage = Frame(ventana, width=600, height=350,bg=bg_fondo)
frameResultado = Frame(frameContent,width=230, height=230,bg=bg_fondo)

frameBotones = Frame(ventana,width=300,height=20,bg=bg_fondo)
salir = tk.Button(frameBotones, text="Salir", command=quit,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
botonDijkstra = tk.Button(frameBotones, text="Algoritmo Dijkstra",command=dijkstra_request,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
botonAlgoritmoD = tk.Button(frameBotones, text="Realizar algoritmo Dijkstra",command=dijkstra,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
ventana.mainloop()
