import sys
import socket
import threadpool
import os
import chatroom_manager

# global threadpool for server
server_thread_pool = threadpool.ThreadPool(40)

#port_number = int(sys.argv[1])
port_number = 9000

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
        data = connection.recv(1024)
        print "received message: %s" % data

        # Respond to the appropriate message
        if data == "KILL_SERVICE\n":
            # Kill service
            response = "Killing Service\n"
            connection.sendall("%s" % response)
            os._exit(0)
        elif data[0:4] == "HELO" and data[-1] == '\n':
            # Respond to HELO message
            # Construct the appropriate response
            response = data
            response += "IP:[" + socket.gethostbyname(socket.gethostname()) + "]\n"
            response += "Port:[" + str(port_number) +"]\n"
            response += "StudentID:[a09577ec2fe97c36c854f4010526ed2f81b4747edea7d4247ded8c32f76e93f2]\n"
            connection.sendall("%s" % response)

    finally:
        connection.close()


if __name__ == '__main__':
    create_server_socket()
    # wait for threads to complete
    server_thread_pool.wait_completion()
