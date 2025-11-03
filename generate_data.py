import pandas as pd
import numpy as np

COMPONENTS = {
    "PUMP-A01": {"temp_mean": 80, "temp_std": 2, "vib_mean": 0.5, "vib_std": 0.1},
    "PUMP-B02": {"temp_mean": 75, "temp_std": 1, "vib_mean": 0.4, "vib_std": 0.05},
    "TURBINE-G01": {"temp_mean": 500, "temp_std": 15, "vib_mean": 1.2, "vib_std": 0.2},
}
N_ROWS = 1000
START_DATE = "2024-01-01 00:00:00"

print("Generating mock sensor data...")
final_df = pd.DataFrame()
date_rng = pd.date_range(start=START_DATE, periods=N_ROWS, freq='h')

for comp_id, specs in COMPONENTS.items():
    temp_data = np.random.normal(loc=specs["temp_mean"], scale=specs["temp_std"], size=N_ROWS)
    vib_data = np.random.normal(loc=specs["vib_mean"], scale=specs["vib_std"], size=N_ROWS)
    
    df = pd.DataFrame({
        "timestamp": date_rng,
        "component_id": comp_id,
        "temperature_C": temp_data,
        "vibration_mm_s": vib_data,
        "pressure_kPa": np.random.normal(loc=1500, scale=50, size=N_ROWS)
    })
    
    if comp_id == "PUMP-A01":
        degradation = np.linspace(0, 5, N_ROWS)
        df["temperature_C"] += degradation

    final_df = pd.concat([final_df, df])

output_file = "sensor_data.csv"
final_df.to_csv(output_file, index=False)
print(f"Successfully generated {len(final_df)} rows and saved to '{output_file}'")