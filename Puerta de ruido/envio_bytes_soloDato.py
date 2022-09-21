import serial

#Defino el peurto en windows
s = serial.Serial('COM3')

#Defino baudrate y timeout para la lectura
s.baudrate = 9600
s.timeout=3

print("Nombre del puerto: ",s.name)
print("Envio un dato")
valor_enviar = 6000
caracter = 'p'
if valor_enviar < 0:
    valor = -1*valor_enviar
    caracter = 'n'
else:
    valor = valor_enviar

valor_unsigned = int.from_bytes(valor.to_bytes(2, 'little',signed=True),'little',signed=False)
cant = s.write(valor_unsigned.to_bytes(2, 'little'))
print("Cantidad de datos enviados: ",cant)
res = s.read(2)
print(res)
print(len(res))
#print("Signo: ",res[2].decode("Ascii"))
res_int = int.from_bytes(res, 'little')
print("Datos recibido: ",res_int)
