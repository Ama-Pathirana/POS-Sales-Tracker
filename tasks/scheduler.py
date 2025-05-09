from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from database import app
from services import summary_service, store_service

def generate_all_hourly_summaries():
    with app.app_context():
        now = datetime.utcnow()
        start_of_hour = now.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
        stores = store_service.Store.query.all()
        for store in stores:
            summary_service.generate_hourly_summary(store.store_id, start_of_hour)
        print(f"Generated hourly sales summaries for {start_of_hour}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_all_hourly_summaries, 'interval', hours=1)
    scheduler.start()

if __name__ == '__main__':
    # This block will run if you execute this file directly (for testing)
    with app.app_context():
        from database import init_db
        init_db()
        # Example: Create a store for testing
        store = store_service.Store(name="Test Store", location="Test Location")
        db.session.add(store)
        db.session.commit()
        generate_all_hourly_summaries()
        print("Hourly summary generation tested.")