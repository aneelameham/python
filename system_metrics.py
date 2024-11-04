import csv
import psutil
import datetime


with open(r'names.csv', 'a', newline='') as csvfile:
    fieldnames = ['timestamp', 'cpu', 'mem']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    metrics = []
    metrics.append(datetime.datetime.now())
    metrics.append(psutil.cpu_percent(interval=1, percpu=False))
    metrics.append(psutil.virtual_memory().available)
    writer.writerow(dict(zip(fieldnames, metrics)))
