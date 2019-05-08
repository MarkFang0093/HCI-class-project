import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
int_encode = b'2'
float_encode = b'42.3'


string1 = "Hello!"
string1_encode = string1.encode()

int1 = 5
int1_encode = b'%d' %int1  # you need to change %d based on the type your variable
userinput = 0

#c = int(1,10)

ser.write(b'1')

print('messeged')

while 1:
    print('Enter your mode:')
    

    inkey = raw_input()
    if inkey == "2":
        ser.write(b'2')
    elif inkey == "3":
        ser.write(b'3')
    elif inkey == "4":
        ser.write(b'4')
    elif inkey == "5":
        ser.write(b'5')
    elif inkey == "6":
        ser.write(b'6')
    elif inkey == "7":
        ser.write(b'7')



        #if(ser.in_waiting >0):
                #line = ser.readline()
                #print(line)

               # ser.write(b'1')
               # ser.write(b'5')
                #ser.write(b'7')
