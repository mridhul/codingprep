#Write a Python script to read an Nginx log file and count the occurrences of each HTTP status code.
import json


def count_http_status(logfile):
    status_counter = {
        200:0,
        404:0,
        403:0
    }
    with open(logfile,'r') as data:
        logs = json.load(data)
        for line in logs:
            status_code = int(line.get('status', 0))
            if status_code in status_counter:
                status_counter[status_code]+=1

    return status_counter





#Count status
log_file = "./nginx_logs.json"
print(count_http_status(log_file))
