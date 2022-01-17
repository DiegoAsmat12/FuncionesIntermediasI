#Ejercicio 1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
estudiantes[0]['last_name'] = 'Bryant'
directorio_deportes['fútbol'][0] = "Andrés"
z[0]['y'] = 30

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)

#Ejercicio 2
def iterateDictionary(estudiantes):
    estudiantesString= ""
    for diccionario in estudiantes:
        for elementoDeTupla in diccionario.items():
            if(elementoDeTupla[0]=="last_name"):
                estudiantesString += f"{elementoDeTupla[0]} - {elementoDeTupla[1]}\n"
                continue
            estudiantesString += f"{elementoDeTupla[0]} - {elementoDeTupla[1]}, "
    return estudiantesString
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print(iterateDictionary(estudiantes)) 
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;copy
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - T

#Ejercicio 3
def iterateDictionary2(key_name,some_list):
    for diccionario in some_list:
        print(diccionario[key_name])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#Ejercicio 4
def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), str(i).upper())
        for item in some_dict[i]:
            print(item)

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)