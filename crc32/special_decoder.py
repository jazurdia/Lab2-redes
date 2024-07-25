# Implementación manual del cálculo de CRC32
def crc32_manual(data):
    crc = 0xFFFFFFFF
    polynomial = 0xEDB88320
    
    for i in range(0, len(data), 8):
        byte = int(data[i:i+8], 2)
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
    
    return crc ^ 0xFFFFFFFF

def flip_bit(data, index):
    # Convierte el string binario a una lista de caracteres
    data_list = list(data)
    # Cambia el bit en el índice especificado
    data_list[index] = '1' if data_list[index] == '0' else '0'
    # Convierte la lista de vuelta a un string
    return ''.join(data_list)

def main():
    input_msg = input("Ingrese el mensaje codificado en binario: \n")
    
    # Separar el mensaje y el CRC
    message, received_crc_bin = input_msg[:-32], input_msg[-32:]
    received_crc = int(received_crc_bin, 2)
    
    # Intentar modificar cada bit del mensaje para encontrar una colisión
    for i in range(len(message)):
        modified_message = flip_bit(message, i)
        calculated_crc = crc32_manual(modified_message)
        
        if calculated_crc == received_crc:
            print(f"Se encontró un mensaje modificado con el mismo CRC.\nMensaje original: {message}\nMensaje modificado: {modified_message}")
            return
    
    print("No se encontraron colisiones de CRC con la modificación de un solo bit.")

if __name__ == "__main__":
    main()
