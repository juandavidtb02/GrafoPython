#se importan las librerias necesarias
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#creacion de la ventana
ventana = tk.Tk()
#ajuste parametros ventanalaboratorio
ventana.title("Grafos")
ventana.geometry('640x480')
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
vertices = []
frameContent = Frame(ventana,width=400,height=300,bg=bg_fondo)
frameContent.pack(pady=60)
#titulo primera entrada
request = tk.Label(frameContent, text="Inserte numero de vertices",font=('Ubuntu',12),bg=bg_fondo,fg="white")
request.pack(pady=5)

fail = tk.Label(frameContent, text="Ingrese un numero valido de vertices",font=('Arial',12),bg=bg_fondo,fg="white")


#entradas numero de vertices
gVertices = tk.Entry(frameContent, width=5, font=('Ubuntu',12),bg='#BFBFBF' )
gVertices.insert(0,'1')
gVertices.pack(ipadx=5,ipady=5)

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
numv = 0

Grafo = nx.DiGraph()


def grafo():
    validarEtiquetas = True
    for a in range(numv):
        for fc in range(numv):
            value = matrizGrafica[fc][a].get()
            if value.isspace() or value == '':
                validarEtiquetas = False

    if validarEtiquetas:
        fail.pack_forget()
        for a in range(numv):
            for fc in range(numv):
                if int(matrizGrafica[fc][a].get()) != 0:
                    Grafo.add_edge(valorEtiquetas[a], valorEtiquetas[fc], weight=int(matrizGrafica[fc][a].get()))

        # print(matriz)
        print(Grafo)

        elarge = [(u, v) for (u, v, d) in Grafo.edges(data=True) if d["weight"] > 0.5]
        esmall = [(u, v) for (u, v, d) in Grafo.edges(data=True) if d["weight"] <= 0.5]
        pos = nx.spring_layout(Grafo, seed=1)  # positions for all nodes - seed for reproducibility

        # nodes
        nx.draw_networkx_nodes(Grafo, pos, node_size=400)

        # edges
        nx.draw_networkx_edges(Grafo, pos, edgelist=elarge, width=3, arrows=True)
        nx.draw_networkx_edges(Grafo, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed")

        # node labels
        nx.draw_networkx_labels(Grafo, pos, font_size=15, font_family="sans-serif")
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
        request.destroy()
        frameContent.destroy()
        frameImage.pack()
        frameImage.config(padx=120)

        image = Image.open("grafo.png")
        image = image.resize((350, 350))
        imagen = ImageTk.PhotoImage(image)
        Label(frameImage, image=imagen).place(x=0, y=0)

        salir.pack(pady=5,ipady=5)
    else:
        fail['text'] = 'Ingrese aristas validas'
        fail.pack(pady=1)

def matriz():
    validarEtiquetas = True
    for i in range(0,numv):
        value = gEtiquetas[i].get()
        if value.isspace() or value == '':
            validarEtiquetas = False
            break

    if validarEtiquetas:
        fail.pack_forget()
        request['text'] = "Ingrese la matriz de adyacencia"
        for i in range(0, numv):
            valorEtiquetas.append(gEtiquetas[i].get())
            Grafo.add_nodes_from(valorEtiquetas)

        frameEtiquetas.destroy()

        botonEtiquetas.destroy()

        frameMatriz.pack()

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

        botonMatriz.pack(pady=5,ipady=5)
    else:
        fail['text'] = "Ingrese etiquetas a los vertices"
        fail.pack(pady=1)


def numVertices():
    global vertices
    global numv
    content = gVertices.get()

    if content.isdigit() and content != '0':
        fail.pack_forget()
        numv = int(content)
        print(numv)

        for i in range(0, numv):
            vertices.append(i + 1)
        print(vertices)

        gVertices.destroy()
        boton1.destroy()
        request['text'] = "Ingrese las etiquetas"

        global gEtiquetas
        # entryEtiquetas = []
        etiqueta = []

        frameEtiquetas.pack(pady=5)
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

salir = tk.Button(ventana, text="Salir", command=quit,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)

ventana.mainloop()
