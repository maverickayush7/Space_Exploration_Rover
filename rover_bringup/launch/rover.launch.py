import os
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    rover_bringup_shared_dir = get_package_share_directory("rover_bringup")
    rover_motor_controller_shared_dir = get_package_share_directory(
        "rover_motor_controller_cpp"
    )
    rover_teleop_shared_dir = get_package_share_directory("rover_teleop")

    stdout_linebuf_envvar = SetEnvironmentVariable(
        "RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED", "1"
    )

    #
    # LAUNCHES
    #

    urg_node_action_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(rover_bringup_shared_dir, "launch", "urg_node.launch.py")
        ),
        launch_arguments={
            "config_filepath": os.path.join(
                rover_bringup_shared_dir, "config", "urg_node_serial.yaml"
            )
        }.items(),
    )

    teleop_twist_joy_action_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(rover_teleop_shared_dir, "launch", "joy_teleop.launch.py")
        )
    )

    rover_motor_controller_action_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                rover_motor_controller_shared_dir, "launch", "motor_controller.launch.py"
            )
        )
    )

    ld = LaunchDescription()

    ld.add_action(stdout_linebuf_envvar)

    ld.add_action(urg_node_action_cmd)
    ld.add_action(teleop_twist_joy_action_cmd)
    ld.add_action(rover_motor_controller_action_cmd)

    return ld
