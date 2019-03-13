from locust import HttpLocust, TaskSet, task

class DominiksBehavior(TaskSet):
    @task(1)
    def statusGET(self):
        self.client.get("/status")
        
    @task(2)
    def registryGET(self):
        self.client.get("/registry")
        
    @task(3)
    def registryByNameGET(self):
        self.client.get("/registry/software")
        
    @task(4)
    def registryByNamePOST(self):
        self.client.post("/registry", {"serviceName": "mysystems", "verificationCode": "test"})

class APIUser(HttpLocust):
    task_set = DominiksBehavior
    min_wait = 5000
    max_wait = 9000
