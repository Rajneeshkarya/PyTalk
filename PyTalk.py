import argparse
import socket
from colorama import Fore
import textwrap

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
def main():

	parser = argparse.ArgumentParser(description=Fore.BLUE+'---Chat by Rajneesh Kumar Arya---',formatter_class=argparse.ArgumentDefaultsHelpFormatter,epilog=textwrap.dedent('''
	Example -

	chat.py -j -i <IP_ADDR> -p <PORT>
	chat.py -c -p <port> -pwd <password>
	'''))

	parser.add_argument('-i','--ip',help='Specify Server ip address',default='0.0.0.0')
	parser.add_argument('-p','--port',help='Specify the port',default='4444',type=int)
	parser.add_argument('-pwd','--password',help='Set a password for Room')
	parser.add_argument('-j','--join',action='store_true',help='To Join the Room')
	parser.add_argument('-c','--create',action='store_true',help='To Create a Room')
	args = parser.parse_args()

	if args.join:
		sock.connect((args.ip,args.port))
		response = sock.recv(1024)

		name = input(Fore.RED+f'{response.decode()}')
		name = name.encode()
		sock.send(name)

		serv_name = sock.recv(1024)
		print(Fore.BLUE + f'Connected with {serv_name.decode()}')
		if args.password==None:
			pswd = input(Fore.GREEN+'Password :')
			pswd = pswd.encode()
		else:
			pswd = args.password
			pswd = pswd.encode()
			
		sock.send(pswd)

		verify = sock.recv(1024)
		if verify.decode() == '1':
			print("Start Chatting...")
			while(True):
				buffer = input(Fore.GREEN + f"You({name.decode()}) : ")
				check = buffer
				buffer = buffer.encode()
				sock.send(buffer)
				if "bye" in check:
					exit()

				data = sock.recv(1024)
				print(Fore.BLUE + f'\t\t\t\t\t{serv_name.decode()} : {data.decode()}')
				if "bye" in data.decode():
					exit()
		else:
			print(Fore.RED + 'Invalid Password')
			exit()	
	elif args.create:
		sock.bind((args.ip,args.port))
		s_name = input(Fore.RED + "Enter your name : ")
		s_name = s_name.encode()
		sock.listen(2)
		print(Fore.CYAN + 'Waiting for connection : ')
        
		client,addr = sock.accept()
		client.send(b"Enter your name : ")
		cli_name = client.recv(1024)
		client.send(s_name)
		token = client.recv(1024)
		if token.decode() == args.password:
			client.send(b'1')
			print(Fore.BLUE + f"Connected with {cli_name.decode()} on {addr[0]}")
			print(Fore.GREEN + "Start Chatting...")
			while(True):
				data = client.recv(1024)
				print(Fore.BLUE + f"\t\t\t\t\t{cli_name.decode()} : {data.decode()}")
				buffer = input(Fore.GREEN + f"You({s_name.decode()}) : ")
				check = buffer
				buffer = buffer.encode()
				client.send(buffer)
				if "bye" in check:
					exit()
		else:
			client.send(b'0')

if __name__ == '__main__':
	main()
