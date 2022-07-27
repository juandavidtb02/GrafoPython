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
ventana.geometry('680x620')
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
frameContent = Frame(ventana,width=400,height=500,bg=bg_fondo)
frameContent.pack()
#texto entradas
request = tk.Label(frameContent,text="Inserte numero de vertices",font=('Ubuntu',12),bg=bg_fondo,fg="white")
request.pack(pady=5)
#texto fallo
fail = tk.Label(frameContent,text="Ingrese un numero valido de vertices",font=('Arial',12),bg=bg_fondo,fg="white")

imagePack = Label(ventana,bg=bg_fondo)
costo = Label(frameContent, font=('Arial', 12, 'bold'), pady=6,bg=bg_fondo, fg="white")
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
d = dis()
matrizResultados = []
matrizPasos = []
grafoGenerado = False

def dijkstra():
    if origen.get() in valorEtiquetas and destino.get() in valorEtiquetas:
        frameBotones.pack_forget()
        frameOD.pack_forget()
        request.pack_forget()
        title2['text'] = 'Algoritmo Dijkstra'
        newdijkstra.pack(padx=5, pady=5)
        botonAlgoritmoD.grid_forget()
        # se realiza el algoritmo dijkstra y se almacena el resultado
        resultado = d.algoritmo_dijkstra(origen.get(),destino.get(),matrizAristas)
        if resultado != False:
            fail.pack_forget()
            # creacion de las matrices necesaria para mostrar en pantalla el resultado
            global matrizResultados
            global matrizPasos

            matrizPasos = []
            # Crecion de la matriz grafica para mostrar el dijkstra
            pasoTitulo = Label(frameResultado, text='Paso', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
            origenTitulo = Label(frameResultado, text='Origen', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
            destinoTitulo = Label(frameResultado, text='Destino', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
            pesoTitulo = Label(frameResultado, text='Peso', font=('Arial', 12), pady=3, bg=bg_fondo, fg="white")
            pasoTitulo.grid(row=0, column=0, padx=3, pady=1, ipadx=5, ipady=5)
            origenTitulo.grid(row=0, column=1, padx=3, pady=1, ipadx=5, ipady=5)
            destinoTitulo.grid(row=0, column=2, padx=3, pady=1, ipadx=5, ipady=5)
            pesoTitulo.grid(row=0, column=3, padx=3, pady=3, ipadx=5, ipady=5)

            for i in range(len(resultado)):
                matrizPasos.append(
                    Label(frameResultado, text=i + 1, font=('Arial', 12), pady=1, bg=bg_fondo, fg="white"))
                matrizPasos[i].grid(row=i + 1, column=0)

            for i in range(len(resultado)):
                matrizResultados.append([])
                for j in range(3):
                    matrizResultados[i].append(
                        Label(frameResultado, text=resultado[i][j], font=('Arial', 12), pady=1, bg=bg_fondo,
                              fg="white"))
                    matrizResultados[i][j].grid(row=i + 1, column=j + 1, padx=3, pady=1, ipadx=5, ipady=5)
            frameResultado.pack()
            costo['text'] = f"Costo total: {d.getCosto()}"
            costo.pack()
            # print(resultado)
            # print(f'Costo: {d.getCosto()}')
            frameBotones.pack()

        else:
            fail['text'] = "No existe conexión entre los dos vertices ingresados"
            fail.pack(pady=1)
            frameBotones.pack()
    else:
        fail['text'] = 'Ingrese vertices validos'
        fail.pack(pady=1)

def dijkstra_request():
    global matrizResultados
    costo.pack_forget()
    newdijkstra.pack_forget()
    for i in range(len(matrizResultados)):
        for j in range(3):
            matrizResultados[i][j].destroy()
    for i in range(len(matrizPasos)):
        matrizPasos[i].destroy()
    matrizResultados = []
    frameResultado.pack_forget()

    fail.pack_forget()
    botonDijkstra.grid_forget()
    imagePack.pack_forget()
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
    botonAlgoritmoD.grid(row=0,column=1,padx=5)
    vergrafo.grid(row=0,column=2)
    frameBotones.pack()




def grafo():
    global matrizAristas
    global grafoGenerado
    validarEtiquetas = True
    if not grafoGenerado:
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
                        #se añaden los vertices segun la matriz de adyacencia introducida
                        Grafo.add_edge(valorEtiquetas[a], valorEtiquetas[fc], weight=int(matrizGrafica[fc][a].get()))

            #print(matrizAristas)
            print(Grafo)
            #creacion de la imagen del grafo
            pos = nx.spring_layout(Grafo)
            nx.draw_networkx(Grafo, pos, with_labels=True, font_weight='bold', font_color='white')
            labels = nx.get_edge_attributes(Grafo, 'weight')

            nx.draw_networkx_edges(Grafo, pos, arrowsize=10, arrowstyle='->', width=1)
            nx.draw_networkx_nodes(Grafo, pos, node_size=300, node_color='black')
            nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=labels)

            ax = plt.gca()
            ax.set_facecolor(bg_fondo)
            ax.margins(0.1)
            plt.savefig('grafo.png', transparent = True, bbox_inches = 'tight', pad_inches = 1)
            # plt.show()

            frameMatriz.destroy()
            botonMatriz.destroy()

            title2['text'] = "GRAFO CREADO"


            #frameImage.pack()
            #frameImage.config(padx=120)

            image = Image.open("grafo.png")
            image = image.resize((640, 480))
            imagen = ImageTk.PhotoImage(image)
            imagePack['image'] = imagen
            grafoGenerado = True
            salir.grid(row=0, column=0, padx=5, pady=1)
        else:
            fail['text'] = 'Ingrese aristas validas'
            fail.pack(pady=1)
            return 0

    botonAlgoritmoD.grid_forget()
    newdijkstra.pack_forget()
    frameResultado.pack_forget()
    vergrafo.grid_forget()
    frameContent.pack_forget()
    frameBotones.pack_forget()

    imagePack.pack()
    frameBotones.pack()
    botonDijkstra.grid(row=0, column=1)
    # salir.pack(pady=5,ipady=5)
    # nuevoGrafo.pack()

def matriz():
    #verificacion si etiquetas son validas
    validarEtiquetas = True
    comprobacion = []
    for i in range(0,numv):
        value = gEtiquetas[i].get()
        comprobacion.append(gEtiquetas[i].get())
        if value.isspace() or value == '':
            validarEtiquetas = False
            break
        if comprobacion.count(value) > 1:
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
        numv = int(content)
        if numv <= 10:
            fail.pack_forget()
            print(numv)
            # nuevo texto
            gVertices.destroy()
            boton1.pack_forget()
            request['text'] = "Ingrese las etiquetas"
            global gEtiquetas
            # vector para almacenar las etiquetas
            etiqueta = []
            frameEtiquetas.pack(pady=5)
            # entradas etiquetas
            for i in range(0, numv):
                etiqueta.append(
                    Label(frameEtiquetas, text=f"Vertice {i + 1}: ", font=('Arial', 12), pady=3, bg=bg_fondo,
                          fg="white"))
                etiqueta[i].grid(row=i, column=0)

                gEtiquetas.append(Entry(frameEtiquetas, width=5, font=('Ubuntu', 12), bg='#BFBFBF'))
                gEtiquetas[i].grid(row=i, column=1, ipadx=5, ipady=5, pady=2)

            botonEtiquetas.pack(pady=3, ipady=5)
        else:
            fail['text'] = "El numero maximo de vertices permitidos es 10"
            fail.pack(pady=1)
    else:
        fail.pack(pady=1)


boton1 = tk.Button(frameContent, text="Crear", command=numVertices,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
boton1.pack(pady=10)

frameEtiquetas = Frame(frameContent, width=200, height=200,bg=bg_fondo)
botonEtiquetas = tk.Button(frameContent, text="Establecer vertices", command=matriz,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)


botonMatriz = tk.Button(frameContent, text="Establecer matriz adyacencia", command=grafo,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)

frameMatriz = Frame(frameContent, width=230, height=230,bg=bg_fondo)
#frameImage = Frame(ventana, width=600, height=350,bg=bg_fondo)
frameResultado = Frame(frameContent,width=230, height=230,bg=bg_fondo)

frameBotones = Frame(ventana,width=300,height=20,bg=bg_fondo)
salir = tk.Button(frameBotones, text="Salir", command=quit,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
vergrafo = tk.Button(frameBotones, text="Ver grafo", command=grafo,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
botonDijkstra = tk.Button(frameBotones, text="Algoritmo Dijkstra",command=dijkstra_request,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
botonAlgoritmoD = tk.Button(frameBotones, text="Realizar algoritmo Dijkstra",command=dijkstra,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
newdijkstra = tk.Button(ventana, text="Encontrar nueva ruta",command=dijkstra_request,font=('Ubuntu',10,'bold'),cursor="hand2",relief="raised",borderwidth=5,height=1)
ventana.mainloop()
