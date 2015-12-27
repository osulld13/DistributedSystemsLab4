import chatroom_server
import chatroom_manager

test_chatroom_manager = chatroom_manager.ChatroomManager(80)

test_chatroom_manager.add_client(
    1, 0, 0,
    "Cool_Name",
    "thing"
)

test_chatroom_manager.add_client_to_chatroom(
    "dummy_room",
    test_chatroom_manager.get_active_client( 1 )
)
