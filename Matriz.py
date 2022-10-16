class Matriz():
    def tamanioMatriz(self,tamanio):
        if tamanio>=1:
            return self.tamanio
        else:
            print("esa matriz no tiene elementos")
    def ingresoDatos(fila,columna):
        while True:
            try:
                fila= int(input("ingrese la fila:"))
                columna= int(input("ingrese la columna:"))
                break
            except ValueError as e:
                print ("error de ingreso de tipo: " + str(e))

        matriz=[]
        for i in range(fila):
            matriz.append([])
            for j in range(columna):
                num=int(input("ingrese sus numeros: "))
                matriz[i].append(num)
        return matriz