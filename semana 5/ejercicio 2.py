#2) “Soy profesor y me encanta inspirar y enseñar a la gente”. ¿Cuántas palabras únicas se han
#utilizado en la frase? Usa los métodos de split y sets para obtener las palabras únicas. (4pto)
frase="soy profesor y me encanta inspirar y enseñar a la gente"
palabras=frase.split()
palabras_unicas=set(palabras)
numero_palabras=len(palabras_unicas)
print(numero_palabras)