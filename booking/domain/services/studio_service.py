from typing import List
from ..models.studio import Studio

class StudioService:
    def __init__(self, studio_repository):
        self.studio_repository = studio_repository

    def get_all_studios(self) -> List[Studio]:
        return self.studio_repository.get_all()

    def get_studio_by_id(self, studio_id: int) -> Studio:
        return self.studio_repository.get_by_id(studio_id)