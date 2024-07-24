#codificador de hamming que recibe un mensaje binario, calcula los bits de paridad y devuelve el mensaje codificado
import time
def hamming(mensaje, m, r):
    #m es la longitud del mensaje y r es la longitud de los bits de paridad
    #calculamos los bits de paridad
    for i in range(r):
        posicion = 2**i
        mensaje.insert(posicion-1, 0)
    #calculamos los bits de paridad
    for i in range(r):
        posicion = 2**i
        for j in range(1, len(mensaje)+1):
            if j & posicion == posicion:
                mensaje[posicion-1] = mensaje[posicion-1] ^ mensaje[j-1]
    return mensaje

def main():
    print("Ingrese el mensaje a codificar: ")
    mensaje = list(map(int, input()))
    m = len(mensaje)
    r = 0
    while 2**r < m + r + 1:
        r += 1
    mensaje_codificado = hamming(mensaje, m, r)
    print("Mensaje codificado: ")
    for bit in mensaje_codificado:
        print(bit, end="")

if __name__ == "__main__":
    main()