# MG Project

## Table of Contents

- Installation
- Qt Designer
- Compilation
- Packages
- Components

## Installation

0. Install the required packages

    ```bash
    pip install PySide6
    ```

    ```bash
    pip install opencv-python
    ```

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

### After Changing Code

Remember to run these commands again.  

- Run them while in ~/cas-mc/ros2_ws/
- **BEFORE** src/

    ```bash
    colcon build
    ros2 run ui_app ui_node
    ```

**However**, if you close and open a new terminal, you will need to source again 'source install/setup.bash'.  
To solve this, follow these steps:

1. Open your terminal
2. Run this command (gedit is like notepad in Windows):

    ```bash
    gedit ~/.bashrc
    ```

3. Add this line at the end (remember to change it to YOUR path):

    ```bash
    source /home/spencer/cas-mc/ros2_ws/install/setup.bash
    ```

Now you will **NOT** need to source every time you open a terminal. Making it more convenient

### After Changing Qt Designer

Remember to run these commands.

1. Compile .ui (Qt Designer file) to .py

    ```bash
    pyside6-uic ui_magic_cube.ui -o ui_magic_cube.py
    ```

2. Run patch_icons.py. It will make sure all icons appear in the UI.

    ```bash
        python3 patch_icons.py ui_magic_cube.py
    ```

### About resources.qrc

This file contains:

```xml
    <RCC>
    <qresource prefix="/">
        <file>images/delta-logo.png</file>
        <file>controlArrows/cartesian/down.png</file>
        <file>controlArrows/cartesian/left.png</file>
        <file>controlArrows/cartesian/right.png</file>
        <file>controlArrows/cartesian/up.png</file>
        <file>controlArrows/cartesian/yawMinus.png</file>
        <file>controlArrows/cartesian/yawPlus.png</file>
        <file>controlArrows/lift.svg</file>
        <file>controlArrows/lower.svg</file>
        <file>icons/white/dimmer-switch.svg</file>
        <file>icons/white/home-simple-door.svg</file>
        <file>icons/white/multiple-pages.svg</file>
        <file>icons/white/page.svg</file>
        <file>icons/white/settings.svg</file>
        <file>icons/white/timeline-circle.svg</file>
        <file>icons/white/menu.svg</file>
    </qresource>
    </RCC>
```

If more icons are needed later, you need to include them here and compile it.

```bash
pyside6-rcc resources.qrc -o resources_rc.py
```

## Components

- ui_motor.py
- ui_forklift.py
- ui_cabinets.py
- ui_dido.py
- ui_gripper.py
- ui_limit.py
- ui_pages.py
- ui_style.py
- ui_vision.py
