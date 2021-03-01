import os
import json
import multiprocessing
import time
from p2_multi import process_docker
from p2_multi import monitor_ad

sets = []

for d in os.listdir('../data/personas/'):
    part = d.split('.json')[0]

    if(part in ["All","Control"]):
        continue

    if part not in sets:
        sets.append(part)


for s in sets:

    p1 = multiprocessing.Process(target=process_docker, args=(s,5))
    p2 = multiprocessing.Process(target=process_docker, args=(s,10))
    p3 = multiprocessing.Process(target=process_docker, args=(s,15))
    p4 = multiprocessing.Process(target=process_docker, args=(s,20))
    p5 = multiprocessing.Process(target=process_docker, args=(s,25))
    p6 = multiprocessing.Process(target=process_docker, args=(s,30))
    p7 = multiprocessing.Process(target=process_docker, args=(s,35))
    p8 = multiprocessing.Process(target=process_docker, args=(s,40))
    p9 = multiprocessing.Process(target=process_docker, args=(s,45))
    p10 = multiprocessing.Process(target=process_docker, args=(s,50))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    


    b1 = multiprocessing.Process(target=monitor_ad, args=(s,5))
    b2 = multiprocessing.Process(target=monitor_ad, args=(s,10))
    b3 = multiprocessing.Process(target=monitor_ad, args=(s,15))
    b4 = multiprocessing.Process(target=monitor_ad, args=(s,20))
    b5 = multiprocessing.Process(target=monitor_ad, args=(s,25))
    b6 = multiprocessing.Process(target=monitor_ad, args=(s,30))
    b7 = multiprocessing.Process(target=monitor_ad, args=(s,35))
    b8 = multiprocessing.Process(target=monitor_ad, args=(s,40))
    b9 = multiprocessing.Process(target=monitor_ad, args=(s,45))
    b10 = multiprocessing.Process(target=monitor_ad, args=(s,50))

    b1.start()
    b2.start()
    b3.start()
    b4.start()
    b5.start()
    b6.start()
    b7.start()
    b8.start()
    b9.start()
    b10.start()

