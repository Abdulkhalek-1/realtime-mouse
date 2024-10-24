# Realtime Mouse Movement with WebSocket in Django

This project demonstrates real-time mouse movement tracking using Django Channels with an **in-memory channel layer** (no Redis required). It leverages WebSockets to provide real-time communication between connected clients.

## Features
- Real-time mouse movement tracking.
- WebSocket-based communication using Django Channels.
- In-memory channel layer (no external dependencies like Redis).
- Dockerized setup for easy deployment.

---

## Requirements
- Python 3.x
- Django 4.x
- Django Channels 3.x

---

## Setup (Without Docker)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdulkhalek-1/realtime-mouse
   cd realtime-mouse
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:  
   Open your browser and navigate to `http://127.0.0.1:8000`. You should be able to see the real-time mouse movement tracking.

---

## Setup (With Docker)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdulkhalek-1/realtime-mouse
   cd realtime-mouse
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t realtime-mouse .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:8000 --name realtime-mouse realtime-mouse
   ```

4. **Access the app**:  
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Key Files

- **consumers.py**: Handles WebSocket events for sending and receiving real-time mouse movement data.
- **routing.py**: Defines WebSocket routes.
- **asgi.py**: Configures Django to use ASGI for handling WebSocket connections.
- **settings.py**: Configures Django Channels with an in-memory channel layer.

Example of how the **in-memory channel layer** is configured in `settings.py`:
```python
# settings.py
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
