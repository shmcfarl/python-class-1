# Take input
network = raw_input("Enter a network: ")

#Split each element as an octet in the list
network = network.split(".")

# len is 3 then we are right length if 4 then drop the last octet
if len(network) == 3:
  pass 
elif len(network) == 4:
  network.pop()

print network

network_list = []

# use each octet with period in between - string conctination
base_ip = network[0] + '.' + network[1] + '.' + network[2] + '.'
print base_ip

# base_ip + str(i) is our actual IP address loop for all 254 elements
for i in range(255):
  if i != 0:
     network_list.append(base_ip + str(i))


