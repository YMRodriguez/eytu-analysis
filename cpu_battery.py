import psutil
import os
import pathlib
import json
import time
from datetime import date
import os
from multiprocessing import Process

# -------- Data gathering -----------------
pathlib.Path(os.path.dirname(__file__) + os.path.sep +
             'data').mkdir(parents=True, exist_ok=True)


def sampleTempAndFan():
    os.system(
        "sudo powermetrics -i 1000 -n 1200 -o ." + os.path.sep + "data" + os.path.sep + "powermetrics.txt --samplers smc")


def samplePs():
    dataset = []
    for i in range(1200):
        sample = {}
        sample["date"] = time.strftime("%H: %M: %S")
        sample["phy_cores"] = psutil.cpu_count(logical=False)
        sample["log_cores"] = psutil.cpu_count(logical=True)
        sample["min_freq"] = psutil.cpu_freq().min
        sample["max_freq"] = psutil.cpu_freq().max
        sample["cur_freq"] = psutil.cpu_freq().current
        sample["pids"] = len(psutil.pids())
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            sample["core_" + str(i) +
                   "_percentage"] = round(percentage/100, 3)
        sample["battery"] = psutil.sensors_battery().percent
        sample["tot_usage"] = round(psutil.cpu_percent()/100, 3)
        dataset.append(sample)
        # Take a sample each half a second.
    with open(os.path.dirname(__file__) + os.path.sep + "data" + os.path.sep + "logs.json", 'w+') as file:
        json.dump(dataset, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    p1 = Process(target=sampleTempAndFan)
    p2 = Process(target=samplePs)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
