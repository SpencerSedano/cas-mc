# ui_app/ui_components/ui_dido.py
from std_msgs.msg import String

class DIDOController:
    def __init__(self, ui, ros_node):
        self.ui = ui
        self.ros_node = ros_node

        # Initialize all DO states in ROS node
        self.ros_node.dido_cmd = {f"DO{i}": False for i in range(1, 47)}

        # Connect all DO buttons dynamically
        for i in range(1, 49):
            do_name = f"DO{i}"
            button = getattr(self.ui, do_name)  # Get button from UI by name
            button.toggled.connect(
                lambda checked, name=do_name, btn=button: self.toggle_do(name, btn)
            )

    def toggle_do(self, do_name, button):
        """Toggle the DO button, update internal state, and publish ROS message."""
        self.ros_node.dido_cmd[do_name] = button.isChecked()

        msg = String()
        msg.data = "on" if button.isChecked() else "off"
        self.ros_node.dido_control_publisher.publish(msg)

        print(f"[UI] {do_name} state: {self.ros_node.dido_cmd[do_name]}")
