from netmiko import ConnectHandler

device = {
  "device_type": "cisco_ios",
  "host": "x.x.x.x",
  "username": "admin",
  "password": "cisco",
}

connection = ConnectHandler(device) #ask why
output = connection.send_command("sh ip int brief")
print(output)
connection.disconnect()

