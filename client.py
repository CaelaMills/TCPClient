# Setting up sockets
import socket
# Setting up logging | logging is the recorded event of the message or event you are performing/trying to send.
import logging
# Setting up threading: 'threading' is process of creating and managing multiple threads (or network connections) within a single program.
# Each thread operates independently, allowing the program to execute multiple tasks concurrently
# and improve overall efficiency.
import threading

def handle_connection(target_host, target_port): # def: defines/specifies the start of a new function.
    # Create a new socket object within the function
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # What does this stream above^^^ mean?
    # Well, your socket.socket... stream created a new socket object for network communication however,
    # that socket has to have the following: 'AF_INET' for IPv4 addresses that may be connecting to our computer
    # as well as 'SOCK_STREAM' that indicated that our socket is using TCP.


    try: # try: indicates that the code has the potential to raise exceptions (errors) if something weird occurred.
        # logging.basicConfig(...): this method sets up/configures how logging will work (where logs
        # are saved, what level of detail to log, etc.).
        # logging.info(...): records informational messages and formats those messages are:
        # asctime or 'as time' asks for a timestamp of the log message.
        # levelname asks for the type of security level of the log message.
        # message asks for the actual content of the message that you are trying to send.
        logging.basicConfig(filename='client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        target_host = "google.com"
        target_port = 80

        # Connect the client to your target
        # As you notice when assigning your client object to the variable connect, shorthand coding becomes available
        # print(...): this method allows us to receive immediate, readable, feedback as to what our program is doing;
        # this is great for monitoring.
        client.connect((target_host, target_port))
        logging.info(f"Connected to {target_host} on port {target_port}")
        print("Connected to server")

        # Send some data -- send an HTTP request
        # Assigning an HTTP header that is assigned the host "google.com"
        response = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
        client.send(response)
        logging.info("Response received") # This method allows us to record each action that occurs.
        print("Response received")

        # Receive some data
        response = client.recv(4096) # 4096 is the default buffer size integer that a server can handle per request.

        print(response)

    except Exception as e: # the 'except' command handles any error inside of it's block
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")

    finally:
        client.close()
        logging.info("Connection closed")
        print("Connection closed")

# As I received the HTTP response message of 'HTTP/1.1 301 Moved Permanently' what this means is the
# '301' HTTP status code indicates that the requested resource "google.com" has been permanently moved
# to a whole new URL.

# Create and start multiple threads
# The variable 'threads' is assigned '[]' or an array that holds whatever number of threads you desire.
threads = [] # Think of '[]' as a list that holds things.
for i in range(4):  # Example: create 4 concurrent connections
    thread = threading.Thread(target=handle_connection, args=("google.com", 80)) # args=(...): this method indicates
    # that the arguments passed are the string and integer variables that's been created above.
    threads.append(thread) # This method adds each newly created thread to the threads list.
    thread.start() # This method opens a new thread (a new line of connection).

# Wait for all threads to complete
for thread in threads:
    thread.join() # Waits for all threads to finish running before closing the program.
