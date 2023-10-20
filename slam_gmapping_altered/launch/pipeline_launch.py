from launch import LaunchDescription,launch_description_sources
from launch_ros.actions import Node

from launch.substitutions import EnvironmentVariable
import launch.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='true')

    return LaunchDescription([

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_0',
            arguments = ["0", "0", "0", "0", "0", "0", "odom", "base_link"]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_1',
            arguments = ["0", "0", "0", "0", "0", "0", "odom", "base_footprint"]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_2',
            arguments = ["0", "0", "0", "0", "0", "1", "odom", "map"]
        ),
        Node(
            package='slam_gmapping_altered',
            executable='server',
            name='slam_gmapping_node'
        ),

        ])
