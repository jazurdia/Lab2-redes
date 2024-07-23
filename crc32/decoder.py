# Implementación manual del cálculo de CRC32
def crc32_manual(data):
    crc = 0xFFFFFFFF
    polynomial = 0xEDB88320
    
    for byte in data:
        crc ^= ord(byte)
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
    
    return crc ^ 0xFFFFFFFF

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
    
    calculated_crc = crc32_manual(message)
    
    if calculated_crc == received_crc:
        print(f"No se detectaron errores. Mensaje original: {message}")
    else:
        print("Se detectaron errores.")
        # Find errors by comparing the original message with itself as modified message
        # as the comparison does not make sense in the current form.
        # error_positions = find_errors(message, input_msg[:-8])
        # print(f"Posiciones de los errores: {error_positions}")
    
if __name__ == "__main__":
    main()
