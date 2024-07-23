import binascii

def crc32(data):
    return binascii.crc32(data.encode('utf-8')) & 0xFFFFFFFF

def find_errors(original, modified):
    error_positions = []
    for i in range(len(original)):
        if original[i] != modified[i]:
            error_positions.append(i)
    return error_positions

def main():
    input_msg = input("Ingrese el mensaje codificado en binario: ")
    
    # Separar el mensaje y el CRC
    message, received_crc_hex = input_msg[:-8], input_msg[-8:]
    received_crc = int(received_crc_hex, 16)
    
    calculated_crc = crc32(message)
    
    if calculated_crc == received_crc:
        print(f"No se detectaron errores. Mensaje original: {message}")
    else:
        print("Se detectaron errores.")
        error_positions = find_errors(input_msg[:-8], message)
        print(f"Posiciones de los errores: {error_positions}")
    
if __name__ == "__main__":
    main()
