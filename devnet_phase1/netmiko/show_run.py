from netmiko import ConnectHandler

device = {
  "device_type": "cisco_nexus",
  "host": "x.x.x.x",
  "username": "admin",
  "password": "cisco",
}

connect = ConnectHandler(device)
output = connect.send_command("sh run")
connect.disconnect()

with open("filepath" , "w") as file:
  file.write(output)
  
print("Running config saved")

