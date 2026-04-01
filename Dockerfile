FROM osrf/ros:jazzy-desktop

# 1. Аргументи
ARG USERNAME=pivden
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 2. Створюємо користувача (виконується від root)
# Спочатку видаляємо стандартного користувача 'ubuntu', якщо він має UID 1000
RUN if getent passwd $USER_UID ; then userdel -r $(getent passwd $USER_UID | cut -d: -f1); fi \
    && if getent group $USER_GID ; then groupdel $(getent group $USER_GID | cut -d: -f1); fi \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# 3. Встановлюємо системні пакети (виконується від root)
RUN apt-get update && rosdep update && apt-get install -y \
    python3-pip \
    python3-opencv \
    usbutils \
    bash-completion \
    ros-jazzy-turtlesim \
    ros-jazzy-turtle-tf2-py \
    && rm -rf /var/lib/apt/lists/*

# 4. Перемикаємось на користувача
USER $USERNAME
# ВАЖЛИВО: Тепер всі наступні команди RUN виконуються від імені pivden 
# і зміна ~/.bashrc стосуватиметься саме його домашньої папки!

# 5. Налаштовуємо робоче оточення (вже як користувач pivden)
WORKDIR /home/$USERNAME/ros2_ws

# Автоматичний source ROS та colcon_cd при вході
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc \
    && echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc \
    && echo "export _colcon_cd_root=/opt/ros/jazzy/" >> ~/.bashrc

# 6. Налаштовуємо змінні оточення
ENV ROS_DISTRO=jazzy
ENV SHELL=/bin/bash

# Залишаємо WORKDIR у нашій папці користувача
WORKDIR /home/$USERNAME/ros2_ws
