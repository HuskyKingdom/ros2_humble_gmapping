# ROS 2 Humble SLAM Gmapping with Map Clean Service



<img src="docs/demo.gif"></td>


SLAM(Simultaneous Localization and Mapping) is the command problem in embodied AI & robotics that requires updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.

This contains package openslam_gmapping and slam_gmapping which is a ROS2 wrapper for OpenSlam's Gmapping. Using slam_gmapping, you can create a 2-D occupancy grid map (like a building floorplan) from laser and pose data collected by a mobile robot. 

As sometimes we require building a new map based on modifyed environment and wish to abort what have been built, common approach to this would be re-start SLAM node, which is not condidarable in certain context due to its non-efficiency or other reasons.

In this project, I have altered the sourse code from [SLAM_GMAPPING](https://github.com/Project-MANAS/slam_gmapping) and added a server so that you can clear the current map built at anytime and build a new map without re-boot your SLAM node.



## Install

Clone the repo:

```
git clone https://github.com/HuskyKingdom/ros2_humble_gmapping.git
```

Put the project files under your ROS2 workspace and build the source files:

```
cd <your_workspace>
colcon build --packages-select ros2_humble_gmapping
```

## Launch

Sourcing your underlay & overlay first, then launch the pipeline through the following:

```
cd ros2_humble_gmapping/launch
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
