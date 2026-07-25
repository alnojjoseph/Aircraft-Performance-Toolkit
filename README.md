# Aircraft Performance Analysis Toolkit

A Python toolkit for analyzing and comparing aircraft performance using core aerodynamic principles — lift, drag, stall speed, wing loading, and thrust-to-weight ratio. Built as a hands-on project to apply aerospace engineering theory through clean, object-oriented Python.

## Features

- **Object-oriented design** — an `Aircraft` class encapsulates each aircraft's properties (mass, wing area, max lift coefficient) and exposes its own performance calculations as methods.
- **Data-driven fleet loading** — aircraft specifications are read from a CSV file and used to build a fleet of `Aircraft` objects dynamically, rather than hardcoding values.
- **Two analysis modes:**
  1. **Single Aircraft Analysis** — deep-dive into one aircraft at a given flight condition, with automatic pass/fail interpretation (e.g. insufficient lift for level flight, airspeed below stall speed, low thrust-to-weight ratio).
  2. **Multi-Aircraft Comparison** — compare any number of aircraft side by side, with full performance breakdowns for each and overlaid Matplotlib visualizations.
- **Vectorized performance curves** — NumPy is used to compute lift and drag across a full range of velocities in a single operation, powering smooth plotted curves.
- **Input validation** — aircraft selection retries on invalid names instead of crashing, with clear feedback to the user.

## Tech Stack

- Python 3
- NumPy
- Matplotlib
- `csv` (Python standard library)

## Project Structure

```
aircraft-performance-toolkit/
├── main.py              # Interactive program: mode selection, user input, analysis flow
├── aircraft.py           # Aircraft class: core performance equations as methods
├── aircraft_data.csv     # Aircraft specifications dataset
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/alnojjoseph/Aircraft-Performance-Toolkit.git
   cd aircraft-performance-toolkit
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

 ### Usage

Run the program:

```
python main.py
```

You'll be prompted to:

1. Choose between single-aircraft analysis or multi-aircraft comparison.
2. Select aircraft by name from the loaded dataset.
3. Enter flight conditions — air density, velocity, lift/drag coefficients, and thrust.
4. View calculated results, including automatic warnings if the aircraft can't sustain level flight, is below stall speed, or has a poor thrust-to-weight ratio.
5. Optionally generate a plot of lift and drag versus velocity for one or more aircraft.

## Equations Implemented

| Quantity | Formula |
|---|---|
| Lift | L = 0.5 · ρ · V² · S · C_L |
| Drag | D = 0.5 · ρ · V² · S · C_D |
| Stall Speed | V_stall = √(2W / (ρ · S · C_L,max)) |
| Wing Loading | W / S |
| Thrust-to-Weight Ratio | T / W |

## A Note on the Data

Aircraft specifications in `aircraft_data.csv` are a mix of verified published figures (e.g. Cessna 172, Airbus A320, Boeing 737-800) and reasonable placeholder estimates for aircraft where exact public data wasn't independently confirmed. This is a personal learning project, not a certified engineering reference.

## Roadmap

- [ ] Side-by-side comparison table view (in addition to stacked results)
- [ ] Additional plot types — drag polar (C_L vs C_D), lift-to-drag ratio vs velocity
- [ ] Automatic unit conversion on input
- [ ] More robust input validation for malformed numeric entries
- [ ] Splitting equations further as the project grows toward CAD/CFD integration (PyAnsys, pycatia)

## Author

**Alno John Joseph** — aerospace engineering graduate learning Python as an engineering tool, alongside CATIA and ANSYS, rather than as an end in itself.
