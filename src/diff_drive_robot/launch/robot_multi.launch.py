import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction, DeclareLaunchArgument
from launch_ros.actions import Node, PushRosNamespace
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'diff_drive_robot'
    world_path = os.path.join(get_package_share_directory(package_name), 'worlds', 'obstacles.world')
    urdf_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'robot.urdf.xacro')

    declare_world = DeclareLaunchArgument(
        name='world', default_value=world_path,
        description='Full path to the world model file to load')

    robots = [
        {'name': 'robot1', 'x': 0, 'y': 0, 'z': 1.0},
        {'name': 'robot2', 'x': 2, 'y': 0, 'z': 0.5},
        # Add more robots as needed
    ]

    spawn_robots = []
    for robot in robots:
        spawn_robots.append(
            GroupAction([
                PushRosNamespace(robot['name']),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([
                        os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')
                    ]),
                    launch_arguments={'use_sim_time': 'true', 'urdf': urdf_path}.items(),
                ),
                Node(
                    package='ros_gz_sim',
                    executable='create',
                    arguments=[
                        '-topic', f'/{robot["name"]}/robot_description',
                        '-name', robot['name'],
                        '-x', str(robot['x']),
                        '-y', str(robot['y']),
                        '-z', str(robot['z'])
                    ],
                    output='screen',
                ),
            ])
        )

    # Add Gazebo server/client and bridge as before...
    # (Copy from your existing launch file)
    # Launch the gazebo server to initialize the simulation
    gazebo_server = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
                    )]), launch_arguments={'gz_args': ['-r -s -v1 ', world_path], 'on_exit_shutdown': 'true'}.items()
    )

    # Always launch the gazebo client to visualize the simulation
    gazebo_client = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
                    )]), launch_arguments={'gz_args': '-g '}.items()
    )

    # Launch the Gazebo-ROS bridge
    bridge_params = os.path.join(get_package_share_directory(package_name),'config','gz_bridge.yaml')
    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',]
    )
    return LaunchDescription([
        # ... declare_world, gazebo_server, gazebo_client, ros_gz_bridge, etc.
        *spawn_robots,
        declare_world,
        gazebo_client,
        gazebo_server,
        ros_gz_bridge

    ])
