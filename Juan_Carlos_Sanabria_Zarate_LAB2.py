1#!/usr/bin/env python
# coding: utf-8

#BANCO 


class node:
    def __init__(self, Id = None, Tipo=None, Operacion=None, Tiempo=0, next = None):
        self.Id = Id
        self.Tipo=Tipo
        self.Operacion=Operacion
        self.Tiempo=0
        self.next = next
    
    def __repr__(self):
        return str(self.__dict__)


class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos al final de la cola de la linked list
    def add_at_cola(self, nodo):
        nodo.next=self.head
        self.head = nodo

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al inicio de la cola en la linked list
    def add_at_primero(self, nodo):
        if not self.head:
            self.head = nodo
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nodo
        
    # Método para agregar elementos según pos 
    def add_pos_adelante(self, nodo, pos):
        if not self.head:
            self.head = nodo
            return
        
        pos_actual=self.head
        if pos_actual.Tipo==nodo.Tipo:
            self.add_at_cola(nodo)
            return
                
        cont=1
        while cont<pos:
            cont+=1
            if pos_actual.next and pos_actual.next.Tipo!=nodo.Tipo:
                pos_actual=pos_actual.next
                
        nodo.next=pos_actual.next
        pos_actual.next=nodo
        
    
               
    
    # Método para eleminar nodos según el valor del ID
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.Id != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print ("Cliente ID {0} del Tipo {1} y Tiempo de atención {2}".format(node.Id, node.Tipo, node.Tiempo))
            node = node.next


def leer_archivo_csv(vector, archivo):
    import csv
    '''
    El archivo en cada línea trae el IdCliente, Tipo de Cliente, Operación
    El Tipo de Cliente será P (preferencial), T (Tercera Edad) y N (Normal)
    La operación a realizar será C (Consignar), R (Retirar) y T (Transferencia)
    '''
    with open(archivo, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            '''
              Cada fila (row) trae los 3 campos Id, Tipo y operación
              row es una lista con los tres elementos que son los campos del nodo
              y entonces se mueven al nodo para la lista que queramos utilizar
            '''
            v=node(Id = row[0], Tipo=row[1], Operacion=row[2], Tiempo=0)  
            #v=node(row[0], row[1], row[2], Tiempo=0)
            vector.append(v)


print("** BIENVENIDO A LA SUCURSAL BANCARIA UNIR**")
import os
 
def menu():
    os.system('cls') # NOTA: para windows es cls
    print ("Selecciona una opción")
    print ("\t1 - Leer los datos")
    print ("\t2 - Presentar cola de atención")
    print ("\t3 - Atender los clientes")
    print ("\t4 - Presentar los tiempos promedio")
    print ("\t5 - Salir")
while True:
    # Mostramos el menu
    menu()

    # solicitamos una opción al usuario
    opcionMenu = input("Introduzca el número correspondiente a la acción que desea realizar >> ")
 
    if opcionMenu=="1":
        
        print ("Has pulsado la opción 1 para leer los datos...")  #declaro una lista vacia
        v=[]        
        leer_archivo_csv(v, 'clientes.csv') #El archivo cliente.csv debe estar en la misma carpeta del script o de lo contrario indicar la ruta de manera adecuada
        input("\npulsa Enter para continuar ")
        
    elif opcionMenu=="2":
        
        print ("Has pulsado la opción 2 para desplegar la cola")
        cola = linked_list() # Instancia de la clase lista
        for elemento in v:
            if elemento.Tipo =="T":
                # Aquí se agrega de primero hay que ajustar según el problema
                cola.add_pos_adelante(elemento, 3)

            elif elemento.Tipo=="P":
                # Aquí se agrega de último hay que ajustar según el problema
                cola.add_pos_adelante(elemento, 2)

            else:
                # Aquí se agrega de último sería el caso de cliente normal
                cola.add_at_cola(elemento)
        cola.print_list() # Imprimimos la lista de nodos
        input("...\npulsa Enter para continuar ")
        
    elif opcionMenu=="3":
        
        print ("Has pulsado la opción 3 para Atender los clientes...")
        tiempos=linked_list()
        tiempoe=0
        while not cola.is_empty():
            nodea=cola.get_last_node()
            if nodea.Tipo =='T':
                if nodea.Operacion=='C':
                    tiempoe+=12
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
                if nodea.Operacion=='R':
                    tiempoe+=9
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
                if nodea.Operacion=='T':
                    tiempoe+=10
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
            else:
                if nodea.Operacion=='C':
                    tiempoe+=8
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
                if nodea.Operacion=='R':
                    tiempoe+=6
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
                if nodea.Operacion=='T':
                    tiempoe+=6
                    nodea.Tiempo=tiempoe
                    tiempos.add_at_primero(nodea)
                    cola.delete_node(nodea.Id)
            print ("Cliente ID {0} del Tipo {1} ha sido atendido".format(nodea.Id, nodea.Tipo))
        input("\npulsa una tecla para continuar ")
        
    elif opcionMenu=="4":
        print ("Has pulsado la opción 4 para ver los tiempos promedios...")
        Tiempo_pN=0
        numN=0
        Tiempo_pP=0
        numP=0
        Tiempo_pT=0
        numT=0
        while not tiempos.is_empty():
            i=tiempos.get_last_node()
            if i.Tipo == 'N':
                numN=numN+1
                Tiempo_pN+=i.Tiempo
            if i.Tipo == 'P':
                Tiempo_pP+=i.Tiempo
                numP=numP+1
            if i.Tipo == 'T':
                Tiempo_pT+=i.Tiempo
                numT=numT+1
            tiempos.delete_node(i.Id)
                
        print("El promedio de tiempo de atención para los clientes de tipo general fue de {0} min \nEl promedio de tiempo de atención para los clientes de tipo preferencial fue de {1} min \nEl promedio de tiempo de atención para los clientes de la tercera edad fue de {2} min \n".format(Tiempo_pN/numN, Tiempo_pP/numP,Tiempo_pT/numT))
        
        input("\npulsa Enter para continuar ")
        
    elif opcionMenu=="5":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa Enter para continuar")

