import chatroom

if __name__ == '__main__':
	room = chatroom.Chatroom(0, 0, "test_chat")
	client = chatroom.Client(0, 0, 0, "test_client", "dummy_socket_data")
	other_client = chatroom.Client(1, 1, 1, "other_test_client", "dummy_socket_data")
	print room.add_client(client, 0)
	print room.add_client(client, 1)
	print room.add_client(other_client, 2)
	print room.add_client(other_client, 0)
	print room.active_clients
	print room.remove_client(client)
	print room.active_clients
