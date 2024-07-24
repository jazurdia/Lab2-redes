package main

import (
	"fmt"
)

// Función para calcular el CRC32
// Paso 1: Definir la tabla de polinomios para CRC32.
var crc32Table = makeTable(0xedb88320)

func makeTable(poly uint32) []uint32 {
	table := make([]uint32, 256)
	for i := 0; i < 256; i++ {
		crc := uint32(i)
		for j := 0; j < 8; j++ {
			if crc&1 == 1 {
				crc = (crc >> 1) ^ poly
			} else {
				crc >>= 1
			}
		}
		table[i] = crc
	}
	return table
}

// Paso 2: Implementar calculateCRC32 sin usar librerías externas.
func calculateCRC32(data string) uint32 {
	crc := ^uint32(0)
	for _, b := range []byte(data) {
		crc = crc32Table[(byte(crc)^b)&0xFF] ^ (crc >> 8)
	}
	return ^crc
}

// Paso 3: Implementar toHexString para convertir el número a hexadecimal.
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
