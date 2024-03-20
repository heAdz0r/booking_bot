from datetime import datetime
from .studio import Studio
from .client import Client

class Booking:
    def __init__(self, booking_id: int, studio: Studio, client: Client, start_time: datetime, end_time: datetime, status: str):
        self.booking_id = booking_id
        self.studio = studio
        self.client = client
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def __repr__(self):
        return f"Booking(id={self.booking_id}, studio={self.studio.name}, client={self.client.name}, start_time={self.start_time}, end_time={self.end_time}, status={self.status})"