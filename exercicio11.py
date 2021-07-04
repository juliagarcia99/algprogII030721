class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
###

class Torre:
    def __init__(self, idtorre, nome, endereco):
        self.idtorre = idtorre
        self.nome = nome
        self.endereco = endereco

    def printTorre(self):
        print(self.idtorre)
        print(self.nome)
        print(self.endereco)

class Apartamento:
    def __init__(self, idapto, numero, torre, vaga):
        self.idapto = idapto
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
    def printapto(self):
        print(self.idapto)
        print(self.numero)
        print(self.torre)
        print(self.vaga)

class listadeespera:
    def __init__(self)
        self.head = None
        self._size = 0
    
    def adicionar(self, elem):
        if self.head:
            #inserção qdo a listadeespera ja possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção na listadeespera
            self.head = Node(elem)
        self.size = self.size + 1

    def __getitem_(self, index):
        #exemplo: listadeespera.get(2)
        pointer = self.head
        for i in range (index):
            if pointer: 
                pointer = pointer.next
            else:
                raise IndexError("esse indice n existe na lista")
            if pointer:
                return pointer.data
            raise IndexError ("esse indice n existe na lista")



    def deletarapto(self, elem):
            temp = self.head
            if (temp is not None):
                if (temp.data == elem):
                    self.head = temp.next
                    temp = None
                    return

            while(temp is not None):
                if temp.data == elem:
                    break
                prev = temp
                temp = temp.next
                if(temp == None):
                return
                prev.next = temp.next
            temp = None
    
    def printlistadeespera(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next