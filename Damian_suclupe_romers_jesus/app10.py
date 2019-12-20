import os
import libreria
#programa para calcular la pendiente de la recta ortogonal a otra recta.
#INPUT
pendiente=int(os.sys.argv[1])
#processing
pendiente_ortogonal=libreria.calc_pendiente(pendiente)
#output
print("El valor de la pendiente ortogonal es:", pendiente_ortogonal)
