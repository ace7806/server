from apscheduler.schedulers.background import BackgroundScheduler
from scripts.update_gas_prices import update_todays_prices

def gas_price_update_job():
    update_todays_prices()
    print('Gas price update job has been executed')
scheduler = BackgroundScheduler()
scheduler.add_job(gas_price_update_job, 'interval', 
                  days=1)
