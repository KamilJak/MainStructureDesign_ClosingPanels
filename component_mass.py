
class Component:
    def __init__(self, mass: float, number: int) -> None:
        self.mass = float(mass)
        self.n = int(number)
        self.instances = 0

    def get(self, number: int) -> float:
        if self.instances == self.n:
            raise ValueError("All instances already used")
        elif self.instances + number > self.n:
            raise ValueError("Number is greater than instances remaining")
        else:
            self.instances += number
            return self.mass * number

components: dict[str, Component] = {
    'sun sensor': Component(0.375, 4),
    'star sensor': Component(0.106, 3),
    'gyroscope': Component(1.4, 2),
    'reaction wheel': Component(3.2, 4),
    'rcs thruster': Component(0.012, 12),
    'HRSC camera': Component(11.8, 1),
    'HRSC electronics': Component(7.2, 1),
    'UV spectrometer': Component(14.5, 1),
    'UV electronics': Component(7, 1),
    'magnetometer sensor': Component(0.2, 2),
    'magnetometer electronics': Component(1.2, 1),
    'a-BELA': Component(13, 1),
    'main thruster': Component(1.9, 1),
    'propellant': Component(1207, 1),
    'propellant tank': Component(52.5, 1),
    'radiator': Component(2.53, 1),
    'louver': Component(1, 1),
    'solar panel': Component(5.2, 2),
    'battery': Component(18, 1),
    'PCDS': Component(4.14, 1),
    'cables': Component(0.9, 1),
}

def gc(name, number=1):
    return [components.get(name), number]

