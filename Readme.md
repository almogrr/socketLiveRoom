# Flask-SocketIO Chat Application

This is a simple chat application built using Flask and SocketIO. It allows users to create chat rooms, join existing rooms, send messages, and view message history.

## Features

- **User Authentication:** Users can enter a username to join the chat application. Usernames are unique within the application.
- **Room Creation and Joining:** Users can create new chat rooms by providing a room name and a key. They can also join existing rooms by entering the room name and key.
- **Real-time Messaging:** Users can send and receive messages in real-time within the chat rooms. Messages are displayed instantly to all users in the same room.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the chat application.

3. Enter a username and click "Submit" to enter the chat dashboard.

4. From the dashboard, you can create a new room, join an existing room, or delete a room if you're the creator.

5. Once inside a room, you can send messages to the chat. Messages will be displayed in real-time to all users in the same room.

6. To leave a room, simply close the browser tab or click the "Leave Room" button.


## Usage Tips

1. When accessing the chat application with multiple users on the same computer, it's recommended to open separate browser sessions or use different browsers to prevent session conflicts.

2. If accessing the chat application with multiple users in the same browser, open at least one browser session in incognito or private mode to avoid session conflicts.

3. If you forget to enter incognito mode and encounter a situation where the old username changes to a new one, simply log out of the chat application, clear your browser's cookies or local storage, and log in again with the desired username.


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
