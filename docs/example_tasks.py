# tasks.py
# example client that issues a set of tasks for the server and get's a response back

from python3_gearman.client import GearmanClient
from pprint import pprint

def check_request_status(job_request):
    if job_request.complete:
        print("job %s finished! Result:%s - %s" % (job_request.job.unique, job_request.state, job_request.result))
    elif job_request.timed_out:
        print("Job %s timed out!" % job_request.unique)
    elif job_request.state == JOB_UNKNOWN:
        print("Job %s connection failed!" % job_request.unique)

data = []

gm_client = GearmanClient(["192.168.122.212:4730"])

def completed(task, context):
    if context == 'reverse':
        print("Reversed the thing")
        data = data + task.data()
    if context == 'cast':
        print("Should not be here")
        return "CAST"


jobs = []
jobs.append({'task':"reverse", 'data':"Hello God!"})
jobs.append({'task':"reverse", 'data':"Hello World!"})
jobs.append({ 'task':"reverse", 'data':"Happy Days!"})
for i in range(1,10):
    jobs.append({ 'task':"reverse", 'data':"Happy Day " + str(i) + "!"})

results = gm_client.submit_multiple_jobs(jobs_to_submit=jobs)
for result in results:
    check_request_status(result)
#pprint(result)
