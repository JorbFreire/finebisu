class transactionsController:
    def create():
        pass

    def show(nu):
        card_statements = nu.get_card_statements()
        transactions_list = []

        for card_statement in card_statements:
            transactions = {
                "amount": card_statement["amount"],
                "category": card_statement["category"],
                "description": card_statement["description"],
                "source": card_statement["source"],
                "time": card_statement["time"],
                "title": card_statement["title"],
            }
            transactions_list.append(transactions)

        return transactions_list

    def update():
        pass
