# Raspberry Pi Environmental Monitoring and Control System

## Project Overview
This project implements an embedded environmental monitoring and control system using a Raspberry Pi and the Raphael Kit. It integrates multiple sensors to measure temperature, humidity, and light intensity, displays real-time data, and controls actuators based on sensor thresholds. Additionally, the system logs data for later analysis and visualization.

---

## Features and Implementation

### Sensor Integration
- **Temperature and Humidity**: Using the DHT11 or DHT22 sensor connected to the Raspberry Pi GPIO pins, the system reads environmental temperature and humidity data.
- **Light Intensity**: A photoresistor (LDR) is connected and read via an ADC or GPIO interface to measure ambient light levels.

### Data Display
- Sensor readings are displayed in real-time on an LCD or OLED screen connected through the Raphael Kit display module, providing instant visual feedback.

### Actuator Control
- Based on predefined threshold values for temperature and light, the system controls an actuator such as a fan or LED.
- The control logic automatically activates or deactivates the actuator to maintain desired environmental conditions.

### Data Logging and Visualization
- Sensor data with timestamps are recorded in a CSV log file.
- A Python script enables basic visualization of the logged data, facilitating trend analysis over time.

---

## Hardware Components
- Raspberry Pi (with GPIO capabilities)
- Raphael Kit (GPIO breakout board and display module)
- DHT11 or DHT22 Temperature & Humidity Sensor
- Photoresistor (LDR) or similar light sensor
- Actuator (fan or LED)
- Necessary resistors and wiring

---

## Software Requirements
- Python 3.x
- Libraries:
  - `Adafruit_DHT` (for temperature and humidity sensor)
  - `RPi.GPIO` or equivalent GPIO library
  - `matplotlib` (for data visualization)
  - Additional libraries as per display module requirements

---

## Setup and Usage

1. **Hardware Wiring**: Connect sensors and actuators to the Raspberry Pi GPIO pins as per schematic.
2. **Software Installation**: Install required Python packages using pip.
3. **Running the System**:
   - Execute the main Python script to start reading sensors, displaying data, and controlling actuators.
   - Data logging runs continuously, storing readings to a CSV file.
4. **Data Visualization**: Run the visualization script to generate plots from the logged data.

---

## Project Structure
- `sensor_readings.py` — Reads and processes sensor data.
- `display.py` — Handles real-time data display on the screen.
- `actuator_control.py` — Contains logic to control actuators based on sensor thresholds.
- `data_logger.py` — Logs sensor readings to file.
- `visualize.py` — Generates plots from logged data.

---

## Example Output
- Real-time temperature, humidity, and light levels displayed on the LCD/OLED.
- Actuator (fan or LED) turning on/off automatically when thresholds are met.
- CSV files containing timestamped sensor logs.
- Graphical plots showing environmental trends over time.

---

## Contribution and License
Feel free to contribute improvements or report issues. This project is for educational and personal use.

---

*Developed as a practical embedded systems project leveraging Raspberry Pi and the Raphael Kit.*

## 📅 Day-by-Day Progress Log

### Day 1 – Initial Setup
- **Hardware**: Raspberry Pi setup, SSH connection established.
- **Software**: Created virtual environment, basic directory navigation commands documented.
- **Notes**: Linked Pi to GitHub, tested initial `blink.py` file push.

---

### Day 2 – Temperature & Humidity Sensor Integration
- **Hardware**: Connected DHT11/DHT22 sensor to Raspberry Pi.
- **Software**:  
  1. Created Python script to read data from the sensor.  
  2. Installed libraries in virtual environment:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install adafruit-circuitpython-dht
     pip install RPi.GPIO
     ```
  3. Printed readings to terminal.  
- **Notes**: Committed and pushed updated code & README.

---

### Day X – [Title of Activity]
- **Hardware**: [Describe hardware changes]
- **Software**: [Describe software/code updates]
- **Notes**: [Any extra notes or issues encountered]

---

