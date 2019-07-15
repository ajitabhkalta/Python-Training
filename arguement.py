import sys 
print(len(sys.argv))
print(f"file name:{sys.argv[0]}")
ip_address=sys.argv[1]
port_num=sys.argv[2]
print(f"Connecting to your machine via {ip_address} with port {port_num}")
print("\nConnected")