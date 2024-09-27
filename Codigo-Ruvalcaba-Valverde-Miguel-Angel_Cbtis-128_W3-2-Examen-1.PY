print(" ")
print("Nombre: Ruvalcaba Valverde Miguel Angel")
print("----------------------------")
#primero capturemos los valores
A = int(input("Añade un primer valor:"))
B = int(input("Añade un segundo valor:"))
C = int(input("Añade un tercer valor:"))
#usando estas palabras haremos que se desida cual de estos valores seran el mayor y el menor.
#me alegra aver visto esos tutoriales unaque pense que usaria esto mas a futuro y no tan pronto.
max = max(A, B, C)
min = min(A, B, C)
print("----------------------------")
if A==C or A==B or C==B:#ahora abra que haser un print donde digan que valores son iguales.
#y si resta opcion es balida automaticamente se cierra el codigo.
    print("Error, colocaste 2 valores iguales =)")
    exit()#con esto se cierra el codigo, repito me alegra aver visto esos tutoriales.
else:#ahora si se cumple la condicion de que ninguna de las variables se repiten ahora se puede proseder a mostrar las variables.
    print("El valor mayor es:",max)
    print("El valor mmenor es:",min)
#Nota final: al pricipio me llene de emiedo con este codigo y probe mas de 4 ideas diferentes, 
#pero luego cuando puse la cabeza fria y se me ocurrio esta idea para llebarla a cabo descubri que eran las 4:16 y luego me llene de mas miedo
#ahahahhahahahahaha
