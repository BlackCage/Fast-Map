from modules import *
from scripts.allPorts import *

################### GLOBAL VARIABLES ###################
######### Colors ###########
reset = Style.RESET_ALL
gordo = Style.BRIGHT

rojo = Fore.RED
azul = Fore.BLUE
amarillo = Fore.YELLOW
verde = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
############################

lisObj = []
colorama.init(autoreset=True)
parser = argparse.ArgumentParser()

######### Arguments ########
parser.add_argument('-t', '--target', required=False)
parser.add_argument('-f', '--fast', required=False, action='store_true')
parser.add_argument('-sU', '--udp', required=False, action='store_true')
parser.add_argument('-i', '--input', required=False)
parser.add_argument('-o', '--output', required=False)
args = parser.parse_args()
############################

ip = args.target
fast = args.fast
file = args.input
output = args.output
sU = args.udp
########################################################

def def_handler(sig, frame):
    sys.exit(f'\n{gordo}{verde}Bye!')
signal.signal(signal.SIGINT, def_handler) # Ctrl+c

def have_internet():
    try:
        internet = requests.get('https://google.com')
    except ConnectionError:
        sys.exit(f"""
{gordo}{rojo}Sorry, I can't perform the scan without internet.{reset}

{gordo}{amarillo}Try this:{reset}{gordo}
    · Check network cables, modem and routers.
    · Re-establish the connection to the wireless network.
        """)

def check():
    global ip
    f = open('json_data.json', 'r')
    read = str(f.read())
    f.close()
    data = json.loads(read)
    target = [x for x in data if x['target'] == f'{ip}']

    if target == []:
        if file == None:
            allPorts(ip, fast, file, output, sU)
        else:
            while True:
                with open(file, 'r') as ips:
                    read = ips.readlines()
                    ips.close()
                for i in read:
                    ip = i.rstrip()
                    f = open('json_data.json', 'r')
                    read = str(f.read())
                    f.close()
                    data = json.loads(read)
                    target = [x for x in data if x['target'] == f'{ip}']
                    if target == []:
                        print(f'{gordo}========================= {amarillo}ANALYZING{reset}{gordo} IP {cyan}{ip}{reset}{gordo} =========================')
                        allPorts(ip, fast, file, output, sU)
                        print(f'{gordo}========================= {magenta}FINISHED{reset}{gordo} IP {cyan}{ip}{reset}{gordo} =========================')
                    else:
                        main(ip)
                print(f'All IPs have already been tested.')
                break
    else:
        main(ip)

def main(ip):
    f = open('json_data.json', 'r')
    read = str(f.read())
    f.close()
    data = json.loads(read)
    target = [x for x in data if x['target'] == f'{ip}']

    while True:
        resp = input(f'The IP {gordo}{cyan}{ip}{reset}{gordo} {amarillo}has already been scanned before{reset}, do you want to scan the IP again? [({gordo}Y{reset})es or ({gordo}n{reset})o]{reset} ')
        if resp == 'Y' or resp == 'y':
            if file == None:
                allPorts(ip, fast, file, output, sU)
                break
            else:
                print(f'{gordo}========================= {amarillo}ANALYZING{reset}{gordo} IP {cyan}{ip}{reset}{gordo} =========================')
                allPorts(ip, fast, file, output, sU)
                print(f'{gordo}========================= {magenta}FINISHED{reset}{gordo} IP {cyan}{ip}{reset}{gordo} =========================')
                break
        elif resp == 'N' or resp == 'n':
            state = target[0]['state']
            protocol = target[0]['protocol']
            ports = target[0]['ports']

            print(f"{gordo}===== BASIC INFORMATION =====")
            print(f'{gordo}Target : {rojo}{ip}')
            print(f'{gordo}State : {verde}{state}')
            print(f'{gordo}Protocol : {cyan}{protocol}')
            print(f"{gordo}===== OPEN PORTS =====")
                
            ports = ports.replace(',', ' ')
            cnt = 0
            while True:
                try:
                    port = ports.split(' ')[cnt]
                    print(f'{gordo}Port : {azul}{port}{reset}{gordo}')
                    cnt += 1
                except:
                    break
            break
        else:
            print(f'The option "{resp}" is not valid.')

if __name__ == '__main__':
    if ip == None:
        if file == None:
            sys.exit(f'{gordo}{rojo}ERROR{reset} : You have to provide an IP or a file with the IPs to test.')
        else:
            pass
    else:
        if file != None:
            sys.exit(f'{gordo}{rojo}ERROR{reset} : You cannot specify an IP and a file.')
    have_internet()
    check()