class TransactionManager:
    def __init__(self):
        self.transactions = []

    def perform_transaction(self, account_id, amount):
        transaction = {
            "account_id": account_id,
            "amount": amount
        }
        self.transactions.append(transaction)
        print(f"Transaction successful! Amount: ${amount}")
