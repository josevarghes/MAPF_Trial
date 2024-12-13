# Simulation for Multi-Agent Path Finding (MAPF) in ROS2
Use https://shields.io/badges to create badges.

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytorch](https://img.shields.io/badge/pytorch-blue?logo=pytorch)
![Static Badge](https://img.shields.io/badge/raspberry-purple?logo=raspberrypi)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Passing Badge](https://img.shields.io/badge/Build-passing-green?style=for-the-badge)
![ROS Version](https://img.shields.io/badge/ROS%20version-humble-blue?style=for-the-badge)

<!-- TABLE OF CONTENTS -->
## Table of Contents
1. [About The Project](#about-the-project)
   - [Built With](#built-with)
2. [Getting Started](#getting-started)
   - [Setup](#setup)
   - [Installation](#installation)
3. [Usage](#usage)
4. [Roadmap](#roadmap)
5. [License](#license)
6. [Contact](#contact)
7. [Reference](#Reference)



<!-- ABOUT THE PROJECT -->
## About The Project

This project focuses on simulating multi-Agent Path Finding in ROS2, motivated by the need to efficiently coordinate multiple robots in dynamic environments. It is crucial for tasks like warehouse automation and robot fleets, optimizing paths to avoid collisions while minimizing travel time and resource usage.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


###  Software and Tools Used
Describe here, which software and which versions you used, e.g.:
- Python 
- Anaconda 
- ROS2
- Gazebo
- ...

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started
Here we describe, how to get the project running.

### Setup
Describe the setup and the used hardware.

### Installation
Provide a step-by-step guide on how to get the project running locally. This should include steps to install necessary software, how to set up the environment, and how to run the application. In the following example we describe for example, how to clone the github repository, install conda, create a virtual environment from an myenv.yml file and run a python file test.py. Note, that this can also be described different and does not have to be the same structure, just make sure, that one can get your project running. Important is always, that you you specify, which versions you used of which software! Also make sure, that you create a .yml file from your environment, when you use python. Example:

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install Anaconda as described [here](https://docs.anaconda.com/free/anaconda/install/index.html)
3. Create an environment with conda by putting this in your command line:
   ```sh
   conda env create -f myenv.yml
   ```
4. Run the test.py file by using a IDE or run this in command line:
   ```sh
   python test.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Examples of Usages
Describe, how use your code by examples:
### Example 1
### Example 2

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
Description of the milestones of this project. Example:
- [ ] Research on approaches for the MAPF tasks
   - [ ] Find proper algorithms for implementation 
- [ ] Get familiar with the software  
  - [ ] Install the ROS2 
  - [ ] Install Gazebo, build a simulator
- [ ] Implement MAPF algorithms and run in the simulator
- [ ] Compare the performance between different algorithms

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Folder structure
Describe here, how your project is structured:
Examples:
```text
project/
```text
create3_project/
├── config/
│   ├── rviz config
│   ├── LiDAR sensor config
│   └── mapper config
├── include/
│   └── Header file of the publisher
├── launch/
│   ├── old_lidar/
│   │   └── Python files from create3_examples/create3_lidar_slam
│   ├── old_nolidar/
│   │   └── Python files based on create3_examples/create3_lidar_slam with modifications
│   ├── launch_publisher.py (C++ tester)
│   └── Python files (shortcuts) to launch all lidar or all no lidar files
├── run/
│   ├── map.py
│   ├── run_avoider.py
│   └── run_mapper.py
└── src/
    └── Implementation file of the publisher
```
Another example: A common approach for data science projects can be found [here](https://neptune.ai/blog/best-practices-for-data-science-project-workflows-and-file-organizations).

```text
create3_project/
├── data/
│   ├── external
│   ├── interim
│   ├── processed 
│   └── processes
├── models
├── src/
    ├── data
    ├── features
    └── model
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Your Name:
Your e-mail:

# Reference






