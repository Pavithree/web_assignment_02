import socket
import pickle

test_message = []
checksum = 0
flag = 0
result = []
NUM = 1 << 8


# def onesComplimentAddition(num1,num2) : returns result which is 1's compliment addition of num1 and num2

def onesComplimentAddition(num1, num2):
    result = num1 + num2
    return result if result < NUM else (result + 1) % NUM

# def BinaryCompliment(decimalNum): returns 1's compliment of decimal number

def BinaryCompliment(decimalNum):
    # binaryNum = bin(decimalNum)
    binaryNum = format(decimalNum, '#010b')
    binString = str(binaryNum)
    checksum = "0b"
    for i in range(2, len(binString)):
        if binaryNum[i] == '1':
            checksum += '0'
        else:
            checksum += '1'
    checkSumInt = int(checksum, 2)
    return checkSumInt

# def validate_data(message_one, check_sum) : function to validate checksum

def validate_data(message_one, check_sum):
    new_message = []
    for i in range(0, len(message_one)):
        new_message.append(message_one[i])
    new_message.append(check_sum)
    sum = 0
    for itr in range(0, len(new_message) - 1):
        if itr == 0:
            sum = onesComplimentAddition(new_message[itr], new_message[itr + 1])
            print("var {} :{}".format(1, bin(new_message[itr])))
            print("var {} :{}".format(2, bin(new_message[itr + 1])))
            print("Sum   :{}".format(bin(sum)))
        else:
            sum = onesComplimentAddition(new_message[itr + 1], sum)
            print("var {} :{}".format(1, bin(sum)))
            print("var {} :{}".format(2, bin(new_message[itr + 1])))
            print("Sum   :{}".format(bin(sum)))

    tmp = format(sum, '#010b')
    print("Got the following sum {} after the validation".format(tmp))
    if tmp == '0b11111111':
        print("Successful transmission")
        flag = 1
        result.append(flag)
    else:
        print("Corrupted Data")
        flag = 0
        result.append(flag)

# Server function

def server():
    # host = socket.gethostname()
    host = '127.0.0.1'
    port = 8080

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    s.listen(1)
    client_socket, address = s.accept()
    print("Connection from: " + str(address))

    message = client_socket.recv(1024)
    unpickledData = pickle.loads(message)
    for itr in range(0, len(unpickledData)):
        if itr < 4:
            test_message.append(unpickledData[itr])
        else:
            checksum = unpickledData[itr]

    print("Got the following message {} and {} as checksum from the sender".format(test_message, checksum))
    validate_data(test_message, checksum)
    result.append(checksum)
    output = pickle.dumps(result)
    client_socket.send(output)


    s.close()

if __name__ == '__main__':
    server()