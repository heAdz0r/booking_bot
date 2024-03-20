import os

folders = [
    "booking/domain/models",
    "booking/domain/services",
    "booking/infrastructure/repositories",
    "config",
    "utils",
]

files = [
    ("booking/domain/models/__init__.py", ""),
    ("booking/domain/models/booking.py", ""),
    ("booking/domain/models/client.py", ""),
    ("booking/domain/models/studio.py", ""),
    ("booking/domain/services/__init__.py", ""),
    ("booking/domain/services/booking_service.py", ""),
    ("booking/domain/services/studio_service.py", ""),
    ("booking/domain/commands.py", ""),
    ("booking/domain/handlers.py", ""),
    ("booking/infrastructure/__init__.py", ""),
    ("booking/infrastructure/database.py", ""),
    ("booking/infrastructure/repositories/__init__.py", ""),
    ("booking/infrastructure/repositories/booking_repository.py", ""),
    ("booking/infrastructure/repositories/studio_repository.py", ""),
    ("booking/__init__.py", ""),
    ("config/__init__.py", ""),
    ("config/settings.py", ""),
    ("config/config.ini", ""),
    ("utils/__init__.py", ""),
    ("utils/fsm.py", ""),
    ("bot.py", ""),
    ("requirements.txt", ""),
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_name, content in files:
    with open(file_name, "w") as file:
        file.write(content)
