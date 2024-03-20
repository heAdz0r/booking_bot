from aiogram import types
from .commands import CreateBookingCommand, CancelBookingCommand, GetStudioCommand, GetClientBookingsCommand
from .services.booking_service import BookingService
from .services.studio_service import StudioService
from .services.client_service import ClientService
from collections import defaultdict

from datetime import datetime, timedelta

async def handle_create_booking(message: types.Message, command: CreateBookingCommand, booking_service: BookingService):
    start_time = datetime.strptime(command.start_time, "%d.%m.%y %H:%M")
    duration = timedelta(hours=command.duration)
    end_time = start_time + duration

    booking = booking_service.create_booking(command.studio_id, command.client_id, start_time, end_time)
    await message.answer(f"Бронирование создано: {booking}")

async def handle_cancel_booking(message: types.Message, command: CancelBookingCommand, booking_service: BookingService):
    booking_service.cancel_booking(command.booking_id)
    await message.answer(f"Бронирование отменено: {command.booking_id}")

async def handle_get_studio(message: types.Message, command: GetStudioCommand, studio_service: StudioService):
    studio = studio_service.get_studio_by_id(command.studio_id)
    await message.answer(f"Информация о студии: {studio}")


async def handle_get_client_bookings(message: types.Message, command: GetClientBookingsCommand, client_service: ClientService):
    bookings = client_service.get_client_bookings(command.client_id)
    if bookings:
        # Группируем бронирования по дате
        booking_groups = defaultdict(list)
        for booking in bookings:
            date = booking.start_time.strftime("%d.%m.%y")
            booking_groups[date].append(booking)

        # Формируем таблицу бронирований
        table = []
        for date, bookings in booking_groups.items():
            table.append(f"Дата: {date}")
            for booking in bookings:
                start_time = booking.start_time.strftime("%H:%M")
                end_time = booking.end_time.strftime("%H:%M")
                table.append(f"  {start_time} - {end_time} (студия {booking.studio_id})")

        await message.answer("\n".join(table))
    else:
        await message.answer("У клиента нет бронирований.")

async def handle_help(message: types.Message):
    help_text = (
        "Список доступных команд:\n"
        "/create_booking - создать новое бронирование (формат: /create_booking студия клиент дата время продолжительность)\n"
        "/cancel_booking - отменить бронирование (формат: /cancel_booking id_бронирования)\n"
        "/get_studio - получить информацию о студии (формат: /get_studio id_студии)\n"
        "/get_client_bookings - получить список бронирований клиента (формат: /get_client_bookings id_клиента)\n"
    )
    await message.answer(help_text)