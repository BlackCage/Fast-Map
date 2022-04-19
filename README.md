# NOMBRE HERRAMIENTA

> (Nombre de la herramienta) es una herramienta creada en Python con la finalidad de hacer que los escaneos sean efectuados de una manera más fácil y solo con información necesaria.

## Uso
- **-t**, **--target**
	- Especifica una IP para escanearla.
		- `python3 (nombre de la herramienta).py -t 127.0.0.1`
	
- **-f**, **--fast**
	- Hace que el escaneo sea más rápido pero solo escanea los 100 puertos más comunes en todos los protocolos.
		- `python3 (nombre de la herramienta).py -t 127.0.0.1 -f`
	
- **-sU**, **--udp**
	- Haz que el escaneo se realice por el protocolo «**UDP**».
		- `python3 (nombre de la herramienta).py -t 127.0.0.1 -f -sU`
	
- **-i**, **--input**
	- Introduce un archivo con las IPs que deseas escanear, el escaneo será automático.
		- `python3 (nombre de la herramienta).py -i archivo.txt -f -sU`
	
- **-o,** **--output**
	- Crea un archivo y guarda la información.
		- `python3 (nombre de la herramienta).py -t 127.0.0.1 -o Targeted.txt`

## Combinaciones
Sí, puedes combinar las opciones, es decir, puedes efectuar un escaneo rápido y UDP al mismo tiempo, aunque hay algunas que **no están permitidas**.
### NO PERMITIDAS
- `python3 (nombre de la herramienta).py -t 127.0.0.1 -i archivo.txt`
	- Ésta combinación dará error, ya que no puedes especificar un archivo de entrada y una IP.
