import psutil

curr_sent=0
curr_recv=0

prev_sent=0
prev_recv=0

while True:
    cpu_p=psutil.cpu_percent(interval=1)
    print(f"cpu : {cpu_p}%")

    memory=psutil.virtual_memory()
    memory_total=round(memory.total/1024**3)
    print(f'memory : {memory_total}GB')

    net=psutil.net_io_counters()
    curr_sent=round(net.bytes_sent/1024**2,1)
    curr_recv=round(net.bytes_recv/1024**2,1)

    sent=round(curr_sent-prev_sent,1)
    recv=round(curr_recv-prev_recv,1)
    
    print(f'send : {sent}MB  recieve : {recv}MB')

    prev_sent=curr_sent
    prev_recv=curr_recv
