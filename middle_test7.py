import time
fseconds=time.time()
total_sec=int(fseconds)
total_min=total_sec//60
minute=total_min%60
total_hour=total_min//60
hour=total_min//60%60
print(str(hour),str(minute))
