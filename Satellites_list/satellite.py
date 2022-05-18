"""
Defined class satellite
"""
class satellite:
    def __init__(self, name, mass, reference_area, radiation_pressure_coefficient, occulting_bodies, initial_states):
        self.name = name
        self.mass = mass
        self.reference_area = reference_area
        self.radiation_pressure_coefficient = radiation_pressure_coefficient
        self.occulting_bodies = occulting_bodies
        self.initial_states = initial_states