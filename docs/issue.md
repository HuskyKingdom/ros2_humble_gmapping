# Memory Leaking Issue


## Reproduce in Docker

Pull ROS2 HUMBLE image:

```
docker pull ros:humble
```

Build environment by provided docker file:

```
docker build -t ros2:reproduce .
```

Run a container:
```
docker run --name reproduce --entrypoint /bin/bash -it ros2:reproduce
```

## Launch

Inside the container run the following the launch the mapping node(s):

```
source /opt/ros/humble/setup.bash
cd ~/ros2_ws && source install/setup.bash 
cd ~/ros2_ws/src/ros2_humble_gmapping/slam_gmapping_altered/launch
ros2 launch pipeline_launch.py
```

The node slam_gmapping subscribes to ``sensor_msgs/LaserScan`` on ros2 topic scan. It publishes the `nav_msgs/OccupancyGrid` on ``/map``topic.

You can customize the TF nodes in launch file if needed.

Map Meta Data and Entropy is published on ``map_metadata`` and ``entropy`` respectively.

The node starts a server ``/map_clear_serve`` which takes requests in type ``std_srvs/srv/Empty`` and response with the same tyoe. Once this server was called, the node will clear the current map and build a new one.


### About


<a href="https://yhscode.com">Contact me at: <strong>me@yhscode.com</strong></a>

<a href="https://yhscode.com"><strong>View my full bio.</strong></a>
    <br />
    <br />
  </p>
