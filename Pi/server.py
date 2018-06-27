import socket
from socket import error as SocketError
import RPi.GPIO as GPIO
import time
import errno
led1 = 18
led2 = 17
led3 = 19
#set numbering mode for the program
GPIO.setmode(GPIO.BCM)
#setup led(pin 8) as output pin
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)


def Main():
    host = "192.168.43.250" #ip address of your rapberry Pi use ifconfig to find ip
    port = 9345
    try:
        mySocket = socket.socket()
        mySocket.bind((host,port))

        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        while True:
                data = conn.recv(1024).decode()
                if data == "on_led1":
                        GPIO.output(led1,GPIO.HIGH)
                elif data == "off_led1":
                        GPIO.output(led1,GPIO.LOW)
                if data == "on_led2":
                        GPIO.output(led2,GPIO.HIGH)
                elif data == "off_led2":
                        GPIO.output(led2,GPIO.LOW)
                if data == "on_led3":
                        GPIO.output(led3,GPIO.HIGH)
                elif data == "off_led3":
                        GPIO.output(led3,GPIO.LOW)
                if data == "close_all":
                        GPIO.output(led1,GPIO.LOW)
                        GPIO.output(led2,GPIO.LOW)
                        GPIO.output(led3,GPIO.LOW)


                if not data:
                    print("waiting for client")
                    conn, addr = mySocket.accept()
                    print ("Connection from: " + str(addr))
                else:
                    print ("from connected  user: " + str(data))
                    data = str(data).upper()
                    print ("sending: " + str(data))
                    #conn.send(data.encode())
    except SocketError as e:
        print (e)
        if e.errno != errno.ECONNRESET:
            raise
        data = ""

    finally:
        conn.close()
        GPIO.output(led1,GPIO.LOW)
        GPIO.output(led1,GPIO.LOW)
        GPIO.output(led1,GPIO.LOW)


if __name__ == '__main__':
    Main()
