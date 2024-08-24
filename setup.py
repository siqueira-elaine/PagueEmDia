import subprocess
import sys
import os
import platform

def installPackage(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def ensureInquirerInstalled():
    try:
        import inquirer
    except ImportError:
        print("A biblioteca 'inquirer' não está instalada. Instalando agora...")
        installPackage('inquirer')

def installRequirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def runServer():
    subprocess.check_call([sys.executable, "-m", "flask", "run"])

def createVirtualenv():
    if platform.system() == "Windows":
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Ambiente virtual criado. Ative-o usando: .\\venv\\Scripts\\activate")
    else:
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Ambiente virtual criado. Ative-o usando: source venv/bin/activate")

def main():
    ensureInquirerInstalled()
    import inquirer

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[93mPressione CTRL+C para sair\033[0m")

    while True:
        questions = [
            inquirer.List('action',
                          message="Escolha uma opção",
                          choices=['Configurar o ambiente virtual e instalar dependências', 'Apenas instalar dependências', 'Sair'],
                          ),
        ]
        
        answers = inquirer.prompt(questions)
        
        if answers['action'] == 'Configurar o ambiente virtual e instalar dependências':
            createVirtualenv()
            installRequirements()
        elif answers['action'] == 'Apenas instalar dependências':
            installRequirements()
        elif answers['action'] == 'Sair':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
