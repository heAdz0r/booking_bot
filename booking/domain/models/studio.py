
class Studio:
    def __init__(self, studio_id: int, name: str, address: str, description: str, working_hours: str):
        self.studio_id = studio_id
        self.name = name
        self.address = address
        self.description = description
        self.working_hours = working_hours

    def __str__(self):
        return f"Studio(id={self.studio_id}, name='{self.name}', address='{self.address}', description='{self.description}', working_hours='{self.working_hours}')"