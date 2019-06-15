# This is an example for Worker and tasks client.

# worker.py

from python3_gearman.worker import GearmanWorker
import os

gm_worker = GearmanWorker(['192.168.122.212:4730'])

def task_listener_reverse(gearman_worker, gearman_job):
    print(str(os.getpid()) + ":Reversing string: " + gearman_job.data)
    import time
    time.sleep(5)
    return gearman_job.data[::-1]


gm_worker.set_client_id("python-worker_"+str(os.getpid()))
gm_worker.register_task("reverse", task_listener_reverse)

gm_worker.work()

# worker.py end
