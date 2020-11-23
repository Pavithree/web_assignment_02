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
    print("check_sum = calculate_checksum (message)\n")
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


# def validate_data(message_one, check_sum): validates if there is any error in the transmitted message


def validate_data(message_one, check_sum):
    print("validate_data(message, checksum)")
    new_message = []
    for i in range(0, len(message_one)):
        new_message.append(message_one[i])
    new_message.append(check_sum)
    sum = 0
    for itr in range(0, len(new_message) - 1):
        if itr == 0:
            sum = onesComplimentAddition(new_message[itr], new_message[itr + 1])
        else:
            sum = onesComplimentAddition(new_message[itr + 1], sum)
    tmp = format(sum, '#010b')
    if tmp == '0b11111111':
        print("Successful transmission")
    else:
        print("Corrupted Data")


# def update_table(message, checksum) : Function to print the table


output = []
checksum_list = []


def update_table(message, checksum):
    output_message = []
    tmp = 0
    for itr in range(0, len(message)):
        tmp = format(message[itr], '#010b')
        output_message.append(tmp)
    output.append(output_message)
    checksum_list.append(bin(checksum))


# def message_table() : constructing a table of messages with their corresponding checksums
def message_table():
    message_one = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    checksum_one = Calculate_Checksum(message_one)
    update_table(message_one, checksum_one)
    # validate_data(message_one,checksum_one)
    message_two = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
    checksum_two = Calculate_Checksum(message_two)
    update_table(message_two, checksum_two)
    message_three = [0b01100101, 0b01100010, 0b00100000, 0b01110011]
    checksum_three = Calculate_Checksum(message_three)
    update_table(message_three, checksum_three)


# output = []
# checksum_list = []
# def message_table():
#     i = 1
#     while i != 0:
#         output_message = []
#         message = []
#         num = 0
#         tmp = 0
#         print("Enter the message")
#
#         for index in range(0,4):
#             num = int(input(), 2)
#             tmp = format(num, '#010b')
#             output_message.append((tmp))
#             message.append(num)
#         output.append(output_message)
#         # print(message)
#         # print(output_message)
#         check_sum = Calculate_Checksum(message)
#         checksum_list.append(bin(check_sum))
#         print("Press 0 to quit or 1 for next input")
#         i = int(input())

message_table()
# Filling the table as per the template


print("Message\t\t\t\t\t\t\t   Checksum")
for itr in range(0, len(output)):
    print("{} :{}".format(output[itr], checksum_list[itr]))


# Validating the message
message = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
test_message = [0b01101001, 0b00100000, 0b01101100, 0b01101100]
checksum = Calculate_Checksum(message)

validate_data(test_message, checksum)
