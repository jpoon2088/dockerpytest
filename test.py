import docker
##client = docker.APIClient(base_url='unix://var/run/docker.sock')
client = docker.APIClient(base_url='tcp://127.0.0.1:80', timeout=5)
pullresult = client.pull("alpine")
listresult = client.containers(all='true')
print(listresult)
