from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from scripts.update_gas_prices import update_todays_prices

def gas_price_update_job():
    # with app.app_context():
    update_todays_prices()
    print('Gas price update job has been executed')
gas_price_update_job()
scheduler = BackgroundScheduler()
scheduler.add_job(gas_price_update_job, 'interval', days=1)
scheduler.start()