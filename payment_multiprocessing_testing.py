import multiprocessing

def process_payment(account, amount):
    print("Processando pagamento...")
    account['balance'] -= amount
    print(f"Pagamento de {amount} concluído. Saldo restante: {account['balance']}")

def check_balance(account):
    print(f"Verificação de saldo: Saldo atual é {account['balance']}")

def generate_receipt(account, amount):
    print(f"Gerando comprovante para pagamento de {amount}. Saldo final: {account['balance']}")

if __name__ == "__main__":
    account = {'balance': 1000}
    amount = 200

    p1 = multiprocessing.Process(target=process_payment, args=(account, amount))
    p2 = multiprocessing.Process(target=check_balance, args=(account,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    generate_receipt(account, amount)
