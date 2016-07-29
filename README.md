# Hotwire

User-friendly launcher for ROS processes.

### Desired features
    - list known behaviors and demos
    - start a process with roslaunch
    - stop the current process

### Design goals
    - The launcher should be easy to install on a new robot, with minimal dependencies (ros-base and pure python packages).
    - The launcher should always be running on the robot.
    - The launcher should not interfere with the any other processes unless it is in active use.
    - It should be easy to register new launch files and catkin workspaces with the launcher.
    - The frontend should not require any installation. (Send commands by web or rostopic)
    - Some features should be password-protected.
