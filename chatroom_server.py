import sys
import socket
import threadpool
import os
import re
import chatroom_manager

# global threadpool for server
server_thread_pool = threadpool.ThreadPool(500)

port_number = 9000#int(sys.argv[1])

ip_address = socket.gethostbyname(socket.gethostname())

current_chatroom_manager = chatroom_manager.ChatroomManager(port_number)

def create_server_socket():
    # create socket  and initialise to localhost:8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', port_number)

    print "starting up on %s port %s\n" % server_address

    # bind socket to server address and wait for incoming connections4
    sock.bind(server_address)
    sock.listen(1)

    while True:
        # sock.accept returns a 2 element tuple
        connection, client_address = sock.accept()
        #print "Connection from %s, %s\n" % connection, client_address
        # Hand the client interaction off to a seperate thread
        server_thread_pool.add_task(
            start_client_interaction,
            connection,
            client_address
        )


def start_client_interaction(connection, client_address):
    try:

        while True:

            #A client id is generated, that is associated with this client
            #It is to be used to check that one thread does not spawn multiple
            #clients.
            curr_client_id = current_chatroom_manager.gen_client_id()

            data = connection.recv(1024)
            print "received message: %s" % data

            # Respond to the appropriate message
            if data == "KILL_SERVICE\n":
                kill_service(connection)
            elif data[0:4] == "HELO" and data[-1] == '\n':
                helo_response(connection, data)
            else:
                split_data = seperate_input_data(data)
                #Check for Disconnect Command
                if split_data[0] == "JOIN_CHATROOM":
                    join_chatroom(connection, client_address, curr_client_id, split_data)
    finally:
        connection.close()

def kill_service(connection):
    # Kill service
    response = "Killing Service\n"
    connection.sendall("%s" % response)
    os._exit(0)

def helo_response(connection, data):
    # Respond to HELO message
    # Construct the appropriate response
    response = data
    response += "IP:[" + ip_address + "]\n"
    response += "Port:[" + str(port_number) +"]\n"
    response += "StudentID:[a09577ec2fe97c36c854f4010526ed2f81b4747edea7d4247ded8c32f76e93f2]\n"
    connection.sendall("%s" % response)

def join_chatroom(connection, client_address, client_id, split_data):
    #Create client and add to chatroom
    current_chatroom_manager.add_client( client_id, client_address, 0, split_data[7], connection )
    current_chatroom_manager.add_client_to_chatroom( split_data[1], current_chatroom_manager.get_active_client( client_id ) )
    #Create and send response
    chatroom_name = split_data[1]
    room_ref = get_active_chatroom(chatroom_name).id
    response = "JOINED_CHATROOM: %s\nSERVER_IP: %s\nPORT: %s\nROOM_REF:%s\nJOIN_ID:%s\n" % chatroom_name, ip_address, port_number, room_ref, client_id

#Function to split reveived data strings into its component elements
def seperate_input_data(input_data):
    seperated_data = []

    input_data_split = input_data.split('\n')

    for i in input_data_split:
        i = i.split(": ")
        #seperated_data.append(i)
        for j in i:
            j = j.split(':')
            for k in j:
                seperated_data.append(k)

    return seperated_data

if __name__ == '__main__':
    create_server_socket()
    # wait for threads to complete
    server_thread_pool.wait_completion()

# Plan For Chat Server
#
# Have one socket per client
# Have two threads per client
#   - One listening for messages
#   - One for sending messages
# Have an
