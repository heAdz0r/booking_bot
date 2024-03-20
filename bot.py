import logging
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from aiogram import types
from booking.domain import handlers
from booking.domain.commands import CreateBookingCommand, CancelBookingCommand, GetStudioCommand, GetClientBookingsCommand
from booking.infrastructure.repositories.booking_repository import BookingRepository
from booking.infrastructure.repositories.studio_repository import StudioRepository
from booking.infrastructure.repositories.client_repository import ClientRepository
from booking.domain.services.booking_service import BookingService
from booking.domain.services.studio_service import StudioService
from booking.domain.services.client_service import ClientService
from booking.domain.models.studio import Studio
from booking.domain.models.client import Client



# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Инициализация репозиториев и сервисов
booking_repo = BookingRepository()
studio_repo = StudioRepository()
client_repo = ClientRepository()

booking_service = BookingService(booking_repo)
studio_service = StudioService(studio_repo)
client_service = ClientService(client_repo)

# Заполнение репозиториев начальными данными
studio_repo.add(Studio(1, "Studio 1", "Address 1", "Description 1", "10:00-20:00"))
studio_repo.add(Studio(2, "Studio 2", "Address 2", "Description 2", "09:00-21:00"))

client_repo.add(Client(1, "John Doe", "+1234567890", 123456789))
client_repo.add(Client(2, "Jane Smith", "+9876543210", 987654321))

# Регистрация обработчиков команд
dp.register_message_handler(lambda message: handlers.handle_create_booking(message, CreateBookingCommand(**message.get_args()), booking_service), commands=['create_booking'])
dp.register_message_handler(lambda message: handlers.handle_cancel_booking(message, CancelBookingCommand(**message.get_args()), booking_service), commands=['cancel_booking'])
dp.register_message_handler(lambda message: handlers.handle_get_studio(message, GetStudioCommand(**message.get_args()), studio_service), commands=['get_studio'])
dp.register_message_handler(lambda message: handlers.handle_get_client_bookings(message, GetClientBookingsCommand(**message.get_args()), client_service), commands=['get_client_bookings'])


if __name__ == '__main__':
    from aiogram import executor
    from booking.domain import handlers

    # Запуск бота
    executor.start_polling(dp, skip_updates=True)