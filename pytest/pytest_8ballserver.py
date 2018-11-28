#!/usr/bin/python3
import socket
import sys

first_res = "Your guess is as good as mine."
sec_res = "You need a vacation."
thrid_res = "It's Trump's fault!"
forth_res = "I don't know. What do you think?"
fifth_res = "Nobody ever said it would be easy, they only said it would be worth it."
sixth_res = "You really expect me to answer that?"
seven_res = "You're going to get what you deserve."
eight_res = "That depends on how much you're willing to pay."
list_of_res = [first_res, sec_res, thrid_res, forth_res, fifth_res, sixth_res, seven_res, eight_res]
list_of_questions = []
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    s.bind((host_name, 9000))
    s.listen(5)
    port_num = sys.argv[1]
    print "Listening on port", port_num
    j = 0
    i = 1
    while True:
        clientsocket, address = s.accept()
        print "Server: Connection from ", address
        while True:
            message = clientsocket.recv(1024)
            if message in list_of_questions:
                print("you asked the same questions!")
            list_of_questions.append(message)
            file_name = "8ball_message_" + str(i) + ".txt" 
            test_file = open(file_name, "wb")
            res = list_of_res[j]
            test_file.write(bytes(res))
            i = i + 1
            j = j + 1
            if (j == 8):
                j = j - 8
            if message == "":
                break
            if message == "EXIT" or "__EXIT__":
                sys.exit(0)
        clientsocket.close()

