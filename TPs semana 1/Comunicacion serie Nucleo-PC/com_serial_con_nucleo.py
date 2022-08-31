import serial

#Defino el peurto en windows
s = serial.Serial('/dev/ttyACM0')

#Defino baudrate y timeout para la lectura
s.baudrate = 9600
s.timeout=3

print("Nombre del puerto: ",s.name)
print("Envio un dato")
caracter = 'a'
cant = s.write(caracter.encode("Ascii"))
#cant = s.write(b'a')
print("Cantidad de datos enviados: ",cant)
res = s.read()
print("Datos recibido: ",res.decode("Ascii"))