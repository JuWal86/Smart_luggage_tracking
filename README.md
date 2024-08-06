# Luggage Tracking System

This repository contains a luggage tracking system that simulates the movement of luggage pieces and tracks their status and location using MQTT. The system uses Docker to manage its services, which include Mosquitto (MQTT broker), Telegraf, InfluxDB, Grafana, and Node-RED.

## How to Start the Project

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/Smart_luggage_tracking.git
    ```

2. **Unzip the Data Directories**

    ```sh
    unzip influxdb_data.zip -d influxdb_data
    unzip nodered_data.zip -d nodered_data
    ```

3. **Configure Environment Variables**

    Ensure the `.env` file contains the necessary configuration for your environment. You can customize the settings as needed.

4. **Build and Start the Docker Containers**

    ```sh
    docker-compose up --build
    ```

    This command will build and start all the services defined in the `docker-compose.yml` file.

5. **Access the Services**

    - **Grafana**: http://localhost:3000 (Default login: `admin` / `admin`)
    - **Node-RED**: http://localhost:1880 
    - **InfluxDB**: http://localhost:8086 (Default login: `admin` / `PASSWORD`)
    - **MQTT Broker (Mosquitto)**: mqtt://localhost:1883

## Python Script for Luggage Simulation

The Python script `luggage_simulation.py` is responsible for generating and updating luggage data and publishing it to the MQTT broker.

### Script Overview

- Generates 1000 luggage pieces with random attributes.
- Publishes updates to random luggage locations every 5 seconds to the MQTT topic `luggage/tracking`.

