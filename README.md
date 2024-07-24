# Laboratorio 2 - Esquemas de Detección y Corrección de Errores - Parte 1

## Universidad del Valle de Guatemala
**Facultad de Ingeniería**  
**Departamento de Ciencias de la Computación**  
**CC3067 Redes**

### Integrantes
- Alejandro Azurdia, 21242
- Angel Castellanos, 21700
- Diego Morales, 21146

## Descripción del Proyecto
Este proyecto tiene como objetivo implementar y analizar algoritmos de detección y corrección de errores en el contexto de transmisión de datos en redes. Se implementarán al menos dos algoritmos: uno para la detección de errores y otro para la corrección de errores, utilizando distintos lenguajes de programación para el emisor y el receptor.

## Objetivos
- Analizar el funcionamiento de los algoritmos de detección y corrección de errores.
- Implementar algoritmos de detección y corrección de errores.
- Identificar las ventajas y desventajas de cada uno de los algoritmos.

## Algoritmos Implementados
### Corrección de Errores
- **Código de Hamming**: Implementado en C++

### Detección de Errores
- **Checksum de Fletcher**: Implementado en Python3 y en JavaScript
- **CRC-32**: Implementado en Python

## Instrucciones de Uso
### Emisor
1. Solicitar un mensaje en binario.
2. Ejecutar el algoritmo seleccionado y generar la información necesaria para comprobar la integridad del mensaje.
3. Devolver el mensaje en binario concatenado con la información de detección/corrección.

### Receptor
1. Solicitar un mensaje en binario concatenado con la información generada por el emisor.
2. Ejecutar el algoritmo seleccionado y comprobar la integridad del mensaje.
3. Devolver la siguiente información según corresponda:
   - No se detectaron errores: mostrar el mensaje original (sin la información generada por el emisor).
   - Se detectaron errores: indicar que el mensaje se descarta por detectar errores.
   - Se detectaron y corrigieron errores: indicar que se corrigieron errores, indicar posición de los bits que se corrigieron y mostrar el mensaje corregido.

## Escenarios de Prueba
1. Enviar un mensaje al emisor, copiar el mensaje generado por este y proporcionarlo tal cual al receptor.
2. Enviar un mensaje al emisor, copiar el mensaje generado por este y cambiar un bit cualquiera antes de proporcionarlo al receptor.
3. Enviar un mensaje al emisor, copiar el mensaje generado por este y cambiar dos o más bits antes de proporcionarlo al receptor.



