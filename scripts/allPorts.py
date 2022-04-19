from modules import *
from scripts.allVersions import allVersions

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

def allPorts(ip, fast, file, output, sU):
    if sU == True:
        if fast == True:
            # List top 1000 common ports on the nmap-services file (fastest way)
            print(f'{gordo}{amarillo}Information :{reset}{gordo} UDP scanning {azul}is generally slower and more difficult than TCP{reset}{gordo}, some security auditors {cyan}ignore these ports{reset}{gordo}.')
            nmScan.scan(f'{ip}', arguments='-F -sU')
        else:
            # Scan all UDP ports with 5000 packets per second (without DNS resolution for better time)
            print(f'{gordo}{amarillo}Information :{reset}{gordo} UDP scanning {azul}is generally slower and more difficult than TCP{reset}{gordo}, some security auditors {cyan}ignore these ports{reset}{gordo}.')
            nmScan.scan(f'{ip}', arguments='-sU -p- -n --min-rate 5000 -Pn')
    else:
        if fast == True:
            if fast == True:
                # List top 1000 common ports on the nmap-services file (fastest way)
                print(f'{gordo}{amarillo}Information :{reset}{gordo} The "{azul}-F{reset}{gordo}" ({azul}fast{reset}{gordo}) option is used to scan {cyan}only the 100 most common ports{reset}{gordo} in each protocol.')
                nmScan.scan(f'{ip}', arguments='-F')
        else:
            # Scan all ports with 5000 packets per second (without DNS resolution for better time)
            print(f'{gordo}{amarillo}Information :{reset}{gordo} This scan will {azul}take a while{reset}{gordo}, {cyan}all ports{reset}{gordo} are being checked.')
            nmScan.scan(f'{ip}', arguments='-sS -p- -n --min-rate 5000 -Pn')
        
    # Run a loop to print all the found result about the ports
    try:
        for host in nmScan.all_hosts():
            print(f"{gordo}===== BASIC INFORMATION =====")
            print(f'{gordo}Target : {rojo}{host}')
            state = nmScan[host].state()
            print(f'{gordo}State : {verde}{state}')
            for proto in nmScan[host].all_protocols():
                print(f'{gordo}Protocol : {cyan}{proto}')
                global protocol
                protocol = proto
                print(f"{gordo}===== OPEN PORTS =====")
                lport = nmScan[host][proto].keys()
                for port in lport:
                    name = nmScan[host][proto][port]['name']
                    print(f'{gordo}Port : {azul}{port}{reset}{gordo} ({amarillo}{name}{reset}{gordo})')
                ports = str(lport)
                ports = ports.replace('dict_keys([', '')
                ports = ports.replace('])', '').rstrip().lstrip()
                ports = ports.replace(' ', '')
        with open('json_data.json') as fp:
            listObj = json.load(fp)
            listObj.append({'target' : host, 'state' : state, 'protocol' : protocol, 'ports' : ports})
            with open('json_data.json', 'w') as json_file:
                json.dump(listObj, json_file, indent=4, separators=(',',': '))
                json_file.close()
            fp.close()

            while True:
                resp = input(f'Do you want to see the versions of the services? [({gordo}Y{reset})es or ({gordo}n{reset})o] ')
                if resp == 'Y' or resp == 'y':
                        if output == None:
                            yes = False
                            allVersions(ip, yes, fast, file, output, sU)
                            break
                        else:
                            yes = True
                            allVersions(ip, yes, fast, file, output, sU)
                            break
                elif resp == 'N' or resp == 'n':
                    if file == None:
                        if output == None:
                            sys.exit(f'{gordo}{verde}Bye!')
                        else:
                            with open(f'{output}_{ip}', 'a') as file_output:
                                file_output.write('===== BASIC INFORMATION =====\n')
                                file_output.write(f'Target : {host}\n')
                                file_output.write(f'State : {state}\n')
                                file_output.write(f'Protocol : {protocol}\n')
                                file_output.write('===== OPEN PORTS =====\n')
                                for port in lport:
                                    name = nmScan[host][proto][port]['name']
                                    file_output.write(f'Port : {port} ({name})\n')
                                file_output.close()
                                break
                    else:
                        if output == None:
                            break
                        else:
                            with open(f'{output}_{host}', 'a') as file_output:
                                file_output.write('===== BASIC INFORMATION =====\n')
                                file_output.write(f'Target : {host}\n')
                                file_output.write(f'State : {state}\n')
                                file_output.write(f'Protocol : {protocol}\n')
                                file_output.write('===== OPEN PORTS =====\n')
                                for port in lport:
                                    name = nmScan[host][proto][port]['name']
                                    file_output.write(f'Port : {port} ({name})\n')
                                file_output.close()
                                break
                else:
                    print(f'The option "{resp}" is not valid.')
    except UnboundLocalError:
        print(f'{gordo}{rojo}ERROR{reset} : It seems that the IP I am trying to scan is down or does not exist.')