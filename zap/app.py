from writing.write import write_browser
from writing.write import write_device
from writing.write import write_os

opcao = 0

print("Teste Zap - Nathália Puglisi \n")
print("Opções de Agrupamento: \n"
                    "1 - browser_family \n"
                    "2 - os_family \n"
                    "3 - device_family \n"
                    "4 - Sair")

while opcao != 4:
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        write_browser()
    elif opcao == 2:
        write_os()
    elif opcao == 3:
        write_device()
    else:
        exit

