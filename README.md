<a id="readme-top"></a>

![GitHub repo size](https://img.shields.io/github/repo-size/krishujeniya/DETERMINANT-FOUNDER)
![GitHub contributors](https://img.shields.io/github/contributors/krishujeniya/DETERMINANT-FOUNDER)
![GitHub stars](https://img.shields.io/github/stars/krishujeniya/DETERMINANT-FOUNDER?style=social)
![GitHub forks](https://img.shields.io/github/forks/krishujeniya/DETERMINANT-FOUNDER?style=social)

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">DETERMINANT-FOUNDER</h3>

</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This is a simple Tkinter application containerized using Docker.

### Key Features

- **User Authentication and Profile Management**
- **Posting Updates with Text and Media**
- **Liking and Commenting on Posts**
- **Following and Unfollowing Users**
- **Real-time Notifications**
- **Search Functionality**

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![Tkinter](https://img.shields.io/badge/Tkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python**: Ensure you have the latest version of Python installed. [Python Installation Guide](https://www.python.org/downloads/)
- **Docker**: Ensure you have the latest version of Docker installed. [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/krishujeniya/DETERMINANT-FOUNDER.git
   cd DETERMINANT-FOUNDER
   ```
2. Build the Docker image
   ```sh
   docker build -t determinant_founder .
   ```

## Step-by-Step Guide to Enable X11 Forwarding in Docker

1. **Install XQuartz (macOS) or Xming (Windows)**:
   - **macOS**: Install XQuartz from [XQuartz.org](https://www.xquartz.org/).
   - **Windows**: Install Xming from [Xming.org](https://sourceforge.net/projects/xming/).

2. **Allow Connections**:
   - **macOS**: Open XQuartz, go to **Preferences > Security**, and check "Allow connections from network clients".
   - **Windows**: Start Xming with default settings.

3. **Run Docker Container with X11 Forwarding**:

   **On Linux**:

   ```sh
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix determinant_founder
   ```

   **On macOS with XQuartz**:

   ```sh
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 determinant_founder
   ```

   **On Windows with Xming**:

   ```sh
   docker run -it --rm -e DISPLAY=host.docker.internal:0 determinant_founder
   ```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Docker](https://www.docker.com/)
* [Open Source Community](https://opensource.org/)
* [Contributors](https://github.com/determinant_founder/my-tkinter-app/graphs/contributors)

