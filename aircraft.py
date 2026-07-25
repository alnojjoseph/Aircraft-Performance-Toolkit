import numpy as np

class Aircraft:
    
    gravity = 9.81  # m/(s^2)
    
    def __init__(self, name, mass, wing_surface_area, lift_coefficient_max):
        
        self.name = name
        self.mass = mass                                                                       # Defining Class with init
        self.wing_surface_area = wing_surface_area
        self.lift_coefficient_max = lift_coefficient_max
        self.weight = self.mass * self.gravity

    def calculate_lift(self, density, velocity, lift_coefficient):
        lift_force = 0.5 * density * velocity **2 * self.wing_surface_area * lift_coefficient   # Lift Function
        return lift_force
    
    def calculate_drag(self, density, velocity, drag_coefficient):
        drag_force = 0.5 * density * velocity**2 * self.wing_surface_area * drag_coefficient    # Drag Function
        return drag_force
    
    def calculate_v_stall(self, density):
        v_stall = np.sqrt((2 * self.weight)/(density * self.wing_surface_area * self.lift_coefficient_max))    # Stall velocity Function
        return v_stall
    
    def calculate_wing_loading(self):
        wing_loading = self.weight / self.wing_surface_area                                      # Wing Loading Function
        return wing_loading
    
    def calculate_thrust_weight_ratio(self, thrust):
        thrust_weight_ratio = thrust / self.weight                                               # Thrust-Weight Ratio Function 
        return thrust_weight_ratio