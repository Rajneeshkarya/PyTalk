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
    git clone https://github.com/your-username/your-chat-repo.git
    cd your-chat-repo
    ```

2. Run the chat application:

    ```bash
    python chat.py -h
    ```

    This will display the available options and usage instructions for the chat application.

3. Start a Chat Room:

    ```bash
    python chat.py -c -p <port> -pwd <password>
    ```

    This command creates a chat room on the specified port with an optional password.

4. Join a Chat Room:

    ```bash
    python chat.py -j -i <ip_address> -p <port>
    ```

    This command allows you to join an existing chat room by specifying the IP address and port.

## Usage Examples

1. To create a chat room:

    ```bash
    python chat.py -c -p 12345 -pwd mypassword
    ```

2. To join a chat room:

    ```bash
    python chat.py -j -i 127.0.0.1 -p 12345
    ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** This is a simple chat application for educational purposes. It may not be suitable for production environments and lacks advanced security features. Use it responsibly and at your own risk.
