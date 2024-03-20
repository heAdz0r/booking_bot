from aiogram import types
from .commands import CreateBookingCommand, CancelBookingCommand, GetStudioCommand, GetClientBookingsCommand
from .services.booking_service import BookingService
from .services.studio_service import StudioService
from .services.client_service import ClientService

async def handle_create_booking(message: types.Message, command: CreateBookingCommand, booking_service: BookingService):
    booking = booking_service.create_booking(command.studio_id, command.client_id, command.start_time, command.end_time)
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
        await message.answer(f"Бронирования клиента: {bookings}")
    else:
        await message.answer("У клиента нет бронирований.")