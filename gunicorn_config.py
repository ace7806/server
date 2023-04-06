from scripts.scheduler import scheduler

def on_starting(server):
    scheduler.start()
    print('Server has started and background jobs are now scheduled.')
