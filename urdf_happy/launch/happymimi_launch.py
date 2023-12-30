import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Declare arguments
    model = LaunchConfiguration('model', default=os.path.join(get_package_share_directory('urdf_happy'), 'robots', 'vhappymimi.urdf.xacro'))
    paused = LaunchConfiguration('paused', default='false')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    gui = LaunchConfiguration('gui', default='true')
    headless = LaunchConfiguration('headless', default='false')
    debug = LaunchConfiguration('debug', default='false')

    # Include Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('gazebo_ros'), 'launch'), '/empty_world.launch.py']),
        launch_arguments={'world_name': os.path.join(get_package_share_directory('megarover_samples'), 'worlds', 'vmegarover_sample.world'),
                         'debug': debug, 'gui': gui, 'paused': paused, 'use_sim_time': use_sim_time, 'headless': headless}.items()
    )

    # Node to spawn URDF
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'vmegarover', '-topic', 'robot_description', '-xacro', model],
                        output='screen')

    return LaunchDescription([
        DeclareLaunchArgument('model', default_value=model),
        DeclareLaunchArgument('paused', default_value=paused),
        DeclareLaunchArgument('use_sim_time', default_value=use_sim_time),
        DeclareLaunchArgument('gui', default_value=gui),
        DeclareLaunchArgument('headless', default_value=headless),
        DeclareLaunchArgument('debug', default_value=debug),
        gazebo,
        spawn_entity,
    ])
