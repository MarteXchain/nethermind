from web3 import Web3  # pip install web3
import os

def main():
    print("=== Extrator de Chave Privada do Nethermind ===")

    # Solicita o caminho do arquivo Keystore
    keystore_path = input("Digite o caminho completo do arquivo Keystore: ").strip()

    # Verifica se o arquivo existe
    if not os.path.exists(keystore_path):
        print("Erro: Arquivo não encontrado!")
        return

    # Solicita a senha (oculta no terminal, se possível)
    password = input("Digite a senha da carteira: ").strip()

    try:
        # Lê o arquivo Keystore
        with open(keystore_path, 'r') as f:
            keystore = f.read()

        # Decripta a chave privada
        private_key = Web3().eth.account.decrypt(keystore, password)
        print("\n=== Chave Privada Extraída ===")
        print(private_key.hex())

    except Exception as e:
        print(f"\nErro: {e}")
        print("Verifique a senha ou o arquivo Keystore.")

if __name__ == "__main__":
    main()
