import docker
##client = docker.APIClient(base_url='unix://var/run/docker.sock')
client = docker.APIClient(base_url='tcp://10.0.2.15:8080', timeout=5)
pullresult = client.pull("alpine")
listresult = client.containers(all='true')
print(listresult)
