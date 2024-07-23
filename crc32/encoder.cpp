#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

// Función para calcular el CRC32
uint32_t crc32(const std::string& data) {
    uint32_t crc = 0xFFFFFFFF;
    for (char c : data) {
        crc ^= static_cast<uint8_t>(c);
        for (int i = 0; i < 8; i++) {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xEDB88320;
            else
                crc >>= 1;
        }
    }
    return crc ^ 0xFFFFFFFF;
}

std::string to_hex_string(uint32_t num) {
    std::stringstream ss;
    ss << std::hex << std::setw(8) << std::setfill('0') << num;
    return ss.str();
}

int main() {
    std::string input;
    std::cout << "Ingrese el mensaje en binario: ";
    std::cin >> input;

    uint32_t crc = crc32(input);
    std::string crc_hex = to_hex_string(crc);

    std::cout << "Mensaje codificado: " << input << crc_hex << std::endl;
    return 0;
}
