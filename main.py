import schedule
import time

def track_price():
    # Your price tracking logic here
    print("Tracking soil price...")

# Schedule the price tracker to run weekly
schedule.every().week.do(track_price)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)