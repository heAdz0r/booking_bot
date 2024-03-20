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
client_service = ClientService(client_repo, booking_repo)

# Заполнение репозиториев начальными данными
studio_repo.add(Studio(1, "Studio 1", "Address 1", "Description 1", "10:00-20:00"))
studio_repo.add(Studio(2, "Studio 2", "Address 2", "Description 2", "09:00-21:00"))

client_repo.add(Client(1, "John Doe", "+1234567890", 123456789))
client_repo.add(Client(2, "Jane Smith", "+9876543210", 987654321))

# Регистрация обработчиков команд
# Регистрация обработчиков команд
async def create_booking_handler(message: types.Message):
    args = message.get_args().split()
    command = CreateBookingCommand(
        studio_id=int(args[0]),
        client_id=int(args[1]),
        start_time=f"{args[2]} {args[3]}",
        duration=int(args[4])
    )
    await handlers.handle_create_booking(message, command, booking_service)
async def cancel_booking_handler(message: types.Message):
    args = message.get_args().split()
    command = CancelBookingCommand(booking_id=int(args[0]))
    await handlers.handle_cancel_booking(message, command, booking_service)

async def get_studio_handler(message: types.Message):
    args = message.get_args().split()
    command = GetStudioCommand(studio_id=int(args[0]))
    await handlers.handle_get_studio(message, command, studio_service)

async def get_client_bookings_handler(message: types.Message):
    args = message.get_args().split()
    command = GetClientBookingsCommand(client_id=int(args[0]))
    await handlers.handle_get_client_bookings(message, command, client_service)

dp.register_message_handler(create_booking_handler, commands=['create_booking'])
dp.register_message_handler(cancel_booking_handler, commands=['cancel_booking'])
dp.register_message_handler(get_studio_handler, commands=['get_studio'])
dp.register_message_handler(get_client_bookings_handler, commands=['get_client_bookings'])
dp.register_message_handler(handlers.handle_help, commands=['help'])

if __name__ == '__main__':
    from aiogram import executor
    from booking.domain import handlers

    # Запуск бота
    executor.start_polling(dp, skip_updates=True)