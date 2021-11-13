import sys
import math

def calculate_forcing(co2_ppm_increase : float) -> float:

    CURRENT_ATMOSPHERIC_CO2 : float = 412.37
    RADIATIVE_FORCING_CONSTANT: float = 5.35
    FEEDBACK_SENSITIVITY_LAMBDA: float = 0.81

    return FEEDBACK_SENSITIVITY_LAMBDA * RADIATIVE_FORCING_CONSTANT * math.log((CURRENT_ATMOSPHERIC_CO2 + co2_ppm_increase) / CURRENT_ATMOSPHERIC_CO2)

if(__name__ == "__main__"):
    co2_ppm_increase = float(sys.argv[1])
    forcing = calculate_forcing(co2_ppm_increase)

    print(f"An increase of {co2_ppm_increase} parts per million will increase global mean temperatures by {forcing} degrees C")