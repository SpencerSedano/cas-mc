# ui_app/ui_components/ui_dido.py
from std_msgs.msg import String
from common_msgs.msg import DIDOCmd  # Adjust this to match your package name

class DIDOController:
    def __init__(self, ui, ros_node):
        self.ui = ui
        self.ros_node = ros_node

        # Initialize internal state
        self.ros_node.dido_cmd = {}

        # === Setup DO Buttons (48) ===
        for i in range(1, 49):
            do_name = f"DO{i}"
            self.ros_node.dido_cmd[do_name] = False
            button = getattr(self.ui, do_name)
            button.toggled.connect(
                lambda checked, name=do_name, btn=button: self.toggle_io(name, btn)
            )

        # === Setup DI Buttons (16) ===
        for i in range(1, 17):
            di_name = f"DI{i}"
            self.ros_node.dido_cmd[di_name] = False
            button = getattr(self.ui, di_name)
            button.toggled.connect(
                lambda checked, name=di_name, btn=button: self.toggle_io(name, btn)
            )

    def toggle_io(self, name, button):
        """Toggle DI/DO button, update internal state, and publish ROS message."""
        state = button.isChecked()
        self.ros_node.dido_cmd[name] = state

        msg = DIDOCmd()
        msg.name = name
        msg.state = "on" if state else "off"
        self.ros_node.dido_control_publisher.publish(msg)

        print(f"[UI] {name} state: {state}")

