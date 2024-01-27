from gdacs.api import GDACSAPIReader

client = GDACSAPIReader()

# Get all alerts
events = client.latest_events()
events_dict = dict(events)
print(events_dict['features'][0])