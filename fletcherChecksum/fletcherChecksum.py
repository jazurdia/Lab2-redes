def fletcher16(mensaje):
    mensajeBytes = []
    
    for i in range(0, len(mensaje), 8):
        byte_str = mensaje[i:i+8]
        byte = int(byte_str, 2)
        mensajeBytes.append(byte)
    
    sum1 = 0
    sum2 = 0
    for byte in mensajeBytes:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1

def main():
    # mensaje = "1100001110110001"
    mensaje = input("Ingrese el mensaje a enviar: ")

    checksum = fletcher16(mensaje)

    checksumBinario = format(checksum, '016b')
    print("Checksum: ", checksumBinario)
    mensajeAEnviar = mensaje + checksumBinario
    print("Mensaje a enviar: ", mensajeAEnviar)


if __name__ == "__main__":
    main()
