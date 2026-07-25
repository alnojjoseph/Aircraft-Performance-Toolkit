import numpy as np
import matplotlib.pyplot as plt
import csv
from aircraft import Aircraft

print('Aircraft Toolkit initialized')

fleet = []

# Aircraft Inputs using CSV file

with open('aircraft_data.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        mass = float(row['mass'])
        wing_surface_area = float(row['wing_surface_area'])
        lift_coefficient_max = float(row['lift_coefficient_max'])
        current_aircraft = Aircraft(name, mass, wing_surface_area, lift_coefficient_max)
        fleet.append(current_aircraft)

print(f'{len(fleet)} Aircraft data loaded successfully')
print()

while True:
    mode = int(input('1. Would you like to analyse 1 Aircraft, OR 2. Multiple Aircrafts at the same time (1/2) '))
    print()
    if mode == 1:
        while True:
        
            while True:
                chosen_aircraft = input('Which Aircraft would you like to Analyse: ')
                selected_aircraft = None
                for aircraft in fleet:
                    if aircraft.name == chosen_aircraft:
                        selected_aircraft = aircraft
                        break
                if selected_aircraft is not None:
                    break
                print('\u26A0 Aircraft not found - Try again by entering the correct spelling ')
            print()
            print(selected_aircraft.name)
            density = float(input('Enter the air density: '))
            velocity = float(input('Enter the current velocity of the Aircraft: '))
            lift_coefficient = float(input('Enter the lift coefficient: '))
            drag_coefficient = float(input('Enter the drag coefficient: '))
            thrust = float(input('Enter the current Thrust value in N: '))

            print()
            print(f'The Lift force of {selected_aircraft.name} is {selected_aircraft.calculate_lift(density, velocity, lift_coefficient):.2f} N ')
            print()
            if selected_aircraft.calculate_lift(density, velocity, lift_coefficient) >= selected_aircraft.weight:
                print('Since the Lift generated is greater or equal to the weight of the aircraft, the aircraft can maintain a level flight.')
            else:
                print('\u26A0 Warning: LIFT GENERATED NOT SUFFICIENT-> Aircraft Descending')
                print('Increase Velocity or Lift coefficient immediately to maintain Level flight.')
            print()
            print(f'The Drag force of {selected_aircraft.name} is {selected_aircraft.calculate_drag(density, velocity, drag_coefficient):.2f} N ')
            print()
            print(f'The Stall velocity of {selected_aircraft.name} is {selected_aircraft.calculate_v_stall(density):.2f} m/s ')
            print()
            if selected_aircraft.calculate_v_stall(density) > velocity:
                print('\u26A0 Current airspeed is below stall speed.')
                print('The aircraft cannot maintain steady flight.')
            print()
            print(f'The Wing loading of {selected_aircraft.name} is {selected_aircraft.calculate_wing_loading():.2f} N/m^2 ')
            print()
            print(f'The Thrust-to-Weight ratio of {selected_aircraft.name} is {selected_aircraft.calculate_thrust_weight_ratio(thrust):.2f} ')
            if selected_aircraft.calculate_thrust_weight_ratio(thrust) < 0.2:
                print(' \u26A0 Warning: Very low thrust-to-weight ratio. Aircraft may have poor climb and acceleration performance.')
            print()
            question1 = input('Do you want to create a Graph for this aircraft- Y/N ')
            print()
            if question1.lower() =='y':
                velocity = np.linspace(20,300,25)
                lift_values = selected_aircraft.calculate_lift(density, velocity, lift_coefficient)
                plt.plot(velocity, lift_values, label ='Lift Force')
                drag_values = selected_aircraft.calculate_drag(density, velocity, drag_coefficient)
                plt.plot(velocity, drag_values, label ='Drag Force')
                plt.legend()
                plt.xlabel('Velocity (m/s)')
                plt.ylabel('Lift/Drag Force in N')
                plt.title(f'Lift/Drag vs Velocity - {selected_aircraft.name}')
                plt.grid(True)
                plt.show()

            again = input('Do you want to Analyse another Aircraft (Y/N): ')
            print()
            if again.lower() !='y':
                break
        
   
    elif mode == 2:
        while True:
            comparison_fleet = []
            num_aircraft = int(input('How many Aircraft would you like to Analyse : '))
            print()
        
            for i in range(num_aircraft):
                while True:
                    chosen_aircraft = input(f'Which Aircraft do you want to choose as {i+1} : ')
                    selected_aircraft = None
                    for aircraft in fleet:
                        if aircraft.name == chosen_aircraft:
                            selected_aircraft = aircraft
                            break
                    if selected_aircraft is not None:
                        break   
                    print('\u26A0 Aircraft not found - Try again by entering the correct spelling ')
                print()

                print(selected_aircraft.name)
                density = float(input('Enter the air density: '))
                velocity = float(input('Enter the current velocity of the Aircraft: '))
                lift_coefficient = float(input('Enter the lift coefficient: '))
                drag_coefficient = float(input('Enter the drag coefficient: '))
                thrust = float(input('Enter the current Thrust value in N: '))
                print()

                entry = {
                    'aircraft': selected_aircraft,
                    'density': density,
                    'velocity': velocity,
                    'lift_coefficient': lift_coefficient,
                    'drag_coefficient': drag_coefficient,
                    'thrust': thrust
                    }
                comparison_fleet.append(entry)

            for entry in comparison_fleet:
                aircraft = entry['aircraft']
                density = entry['density']
                velocity = entry['velocity']
                lift_coefficient = entry['lift_coefficient']
                drag_coefficient = entry['drag_coefficient']
                thrust = entry['thrust']

                lift_force = aircraft.calculate_lift(density, velocity, lift_coefficient)

                print(f'The Lift force of {aircraft.name} is {lift_force:.2f} N ')
                print()
                if lift_force >= aircraft.weight:
                    print('Since the Lift generated is greater or equal to the weight of the aircraft, the aircraft can maintain a level flight.')
                else:
                    print('\u26A0 Warning: LIFT GENERATED NOT SUFFICIENT-> Aircraft Descending')
                    print('Increase Velocity or Lift coefficient immediately to maintain Level flight.')
                print()

                drag_force = aircraft.calculate_drag(density, velocity, drag_coefficient)
                
                print(f'The Drag force of {aircraft.name} is {drag_force:.2f} N ')
                print()

                v_stall = aircraft.calculate_v_stall(density)

                print(f'The Stall velocity of {aircraft.name} is {v_stall:.2f} m/s ')
                
                if v_stall > velocity:
                    print()
                    print('\u26A0 Current airspeed is below stall speed.')
                    print('The aircraft cannot maintain steady flight.')
                print()

                wing_loading = aircraft.calculate_wing_loading()

                print(f'The Wing loading of {aircraft.name} is {wing_loading:.2f} N/m^2 ')
                print()

                thrust_weight_ratio = aircraft.calculate_thrust_weight_ratio(thrust)

                print(f'The Thrust-to-Weight ratio of {aircraft.name} is {thrust_weight_ratio:.2f} ')
                if thrust_weight_ratio < 0.2:
                    print(' \u26A0 Warning: Very low thrust-to-weight ratio. Aircraft may have poor climb and acceleration performance.')
                print()

            graph_question = input('Do you want to compare using graphs (Y/N) : ')
            print()

            if graph_question.lower() == 'y':
                velocity_range = np.linspace(20,300,25)
                for entry in comparison_fleet:
                    aircraft = entry['aircraft']
                    lift_values = aircraft.calculate_lift(entry['density'], velocity_range, entry['lift_coefficient'])
                    plt.plot(velocity_range,lift_values,label = f'Lift - {aircraft.name}')
                    drag_values = aircraft.calculate_drag(entry['density'], velocity_range, entry['drag_coefficient'])
                    plt.plot(velocity_range,drag_values,label = f'Drag - {aircraft.name}')
                plt.legend()
                plt.xlabel('Velocity (m/s)')
                plt.ylabel('Lift/Drag Force in N')
                plt.title(f'Lift/Drag vs Velocity')
                plt.grid(True)
                plt.show()
            
            question2 = input('Do you want to run another comparison (Y/N): ')
            print()

            if question2.lower() != 'y':
                break

    main = input('Do you want to go back to the main menu (Y/N):')
    print()
    if main.lower() !='y':
        break


