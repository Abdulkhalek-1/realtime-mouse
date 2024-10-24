from channels.generic.websocket import AsyncJsonWebsocketConsumer


class MouseConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Get user ID from the URL (e.g., through query parameters)
        self.username = self.scope["url_route"]["kwargs"]["username"]
        self.room_name = self.scope["url_route"]["kwargs"]["group_id"]
        self.room_group_name = f"group_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive_json(self, content):
        # Get x_pos and y_pos from received content
        x_pos = content.get("x_pos")
        y_pos = content.get("y_pos")
        if not (x_pos or y_pos):
            return

        # Log the received position for debugging
        print(
            f"User {self.username} sent: x_pos={x_pos}, y_pos={y_pos} group: {self.room_name}"
        )

        # Resend the received data to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_mouse_position",
                "username": self.username,  # Send user ID with the message
                "x_pos": x_pos,
                "y_pos": y_pos,
            },
        )

    async def send_mouse_position(self, event):
        # Send the mouse position back to the WebSocket
        await self.send_json(
            {
                "message": "Broadcasting mouse position",
                "username": event["username"],  # Include the user ID
                "x_pos": event["x_pos"],
                "y_pos": event["y_pos"],
            }
        )
