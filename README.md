# Previo_Assessment

palindrome: este ejercicio se realizo en python, ya que es uno de los lenguajes que he podido manejar mejor, este ejercicio se inicio transformado el string en un array de numero, y se empezaron a evaluar la igualacion de los numeros desde sus extremos, hasta llegar al centro y evaluamos la cantidad de posibles cambios, para poder asi saber que tanta disponibilidad de cambios existe para convertir el valor en un palindrome evaluando tambien cuantas diferencias hay con respecto a los cambios, ejercicio tal que no salio al 100% ya que presenta fallar en su logica,

la forma de utilizar este codigo esta diseñada para ejecutarse en terminales del sistema, dandole permisos de ejecucion al archivo a travez de un chmod +x *.py, donde *.py son la seleccion de todos los archivos .py existente en el patch actualmente posiscionado despues de esto podemos ejecutar el archivo de la siguiente manera ./palindrome.py, como este archivo recibe parametros debemos realizar lo siguiente ./palindrome string-de-numeros  n_long-string k_maximo numero de cambios

➜  Previo_Assessment git:(main) ✗ chmod +x *.py
➜  Previo_Assessment git:(main) ✗ ./palindrome.py 1221 4 2
9999
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 2
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 1
1231
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 1
1231
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 5
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 5
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 4 3
9239
➜  Previo_Assessment git:(main) ✗ ./palindrome.py '1231' 2 0
-1
➜  Previo_Assessment git:(main) ✗
