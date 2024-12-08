## Exploratory Data Analysis (EDA)
Applying various techniques to uncover trends and patterns. Based on the  regions—Benin, Sierra Leone, or Togo. Each notebook is for each regions.
### Solar Radiation Measurement Data
The data is extracted and aggregated from Solar Radiation Measurement Data. Each row in the data contains the values for solar radiation, air temperature, relative humidity, barometric pressure, precipitation, wind speed, and wind direction, cleaned and soiled radiance sensor (soiling measurement) and cleaning events.

### The structure of the data is as follows and their acronyms:
* **Timestamp (yyyy-mm-dd hh:mm)**: Date and time of each observation.
* **GHI (W/m²)**: Global Horizontal Irradiance, the total solar radiation received per square meter on a horizontal surface.
* **DNI (W/m²)**: Direct Normal Irradiance, the amount of solar radiation received per square meter on a surface perpendicular to the rays of the sun.
* **DHI (W/m²)**: Diffuse Horizontal Irradiance, solar radiation received per square meter on a horizontal surface that does not arrive on a direct path from the sun.
* **ModA (W/m²)**: Measurements from a module or sensor (A), similar to irradiance.
* **ModB (W/m²)**: Measurements from a module or sensor (B), similar to irradiance.
* **Tamb (°C)**: Ambient Temperature in degrees Celsius.
* **RH (%)**: Relative Humidity as a percentage of moisture in the air.
* **WS (m/s)**: Wind Speed in meters per second.
* **WSgust (m/s)**: Maximum Wind Gust Speed in meters per second.
* **WSstdev (m/s)**: Standard Deviation of Wind Speed, indicating variability.
* **WD (°N (to east))**: Wind Direction in degrees from north.
* **WDstdev**: Standard Deviation of Wind Direction, showing directional variability.
* **BP (hPa)**: Barometric Pressure in hectopascals.
* **Cleaning (1 or 0)**: Signifying whether cleaning (possibly of the modules or sensors) occurred.
* **Precipitation (mm/min)**: Precipitation rate measured in millimeters per minute.
* **TModA (°C)**: Temperature of Module A in degrees Celsius.
* **TModB(°C)**: Temperature of Module B in degrees Celsius.
* **Comments**: This column is designed for any additional notes.