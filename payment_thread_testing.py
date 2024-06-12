import threading
import time

def process_payment(account, amount):
    print("Processando pagamento...")
    time.sleep(2)
    account['balance'] -= amount
    print(f"Pagamento de {amount} concluído. Saldo restante: {account['balance']}")

def check_balance(account):
    time.sleep(1)
    print(f"Verificação de saldo: Saldo atual é {account['balance']}")

def generate_receipt(account, amount):
    print(f"Gerando comprovante para pagamento de {amount}. Saldo final: {account['balance']}")

if __name__ == "__main__":
    account = {'balance': 1000}
    amount = 200

    t1 = threading.Thread(target=process_payment, args=(account, amount))
    t2 = threading.Thread(target=check_balance, args=(account,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    generate_receipt(account, amount)
