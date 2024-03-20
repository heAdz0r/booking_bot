from typing import Dict, List
from booking_bot.booking.domain.models.booking import Booking

class BookingRepository:
    def __init__(self):
        self.bookings: Dict[int, Booking] = {}
        self.next_id = 1

    def create(self, booking: Booking) -> Booking:
        booking.booking_id = self.next_id
        self.bookings[booking.booking_id] = booking
        self.next_id += 1
        return booking

    def get_by_id(self, booking_id: int) -> Booking:
        return self.bookings.get(booking_id)

    def get_by_client_id(self, client_id: int) -> List[Booking]:
        return [booking for booking in self.bookings.values() if booking.client_id == client_id]

    def delete(self, booking_id: int):
        del self.bookings[booking_id]