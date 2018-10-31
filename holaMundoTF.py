# Importamos la librería
import tensorflow as tf
# Creamos un tensor de constante con el mensaje que queremos
holamundo = tf.constant("Hola mundo")
# Creamos una sesión, le damos el nombre "sesion" y la ejecutamos como sesión por defecto (default)
with tf.Session() as sesion:
    print(sesion.run(holamundo))

'''
Alternativa para crear sesión y lanzarla:
sesion = tf.Session()
print(sesion.run(holamundo))
'''