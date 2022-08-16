from dateutil.rrule import rrule, MO, TU, WE, TH, FR, HOURLY
import pendulum
from prefect.orion.schemas.schedules import RRuleSchedule

bus_hours = rrule(
    freq=HOURLY,
    interval=1,  # i.e. every 1 hour
    # dtstart=pendulum.datetime(2024, 4, 2, 4, 2),
    byweekday=(MO, TU, WE, TH, FR),
    count=42,  # add limit count for testing schedules - remove this line before applying to RRuleSchedule
    byhour=list(range(9, 18)),  # 9 AM to 5 PM
)

for sched_date in bus_hours:
    print(sched_date)

schedule = RRuleSchedule.from_rrule(bus_hours)
print(schedule.rrule)
