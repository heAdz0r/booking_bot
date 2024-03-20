class Client:
    def __init__(self, client_id: int, name: str, phone: str, telegram_id: int):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.telegram_id = telegram_id

    def __repr__(self):
        return f"Client(id={self.client_id}, name={self.name}, phone={self.phone}, telegram_id={self.telegram_id})"