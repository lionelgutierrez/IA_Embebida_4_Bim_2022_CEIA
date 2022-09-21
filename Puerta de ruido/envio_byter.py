import serial

#Defino el peurto en windows
s = serial.Serial('COM3')

#Defino baudrate y timeout para la lectura
s.baudrate = 9600
s.timeout=3

print("Nombre del puerto: ",s.name)
print("Envio un dato")
valor_enviar = 50
caracter = 'p'
if valor_enviar < 0:
    valor = -1*valor_enviar
    caracter = 'n'
else:
    valor = valor_enviar

#bytesenviar = valor.to_bytes(2, 'little')
#bytesenviar += caracter.encode("Ascii")
#cant = s.write(bytesenviar)
#print("Cantidad de datos enviados: ",cant)
cant = s.write(valor.to_bytes(2, 'little'))
print("Cantidad de datos enviados: ",cant)
cant = s.write(caracter.encode("Ascii"))
#cant = s.write(caracter.to_bytes(1, 'little'))
print("Cantidad de datos enviados: ",cant)
res = s.read(2)
print(res)
print(len(res))
#print("Signo: ",res[2].decode("Ascii"))
res_int = int.from_bytes(res, 'little')

print("Datos recibido: ",res_int)

signo_byte = s.read()
print(len(signo_byte))
print(signo_byte)
signo =  signo_byte.decode("Ascii")#int.from_bytes(signo_byte, 'little')#
#if signo == 'n':
#    print("Datos recibido n: ",-res_int)
#else:    
#    print("Datos recibido p: ",res_int)
print("Signo out: ",signo)