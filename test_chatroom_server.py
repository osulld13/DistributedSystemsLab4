import chatroom_server

data = "JOIN_CHATROOM: [chatroom name]\nCLIENT_IP: [IP Address of client if UDP | 0 if TCP]\nPORT: [port number of client if UDP | 0 if TCP]\nCLIENT_NAME: [string Handle to identifier client user]"
seperated_data = chatroom_server.seperate_input_data(data)
print seperated_data
