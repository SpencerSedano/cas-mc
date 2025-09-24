# MG Project

## Table of Contents

- Installation
- Qt Designer
- Compilation
- Packages
- Components

## Installation

1. Go to ros2_ws folder

    ```bash
    cd ~/ros2_ws
    ```

2. Run these 3 commands

    ```bash
    colcon build
    source install/setup.bash
    ros2 run ui_app ui_node
    ```

## Qt Designer

The project is using Pyside6 which contains Qt Designer.

To open Qt Designer:

- In a terminal:

    ```bash
    pyside6-designer
    ```

## Compilation

After making any changes to the code. Remember to run these commands again.  

- Run them while in ~/cas-mc/ros2_ws/
- **BEFORE** src/

    ```bash
    colcon build
    ros2 run ui_app ui_node
    ```

**However**, if you close and open a new terminal, you will need to source again 'source install/setup.bash'. To solve this, follow these steps:

1. Open your terminal
2. Run this command (gedit is like notepad in Windows):

    ```bash
    gedit ~/.bashrc
    ```

3. Add this line in the end (remember to change it to your path):

    ```bash
    source /home/spencer/cas-mc/ros2_ws/install/setup.bash
    ```

Now you will **not** need to source every time you open a terminal.

## Packages


## Components
