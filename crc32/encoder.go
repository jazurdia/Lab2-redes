package main

import (
	"fmt"
	"hash/crc32"
)

// Función para calcular el CRC32
func calculateCRC32(data string) uint32 {
	return crc32.ChecksumIEEE([]byte(data))
}

// Función para convertir un número a una cadena hexadecimal de 8 caracteres
func toHexString(num uint32) string {
	return fmt.Sprintf("%08x", num)
}

func main() {
	var input string
	fmt.Print("Ingrese el mensaje en binario: ")
	fmt.Scanln(&input)

	crc := calculateCRC32(input)
	crcHex := toHexString(crc)

	fmt.Printf("Mensaje codificado: %s%s\n", input, crcHex)
}
