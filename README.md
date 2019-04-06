# ProyectoAnalisisLU
Aquí subo el código que ocupamos para hacer el proyecto de Analisis.
Hacer especial enfasis en la solución de sistemas de ecuaciones mediante la factorización LU
La función SolveLUCrout resuelve el sistema pidiendo un arreglo de 8 variables independientes
y otro arreglo de 8 variables dependientes (lista de x y lista de f(x)) encontrando los coeficientes
de un polinomio de (en este caso con unicamente 8 valores de x y f(x)) 7 grado que aproxime a los valores
indicados. 
Se puede cambiar esto en la función Datos, indicando que se tomen mas de 8 valores para cada arreglo.

También se generan funciones para sacar la inversa de una matriz cuadrada a partir del metodo de los cofactores
Es importante destacar que se hace uso de la biblioteca Numpy y sus objetos (en especifico, array) con el que 
se determinaba determinantes y se daba presentación a las matrices. Los objetos array de Numpy ocupan muchos decimales, 
por ello es que hay valores multiplicados por 10 a la -11 o exponentes negativos mayores, para considerar practicamente cero
este tipo de valores generados.
