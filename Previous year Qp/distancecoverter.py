class DistanceConverter:
    def __init__(self):
        self.kilometers = 0

    def get_distance(self):
        self.kilometers = float(input("Enter distance in kilometers: "))

    def print_distance(self):
        meters = self.kilometers * 1000
        print(f"Distance in meters: {meters} m")

# Example usage
d = DistanceConverter()
d.get_distance()
d.print_distance()
