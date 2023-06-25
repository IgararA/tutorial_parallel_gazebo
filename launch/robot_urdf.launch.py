import os

from ament_index_python.packages import get_package_share_directory

from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription



def generate_launch_description():

    ld = LaunchDescription()

    used_wheel = LaunchConfiguration('used_wheel_arg')
    used_wheel_arg = DeclareLaunchArgument('used_wheel_arg', default_value='False', description="是否使用轮子")
    
    # urdf = os.path.join(get_package_share_directory("five_bar_link"), "urdf/FiveBarLink.urdf")
    urdf = os.path.join(get_package_share_directory("five_bar_link"), "urdf/five_bar_link_wheel.urdf")

    if urdf != "":
            print(f"Found URDF PATH {urdf}")

    with open(urdf, 'r') as uf:
        robot_desc = uf.read()

    gazebo_world = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource(
                            os.path.join(get_package_share_directory('gazebo_ros'),
                            'launch', 'gazebo.launch.py')))



    start_spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'robot_model', '-file', urdf,
                                    '-x', '0',
                                    '-y', '0',
                                    '-z', '0',
                                    '-R', '0',
                                    '-P', '0',
                                    '-Y', '0'],
                        output='screen')


    start_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        arguments=[urdf],
        output='screen')

    start_joint_state_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen')
    



    ld.add_action(start_robot_state_publisher)
    ld.add_action(start_joint_state_gui)
    ld.add_action(gazebo_world)
    ld.add_action(start_spawn_entity)
    ld.add_action(used_wheel_arg)


    return ld

if __name__ == "__main__":
    generate_launch_description()