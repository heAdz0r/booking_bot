from typing import Dict
from booking_bot.booking.domain.models.client import Client

class ClientRepository:
    def __init__(self):
        self.clients: Dict[int, Client] = {}

    def get_by_id(self, client_id: int) -> Client:
        return self.clients.get(client_id)

    def get_by_telegram_id(self, telegram_id: int) -> Client:
        for client in self.clients.values():
            if client.telegram_id == telegram_id:
                return client
        return None

    def add(self, client: Client):
        self.clients[client.client_id] = client