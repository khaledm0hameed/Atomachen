from plyer import notification
from googlesearch import search

query = "سعر سهم فوري الان"

for result in search(query, num_results=10):
    title = "سهم فاوري "
message = f"سعر السهم الواحد{result}"



notification.notify(title=title, message=message)
