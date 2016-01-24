Student Name: Donal O'Sullivan
Student Number: a09577ec2fe97c36c854f4010526ed2f81b4747edea7d4247ded8c32f76e93f2

Dependency Info:
 - The program has no external dependencies

Running and Testing:
 - To run the program run
      python chatroom_server.py
 - Testing of the program can be done with the multi-threaded client program chatroom_client.py, this can be run with
      python chatroom_client.py

      test client commands - these are used to generate the actual commands that are transported over TCP:

        join room_name client_name
        leave room_name client_name
        disconnect client_name
        chat room_name join_id client_name message


Other info:
  - The threadpool module was downloaded from http://code.activestate.com/recipes/577187-python-thread-pool/
  - The test server ip is 46.101.47.238
  - The TCPServer program is running on port 9800
