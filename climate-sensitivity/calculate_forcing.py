import math
import argparse

RADIATIVE_FORCING_CONSTANT: float = 5.35


def parse_args():

    parser = argparse.ArgumentParser(description="Calculate equlibrium climate change.")

    parser.add_argument('-d', '--delta', required=True, type=float, help='Expected change in CO2 parts per million')
    parser.add_argument('-s', '--sensitivity', required=False, default=3.0, type=float, help='The Equilibrium Climate Sensitivity')
    parser.add_argument('-p', '--ppm', required=False, default=412, type=float, help='The current atmospheric parts per million')

    return parser.parse_args()


def calculate_feedback_sensitivity_lambda(sensitivity: float):
    """[summary]
    Calculates the appropriate climate feedback lambda based on the given equilibrium climate sensitivity to a doubling of CO2

    Args:
        sensitivity (float): [The equilibrium climate sensitivity in degrees celsius to a doubling of CO2]
    """
    doubled_atmospheric_co2 = 2

    return sensitivity / (RADIATIVE_FORCING_CONSTANT * math.log(doubled_atmospheric_co2))


def calculate_forcing(current_atmospheric_co2_ppm: float, co2_delta_ppm: float, feedback_sensitivity_lambda: float) -> float:

    return feedback_sensitivity_lambda * RADIATIVE_FORCING_CONSTANT * math.log(1 + co2_delta_ppm / current_atmospheric_co2_ppm)


if __name__ == "__main__":

    args = parse_args()

    current_atmospheric_co2_ppm = args.ppm
    co2_delta_ppm = args.delta
    sensitivity = args.sensitivity

    feedback_sensitivity_lambda = calculate_feedback_sensitivity_lambda(sensitivity)
    forcing = calculate_forcing(current_atmospheric_co2_ppm, co2_delta_ppm, feedback_sensitivity_lambda)

    print(f"An increase of {co2_delta_ppm} PPM from the current {current_atmospheric_co2_ppm} PPM with an ECS of {sensitivity} degrees K will increase global mean temperatures by {forcing} degrees K")
