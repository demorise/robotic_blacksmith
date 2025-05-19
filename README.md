# Robotic Blacksmith
## Installation (Tested on ROS 2 Humble)
The repo has been designed as a colcon workspace to simplify installation. Also note that the root of the workspace houses the sensor simulation Python script (`sensor.py`). To install, simply clone the repo into any directory of your choice, build it and source as follows:
```bash
git clone https://github.com/demorise/robotic_blacksmith
cd robotic_blacksmith
colcon build --symlink-install
source install/setup.bash
```

## Usage
Open four terminals in the workspace root directory and source the workspace (`source install/setup.bash`) in each one if the sourcing command is not already part of your `.bashrc`. Run the following commands in each terminal in the following order:

1. Start the simulator for the load cells
```bash
python3 sensor.py
```

2. Start the ros2 server for the load cells
```bash
ros2 run load_cell_filter load_cell_server
```

3. Start the ros2 node that makes requets to the server and publishes on topics `load_cell1_data` and `load_cell2_data`
```bash
ros2 run load_cell_filter load_cell_client
```

4. Inspect the load cell topics with either of the following commands:
```bash
ros2 topic echo /load_cell2_data
ros2 topic echo /load_cell1_data
```