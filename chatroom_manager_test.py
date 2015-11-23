import chatroom_manager

# initialise chatroom manager n port 9000
# test to see if initialization occured
chatroom_manager = chatroom_manager.ChatroomManager(9000)
assert chatroom_manager

# test adding a chatroom
chatroom_manager.add_chatroom("test_room")
assert len(chatroom_manager.active_chatrooms) == 1

# test adding a chatroom with the same name
chatroom_manager.add_chatroom("test_room")
assert len(chatroom_manager.active_chatrooms) == 1

# test the removal of chatrooms from the chatroom Mangager
chatroom_manager.remove_chatroom(chatroom_manager.get_active_chatroom("test_room").id)
assert len(chatroom_manager.active_chatrooms) == 0

#test the add_client function
chatroom_manager.add_client("test_room", 0, 0, "osulld13")
assert len(chatroom_manager.active_clients) == 1
assert len(chatroom_manager.get_active_chatroom("test_room").active_clients) == 1

# Test the client chatroom creation on join
chatroom_manager.add_client("other_test_room", 0, 0, "test_user")
assert len(chatroom_manager.active_chatrooms) == 2
assert len(chatroom_manager.active_clients) == 2
assert len(chatroom_manager.get_active_chatroom("other_test_room").active_clients) == 1

chatroom_manager.add_client("other_test_room", 0, 0, "test_user")
assert len(chatroom_manager.active_chatrooms) == 2
assert len(chatroom_manager.active_clients) == 3
assert len(chatroom_manager.get_active_chatroom("other_test_room").active_clients) == 2

# Test the removal of clients
chatroom_manager.remove_client(2)
assert len(chatroom_manager.active_chatrooms) == 2
assert len(chatroom_manager.active_clients) == 2
assert len(chatroom_manager.get_active_chatroom("other_test_room").active_clients) == 1

chatroom_manager.remove_client(1)
assert len(chatroom_manager.active_chatrooms) == 2
assert len(chatroom_manager.active_clients) == 1
assert len(chatroom_manager.get_active_chatroom("other_test_room").active_clients) == 0

chatroom_manager.remove_client(3)
assert len(chatroom_manager.active_chatrooms) == 2
assert len(chatroom_manager.active_clients) == 1
assert len(chatroom_manager.get_active_chatroom("other_test_room").active_clients) == 0


chatroom_manager.log_member_data()
