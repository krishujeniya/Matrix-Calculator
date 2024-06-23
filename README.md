# My Tkinter App

This is a simple Tkinter application containerized using Docker.

## Building the Docker Image

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

   ```
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix determinant_founder
   ```

   **On macOS with XQuartz**:

   ```
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 determinant_founder
   ```

   **On Windows with Xming**:

   ```
   docker run -it --rm -e DISPLAY=host.docker.internal:0 determinant_founder
   ```
