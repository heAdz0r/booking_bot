from datetime import datetime
from typing import List
from booking_bot.booking.domain.models.booking import Booking
from booking_bot.booking.infrastructure.repositories.booking_repository import BookingRepository

class BookingService:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def create_booking(self, studio_id: int, client_id: int, start_time: datetime, end_time: datetime) -> Booking:
        booking = Booking(None, studio_id, client_id, start_time, end_time, "pending")
        return self.booking_repository.create(booking)

    def cancel_booking(self, booking_id: int):
        self.booking_repository.delete(booking_id)

    def get_booking_by_id(self, booking_id: int) -> Booking:
        return self.booking_repository.get_by_id(booking_id)

    def get_client_bookings(self, client_id: int) -> List[Booking]:
        return self.booking_repository.get_by_client_id(client_id)