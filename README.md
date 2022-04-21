# Fast Map

> ***Fast Map*** es una herramienta creada en Python que utiliza NMAP con la finalidad de hacer que los escaneos sean efectuados de una manera más fácil y solo con información necesaria.

## Instalación
La instalación es sencilla, con tan solo iniciar el programa se instalan los paquetes necesarios.
- `python3 fastMap.py`

## Uso
- **-t**, **--target**
	- Especifica una IP para escanearla.
		- `python3 fastMap.py -t 127.0.0.1`
	
- **-f**, **--fast**
	- Hace que el escaneo sea más rápido pero solo escanea los 100 puertos más comunes en todos los protocolos.
		- `python3 fastMap.py -t 127.0.0.1 -f`
	
- **-sU**, **--udp**
	- Haz que el escaneo se realice por el protocolo «**UDP**».
		- `python3 fastMap.py -t 127.0.0.1 -f -sU`
	
- **-i**, **--input**
	- Introduce un archivo con las IPs que deseas escanear, el escaneo será automático.
		- `python3 fastMap.py -i archivo.txt -f -sU`
	
- **-o,** **--output**
	- Crea un archivo y guarda la información.
		- `python3 fastMap.py -t 127.0.0.1 -o Targeted.txt`

## Combinaciones
Sí, puedes combinar las opciones, es decir, puedes efectuar un escaneo rápido y UDP al mismo tiempo, aunque hay algunas que **no están permitidas**.
### NO PERMITIDAS
- `python3 fastMap.py -t 127.0.0.1 -i archivo.txt`
	- Ésta combinación dará error, ya que no puedes especificar un archivo de entrada y una IP.

## Dónde funciona
|    OS   |   Tested   |
|:-------:|:----------:|
| Linux   |      ✔️     |
| Windows |      ✔️     |
| Mac     | Not Tested |

___

###### Versión : 0.0.1
- Añadido el "input".
- Añadido el "output".
- Añadido el método "UDP".

___

###### Versión : 0.0.2
- Mover "Modules.py" a "scripts".
- Crear "installModules.py" y añadirlo a "scripts".
- Cambiar el nombre de "Reconocimiento.py" a "fastMap.py".
- Mover "json_data.json" a "log".
