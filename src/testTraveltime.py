from typing import Annotated

def calculate_travel_time(
    distance: Annotated[int, "Distance in kilometers"],
    speed: Annotated[int, "Speed in km/h"],
) -> str:
    travel_time = distance / speed
    return f"At a speed of {speed} km/h, it will take approximately {travel_time:.2f} hours to travel {distance} kilometers."



if __name__ == "__main__":
    userInput = int(input("Enter the Distance in kilometers: "))
    speedInput = int(input("Enter the Speed in km/h: "))
    print(calculate_travel_time(userInput, speedInput))
