from models.event import *
import datetime

event1 = Event(datetime.date(2023, 5,25), "Jessica", 6, "Outside Bar", "Birthday party")
event2 = Event(datetime.date(2023, 3, 7), "Alvin", 12, "Outside Bar", "Birthday party")
event3 = Event(datetime.date(2023, 1, 5), "Amy + Ben", 16, "Dining Room", "Wedding aniversary")

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)