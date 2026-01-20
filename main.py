import psutil

cpu = psutil.cpu_percent(interval= 1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent


print(f'Uso de CPU: {cpu}')
print(f'Uso de Memoria RAM {memory}')
print(f'Uso de Disko: {disk}')
