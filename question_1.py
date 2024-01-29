from datetime import datetime
from time import sleep

class RateLimiter:
    """This class is used for api throtling concept"""
    def __init__(self):
        self.default_time_int = 2
        self.max_request = 20
        self.total_num_req_maper = {}
        self.last_hit_time_maper = {}
        self.max_waiting_seconds = 2
    
    def check_num_of_request_in_default_time(self,ip_address):
        
        if ip_address in self.total_num_req_maper:
            total_req = self.total_num_req_maper[ip_address]
            total_sec = (datetime.now() - self.last_hit_time_maper[ip_address]).total_seconds()
            print(total_req, total_sec)

            if total_sec < self.default_time_int and total_req <= self.max_request:
                self.total_num_req_maper[ip_address] = self.total_num_req_maper[ip_address]+1
                return True
            
            elif total_sec >= self.default_time_int and total_req <= self.max_request:
                self.last_hit_time_maper[ip_address] = datetime.now()
                self.total_num_req_maper[ip_address] = 1
                return True

            else:

                if total_sec-self.default_time_int >= self.max_waiting_seconds:
                    self.last_hit_time_maper[ip_address] = datetime.now()
                    self.total_num_req_maper[ip_address] = 1
                    return True

                return False
        else:
            self.total_num_req_maper[ip_address] = 1
            self.last_hit_time_maper[ip_address] = datetime.now()
            return True
    
    def isAllowed(self,ip_address:int):
        if self.check_num_of_request_in_default_time(ip_address):
            return "request under limit"
        else:
            return "request over limit"
            
obj = RateLimiter()
for i in range(250):
    #sleep(1)
    if i%50 == 0:
        sleep(1)
    print(obj.isAllowed(1))
