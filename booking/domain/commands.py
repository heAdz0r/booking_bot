from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateBookingCommand:
    studio_id: int
    client_id: int
    start_time: str
    duration: int

@dataclass
class CancelBookingCommand:
    booking_id: int

@dataclass
class GetStudioCommand:
    studio_id: int

@dataclass
class GetClientBookingsCommand:
    client_id: int