from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, transport_id, capacity):
        self.transport_id = transport_id
        self.capacity = capacity
        self.booked_seats = set()

    def book_seat(self, seat_number):
        if not isinstance(seat_number, int):
            return f"Seat number must be integer."
        if seat_number < 1 or seat_number > self.capacity:
            return f"Seat number {seat_number} is not available."
        elif seat_number in self.booked_seats:
            return f"Seat {seat_number} is already booked."
        else:
            self.booked_seats.add(seat_number)
        return f"Seat {seat_number} successfully booked."

    def get_available_seats(self):
        return [seat for seat in range(1, self.capacity + 1) if seat not in self.booked_seats]

    @abstractmethod
    def get_info(self):
        pass


class Bus(Transport):
    def __init__(self, transport_id, capacity, route):
        super().__init__(transport_id, capacity)
        self.route = route

    def get_info(self):
        return f"Bus № {self.transport_id}, {self.capacity}  seats."


class Plane(Transport):
    def __init__(self, transport_id, capacity, model):
        super().__init__(transport_id, capacity)
        self.model = model

    def get_info(self):
        return f"Plane № {self.transport_id}, {self.capacity} seats."


class Train(Transport):
    def __init__(self, transport_id, capacity, cars):
        super().__init__(transport_id, capacity)
        self.cars = cars

    def get_info(self):
        return f"Train № {self.transport_id}, {self.capacity} seats."


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.name}, passport: {self.passport_number}"


class Booking:
    def __init__(self, passenger: Passenger, transport: Transport, seat_number):
        self.passenger = passenger
        self.transport = transport
        self.seat_number = seat_number

    def confirm(self):
        return self.transport.book_seat(self.seat_number)

    def __repr__(self):
        return f"{self.passenger} - Seat {self.seat_number} on {self.transport.get_info()}"


class BookingSystem:
    def __init__(self):
        self.transports = {}
        self.bookings = []

    def add_transport(self, transport: Transport):
        self.transports[transport.transport_id] = transport

    def make_booking(self, passenger: Passenger, transport_id, seat_number):
        transport = self.transports.get(transport_id)
        if not transport:
            return f"Transport {transport_id} does not exist."
        booking = Booking(passenger, transport, seat_number)
        confirmation = booking.confirm()
        if "successfully" in confirmation:
            self.bookings.append(booking)
        return confirmation

    def list_bookings(self):
        if not self.bookings:
            return "No bookings available."
        for booking in self.bookings:
            print(booking)


system = BookingSystem()

bus = Bus(123, 40, 32)
plane = Plane(789, 150, 'Boeing 737')
train = Train(456, 100, 10)
system.add_transport(bus)
system.add_transport(plane)
system.add_transport(train)

passenger = Passenger('Ivan Ivanov', 'MP6542697')
passenger2 = Passenger('Sidor Sidorov', 'MC6521632')
passenger3 = Passenger('Petr Petrov', 'JD8586245')

print(system.make_booking(passenger, 123, 21))
print(system.make_booking(passenger2, 123, 21))
print(system.make_booking(passenger2, 789, 100))
print(system.make_booking(passenger3, 456, 51))

print('Bookings:')
system.list_bookings()

# bus = Bus(123, 40, 32)
# plane = Plane(789, 150, 'Boeing 737')
# train = Train(456, 100, 10)
#
# print(bus.get_info())
# print(plane.get_info())
# print(train.get_info())
#

#
# print(passenger)
# print(passenger2)
# print(passenger3)
#
# booking = Booking(passenger, bus, 21)
# booking2 = Booking(passenger2, plane, 100)
# booking3 = Booking(passenger3, train, 51)
