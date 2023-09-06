# Previo_Assessment

palindrome: este ejercicio se realizo en python, ya que es uno de los lenguajes que he podido manejar mejor, este ejercicio se inicio transformado el string en un array de numero, y se empezaron a evaluar la igualacion de los numeros desde sus extremos, hasta llegar al centro y evaluamos la cantidad de posibles cambios, para poder asi saber que tanta disponibilidad de cambios existe para convertir el valor en un palindrome evaluando tambien cuantas diferencias hay con respecto a los cambios, ejercicio tal que  salio al 100%.

la forma de utilizar este codigo esta diseñada para ejecutarse en terminales del sistema, dandole permisos de ejecucion al archivo a travez de un chmod +x *.py, donde *.py son la seleccion de todos los archivos .py existente en el patch actualmente posiscionado despues de esto podemos ejecutar el archivo de la siguiente manera ./palindrome.py, como este archivo recibe parametros debemos realizar lo siguiente ./palindrome string-de-numeros  n_long-string k_maximo numero de cambios

➜  Previo_Assessment git:(main) ✗ chmod +x *.py
➜  Previo_Assessment git:(main) ./palindrome.py 923145 6 1 
-1
➜  Previo_Assessment git:(main) ./palindrome.py 923145 6 2
-1
➜  Previo_Assessment git:(main) ./palindrome.py 923145 6 3
[9, 4, 3, 3, 4, 9]
➜  Previo_Assessment git:(main) ./palindrome.py 923145 6 4
[9, 4, 3, 3, 4, 9]
➜  Previo_Assessment git:(main) ./palindrome.py 923145 6 5
[9, 9, 9, 9, 9, 9]
➜  Previo_Assessment git:(main) ./palindrome.py 823145 6 5
[9, 9, 3, 3, 9, 9]
➜  Previo_Assessment git:(main) ./palindrome.py 823145 6 6
[9, 9, 3, 3, 9, 9]
➜  Previo_Assessment git:(main) ./palindrome.py 823145 6 7
[9, 9, 9, 9, 9, 9]
➜  Previo_Assessment git:(main) 
