def notafinaldeprogramacionBAMC():
  #Definir variables y otros 
  print("nota final del curso de Fundamentos de programación")
  #Datos de entrada 
  n1BAMC=int(input("Nota primera unidad:")) 
  n2BAMC=int(input("Nota segunda unidad:")) 
  n3BAMC=int(input("Nota tercera unidad:")) 
  nf4BAMC=int(input("Nota trabajo final:")) 
  #Proceso 
  promediofinalBAMC=(n1BAMC*0.2+n2BAMC*0.15+n3BAMC*0.15+nf4BAMC*0.5) 
  #Datos de salida 
  print("La nota final es:", promediofinalBAMC)


def premiodocenteBAMC():

  #definir variables
  premioObtenidoBAMC=930
  #datos de entrada
  salarioMinimo=float(input("Ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuacion que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=50:
    premioObtenidoBAMC=salarioMinimo+93
  elif puntuacionObtenida>=101 and puntuacionObtenida<=150:
    premioObtenidoBAMC=salarioMinimo+372
  elif puntuacionObtenida>150:
    premioObtenidoBAMC=salarioMinimo+651
  #datos de salida
  print("El docente obtendra un sueldo total de:", premioObtenidoBAMC)




notafinaldeprogramacionBAMC()
#premiodocenteBAMC()