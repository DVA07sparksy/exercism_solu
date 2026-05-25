EXPECTED_BAKE_TIME= 40

PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """To calculate the remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """To calculate the preparation time."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """To calculate the elapsed time."""
    ptm = preparation_time_in_minutes(number_of_layers)
    btr= bake_time_remaining(elapsed_bake_time)
    cooking_time=EXPECTED_BAKE_TIME-btr
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return ptm + cooking_time

    