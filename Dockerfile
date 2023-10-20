FROM ros:humble


# install project

RUN mkdir -p ~/ros2_ws/src
RUN cd ~/ros2_ws/src && git clone https://github.com/HuskyKingdom/ros2_humble_gmapping.git
RUN cd ~/ros2_ws && . /opt/ros/humble/setup.sh && colcon build