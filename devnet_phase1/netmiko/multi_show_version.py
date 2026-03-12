from netmiko import ConnectHandler
from devices import devices

for device in devices:
  
  print(f"connecting to {device['host']}")
  
  connection = ConnectHandler(**device)
  
  output = connection.send_command("sh ver")
  
  print(output)
  
  connection.disconnect()

