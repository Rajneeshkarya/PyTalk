# Simple Python Chat Application

This is a simple command-line based chat application implemented in Python. It allows users to either create a chat room or join an existing one. The application uses sockets for communication between the client and server.

## Features

- Create a chat room
- Join an existing chat room
- Password protection for chat rooms

## Requirements

- Python 3.x
- Standard libraries: `argparse`, `socket`

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Rajneeshkarya/PyTalk
    cd PyTalk
    ```
2. Install the requirements
    ```bash
    pip3 install -r requirements.txt
    ```
3. Run the chat application:

    ```bash
    python PyTalk.py -h
    ```

    This will display the available options and usage instructions for the chat application.

4. Start a Chat Room:

    ```bash
    python PyTalk.py -c -p <port> -pwd <password>
    ```

    This command creates a chat room on the specified port with an optional password.

4. Join a Chat Room:

    ```bash
    python PyTalk.py -j -i <ip_address> -p <port>
    ```

    This command lets you join an existing chat room by specifying the IP address and port.

## Usage Examples

1. To create a chat room:

    ```bash
    python PyTalk.py -c -p 12345 -pwd mypassword
    ```

2. To join a chat room:

    ```bash
    python PyTalk.py -j -i 127.0.0.1 -p 12345
    ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


**Note:** This is a simple chat application for educational purposes. It may not be suitable for production environments and lacks advanced security features. Use it responsibly and at your own risk.
