from asyncio import log
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        '''
        The start script for each user - this order is important
        '''
        # Below 3 lines work fine - we get the csrftoken and put it in the header successfully
        response = self.client.get("/api-auth/login/")
        self.csrftoken = response.cookies['csrftoken']
        self.headers = {'X-CSRFToken': self.csrftoken}

        # Now login with username and password as POST
        r1 = self.login()
        return r1

    def login(self):
        # admin login  and retrieving it's access token

        udata = {'username': 'mhmd', 'password': '1234', 'csrfmiddlewaretoken': self.csrftoken}
        cookies = self.client.cookies.get_dict()
        #csrftoken cookie does exist, sessionid does not yet.
        log.info("Current cookies in Login:" + str(self.client.cookies))
        # This next line should come back with a sessionid 
        # from Django - but it does not.
        response = self.client.post("/api-auth/login/",
                                    data=udata,
                                    headers=self.headers)
        log.info("Response from client.post="+str(response)) #OK
        log.info("Response status code:" + str(response.status_code))
        log.info("Response text=" + response.text)
        # Next line does not contain sessionid or Set-Cookie 
        log.info("Headers from post/accts/login = " + str(response.headers)) 


    @task
    def get_todo_items(self):
        self.client.get("/todo/api/task/")
    
