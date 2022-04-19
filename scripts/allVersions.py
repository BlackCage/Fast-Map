from modules import *

colorama.init(autoreset=True)

######### Colores ##########
reset = Style.RESET_ALL
gordo = Style.BRIGHT

rojo = Fore.RED
azul = Fore.BLUE
amarillo = Fore.YELLOW
verde = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
############################

nmScan = nmap.PortScanner()

def allVersions(ip, yes, fast, file, output, sU):
    f = open('json_data.json', 'r')
    read = str(f.read())
    f.close()
    data = json.loads(read)
    
    data = [x for x in data if x['target'] == f'{ip}']
    ports = data[0]['ports']

    if sU == True:
        nmScan.scan(f'{ip}', arguments=f'-sU -sV -p{ports} -n --min-rate 5000 -Pn')
    else:
        nmScan.scan(f'{ip}', arguments=f'-sV -p{ports} -n --min-rate 5000 -Pn')

    for host in nmScan.all_hosts():
        state = nmScan[host].state()
        for proto in nmScan[host].all_protocols():
            lport = nmScan[host][proto].keys()
            if yes == False:
                pass
            else:
                with open(f'{output}_{ip}', 'a') as out:
                    out.write(f"===== BASIC INFORMATION =====\n")
                    out.write(f'Target : {ip}\n')
                    out.write(f'State : {state}\n')
                    out.write(f'Protocol : {proto}\n')
                    out.write('===== OPEN PORTS =====\n')
                    out.close()
            for port in lport:
                name = nmScan[host][proto][port]['name']
                product = str(nmScan[host][proto][port]['product']).rstrip().lstrip()
                version = str(nmScan[host][proto][port]['version']).rstrip().lstrip()
                if version == '':
                    if product == '':
                        print(f'{gordo}Port : {azul}{port}{reset}{gordo} ({amarillo}{name}{reset}{gordo}) [ Unknown ]')
                        if yes == True:
                            with open(f'{output}_{ip}', 'a') as f:
                                f.write(f'Port : {port} ({name}) [ Unknown ]\n')
                                f.close()
                        else:
                            pass
                    else:
                        print(f'{gordo}Port : {azul}{port}{reset}{gordo} ({amarillo}{name}{reset}{gordo}) [ {product} Unknown ]')
                        if yes == True:
                            with open(f'{output}_{ip}', 'a') as f:
                                f.write(f'Port : {port} ({name}) [ {product} Unknown ]\n')
                                f.close()
                else:
                    print(f'{gordo}Port : {azul}{port}{reset}{gordo} ({amarillo}{name}{reset}{gordo}) [ {product} {version} ]')
                    if yes == True:
                        with open(f'{output}_{ip}', 'a') as f:
                            f.write(f'Port : {port} ({name}) [ {product} {version} ]\n')
                            f.close()
                    else:
                        pass