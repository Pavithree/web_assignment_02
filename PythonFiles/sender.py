import random
import pickle
import socket

# def rand_binary(num): Function to generate random 8-bit number

def rand_binary(num):

    binary_string = "0b"
    for i in range(num):
        temp = str(random.randint(0, 1))
        binary_string += temp

    return (binary_string)


length_of_binaryNumber = 8
message = []
for i in range(0,4):
    binary_num = rand_binary(length_of_binaryNumber)
    message.append(int(binary_num,2))


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

# def Calculate_Checksum(message): returns checksum of message

def Calculate_Checksum(message):
    sum = 0
    for itr in range(0, len(message) - 1):
        if itr == 0:
            sum = onesComplimentAddition(message[itr], message[itr + 1])
            print("var {} :{}".format(1, bin(message[itr])))
            print("var {} :{}".format(2, bin(message[itr + 1])))
            print("Sum   :{}".format(bin(sum)))
        else:
            sum = onesComplimentAddition((message[itr + 1]), sum)
            print("var {} :{}".format(1, bin(sum)))
            print("var {} :{}".format(2, bin(message[itr + 1])))
            print("Sum   :{}".format(bin(sum)))
    var = ~sum
    checkSum = BinaryCompliment(sum)
    # checkSum = format(checkSum, '#010b')
    print("Checksum {}".format(bin(checkSum)))
    print("\n")
    return checkSum

# Client function

def client():
    # host = socket.gethostname()
    host = '127.0.0.1'
    port = 8080
    print("Connected to tmps: ({}, {})".format(str(host),str(port)))

    s = socket.socket()
    s.connect((host, port))
    checksum = Calculate_Checksum(message)
    message.append(checksum)
    data = pickle.dumps(message)

    s.send(data)
    data = s.recv(1024)

    unpickledData = pickle.loads(data)
    print("Response from the receiver b ' Receiver Message")
    if unpickledData[0] == 1:
            print("Data is correctly received and checksum is {}".format(bin(unpickledData[1])))
    else:
        print("Corrupted Data")
    s.close()


if __name__ == '__main__':
    client()