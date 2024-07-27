const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const verificarFletcher16 = (mensaje) => {
    let mensajeEnBytes = [];
    
    // Divide el mensaje en bytes
    for (let i = 0; i < mensaje.length - 16; i += 8) {
        mensajeEnBytes.push(parseInt(mensaje.substring(i, i + 8), 2));
    }

    // Separar el mensaje original y el checksum
    const mensajeOriginal = mensaje.substring(0, mensaje.length - 16);
    const checksum = parseInt(mensaje.substring(mensaje.length - 16), 2);

    let sum1 = 0;
    let sum2 = 0;

    // Calcular checksum usando Fletcher-16
    for (let i = 0; i < mensajeEnBytes.length; i++) {
        sum1 = (sum1 + mensajeEnBytes[i]) % 255;
        sum2 = (sum2 + sum1) % 255;
    }

    const checksumCalculado = (sum2 << 8) | sum1;

    // Comparar checksum calculado con el recibido
    return { esValido: checksum === checksumCalculado, mensajeOriginal };
};

// Usar readline para ingresar el mensaje
readline.question('Ingresa tu mensaje en binario: ', mensaje => {
    const { esValido, mensajeOriginal } = verificarFletcher16(mensaje);
    console.log(esValido ? "El mensaje es válido." : "El mensaje es inválido o ha sido alterado.");
    if (esValido) {
        console.log("El mensaje original es: ", mensajeOriginal);
    }
    readline.close();
});
