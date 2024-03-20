from typing import Dict, List
from booking_bot.booking.domain.models.studio import Studio

class StudioRepository:
    def __init__(self):
        self.studios: Dict[int, Studio] = {}

    def get_by_id(self, studio_id: int) -> Studio:
        return self.studios.get(studio_id)

    def get_all(self) -> List[Studio]:
        return list(self.studios.values())

    def add(self, studio: Studio):
        self.studios[studio.studio_id] = studio