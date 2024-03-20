from datetime import datetime
from .studio import Studio
from .client import Client

class Booking:
    def __init__(self, booking_id: int, studio_id: int, client_id: int, start_time: datetime, end_time: datetime, status: str):
        self.booking_id = booking_id
        self.studio_id = studio_id
        self.client_id = client_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def __str__(self):
        return f"Booking(id={self.booking_id}, studio_id={self.studio_id}, client_id={self.client_id}, start_time='{self.start_time}', end_time='{self.end_time}', status='{self.status}')"
