from __future__ import print_function

import tensorflow as tf

# Creamos un gráfico.
g = tf.Graph()
# Lo definimos como el predeterminado.
with g.as_default():
  # El gráfico empieza con 3 operaciones:
  #   * Dos operaciones de constente tf.constant para crear operandos.
  #   * Una operación de adición tf.add para sumar los operandos.
  x = tf.constant(12, name="x_const")
  y = tf.constant(9, name="y_const")
  my_sum = tf.add(x, y, name="x_y_sum")

  #Ahora añadimos un tercer escalar y lo sumamos a la suma de x, y anterior.
  z = tf.constant(4, name="z_const")
  my_new_sum = tf.add(my_sum, z, name="x_y_z_sum")

  # Ahora creamos la sesión donde se ejecutará el gráfico predeterminado.
  with tf.Session() as sess:
    print(my_sum.eval())
    print(my_new_sum.eval())



