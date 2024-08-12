import subprocess
import argparse


GREEN = '\033[92m' 
RED = '\033[91m'
YELLOW_BOLD = '\033[93m\033[1m'
RESET = '\033[0m'

def ping_domain(domain):
    try:
        result = subprocess.run(
            ['ping', '-c', '2', domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f'{GREEN}{domain} domain is active{RESET}')
        else:
            print(f'{RED}{domain} domain is inactive{RESET}')
    except Exception as e:
        print(f'Error! {domain}: {e}')

def main():
    print(f'{YELLOW_BOLD}Process is starting{RESET}')

    parser = argparse.ArgumentParser(description='Ping domains from a file to check their activity.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the file containing domains to ping.')
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as file:
            domains = file.readlines()
        
        for domain in domains:
            domain = domain.strip()
            if domain:
                ping_domain(domain)
    except FileNotFoundError:
        print(f'Error: The file {args.file} was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')
    

    print(f'{YELLOW_BOLD}Process completed{RESET}')

if __name__ == "__main__":
    main()
