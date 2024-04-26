from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),
        Node(
            package='my_package',
            executable='my_node',
            name='circulo',
            prefix = 'gnome-terminal --',
            output='screen'
        )
    ])