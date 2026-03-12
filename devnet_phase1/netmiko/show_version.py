from netmiko import ConnectHandler

device = {
  "device_type": "cisco_ios",
  "host": "x.x.x.x",
  "username": "admin",
  "password": "cisco",
}

connection = ConnectHandler(##deviceIP)
output = connection.send_command("sho ver")
print(output)
connection.disconnect()

