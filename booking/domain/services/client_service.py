from typing import List
from booking_bot.booking.domain.models.client import Client
from booking_bot.booking.domain.models.booking import Booking
from booking_bot.booking.infrastructure.repositories.client_repository import ClientRepository

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_client_by_id(self, client_id: int) -> Client:
        return self.client_repository.get_by_id(client_id)

    def get_client_by_telegram_id(self, telegram_id: int) -> Client:
        return self.client_repository.get_by_telegram_id(telegram_id)

    def get_client_bookings(self, client_id: int) -> List[Booking]:
        return self.booking_repository.get_by_client_id(client_id)