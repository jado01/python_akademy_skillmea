class Device:
    def __init__(self, name):
        self.name = name
        self.__is_on = False
    
    @property
    def is_on(self):
        return self.__is_on
    

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def __str__(self):
        if self.is_on:
            return f"{self.name}: ON"
        return f"{self.name}: OFF"
    

class SmartLight(Device):
    def __init__(self, name, brightness):
        super().__init__(name)
        self.brightness = brightness

    @property
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        self.__brightness = value
    
    def change_brightness(self, amount):
        self.brightness += amount

    def __str__(self):
        if self.is_on:
            return f"{self.name}: ON, brightness: {self.brightness}%"
        return f"{self.name}: OFF, brightness: {self.brightness}%"


class Thermostat(Device):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature
    
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        if not 5 <= value <= 35:
            raise ValueError("Value must be between 5 and 35")
        self.__temperature = value

    def __str__(self):
        if self.is_on:
            return f"{self.name}: ON, temperature: {self.temperature} °C"
        return f"{self.name}: OFF, temperature: {self.temperature} °C"


class Room:
    def __init__(self, name):
        self.name = name
        self.devices = []

    @property
    def device_count(self):
        return len(self.devices)
    
    def add_device(self, device):
        if not isinstance(device, Device):
            raise TypeError("Expected a Device object")
        if device in self.devices:
            raise ValueError("Device is already in the room")
        self.devices.append(device)
    
    def remove_device(self, device):
        if not isinstance(device, Device):
            raise TypeError("Expected a Device object")
        if device not in self.devices:
            raise ValueError("Device is not in the room")
        self.devices.remove(device)
    
    def list_devices(self):
        if not self.devices:
            return f"{self.name} has no devices."
        lines = [f"{self.name} has these devices:"]
        for device in self.devices:
            lines.append(f"- {device}")
        return "\n".join(lines)
    
    def turn_on_all(self):
        for device in self.devices:
            device.turn_on()
    
    def turn_off_all(self):
        for device in self.devices:
            device.turn_off()
    
    def find_device(self, name):
        for device in self.devices:
            if device.name == name:
                return device
        return None
    
    @property
    def active_device_count(self):
        count = 0
        
        for device in self.devices:
            if device.is_on:
                count += 1
        
        return count
    
    def __str__(self):
        return f"{self.name}: {self.device_count} device(s)"
    

def main():
    room = Room("Living room")
    plug = Device("Plug")
    tv = Device("TV")
    lamp = SmartLight("Lamp", 80)
    thermostat = Thermostat("Thermostat", 22)

    for device in (plug, tv, lamp, thermostat):
        room.add_device(device)

    print(room)
    print(room.list_devices())
    print(room.active_device_count)

    found_device = room.find_device("Lamp")

    if found_device is not None:
        found_device.turn_on()
        found_device.change_brightness(10)

    print(room.list_devices())
    print(room.active_device_count)

    room.turn_on_all()
    print(room.list_devices())
    print(room.active_device_count)

    room.turn_off_all()
    print(room.list_devices())
    print(room.active_device_count)


if __name__ == "__main__":
    main()