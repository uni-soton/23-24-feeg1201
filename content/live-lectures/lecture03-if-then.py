def is_boiling_water(temperature):
    """Given `temperature` in degree Celsius, return True
    if the temperature is equal to or greather than
    100 deg C, return False otherwise.
    """
    if temperature >= 100:
        return True
    else:
        return False


def temperature_colour(T):
    """Given a temperature 'T' in degree Celsius, return a string
    defining the colour of a warning sign:
    green is no danger, orange is in between, red is dangerous.
    """
    # feels warm if touched
    if T < 45:
        colour = "green"
    # feels painful if touched
    elif T < 65:
        colour = "orange"
    else:  # T must be equal to or greater than 65
        # causes burns if touched
        colour = "red"

    return colour
