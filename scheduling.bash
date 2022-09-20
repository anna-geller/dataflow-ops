# Set schedule directly during build
# run healthcheck flow every minute:
prefect deployment build -n prod -q prod -a flows/healthcheck.py:healthcheck --interval 60

# hourly 9 to 5 during business days (Mon to Fri)
prefect deployment build -n prod -q prod -a flows/parametrized.py:parametrized --cron "0 9-17 * * 1-5"

# daily at 9 AM but only for the next 7 days (e.g. some campaign)
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'

# only during business hours
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule "FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"

# ---------------------------------------------------------------
# Set schedule in a separate command after build
prefect deployment set-schedule parametrized/prod --interval 300
prefect deployment set-schedule parametrized/prod --cron "*/1 * * * *"  # UTC
prefect deployment set-schedule parametrized/prod --cron '15 20 * * WED' --timezone 'Europe/Berlin'
prefect deployment set-schedule healthcheck/prod --timezone 'Europe/Berlin' --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'
# ---------------------------------------------------------------
# rrule without and with a timezone
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"}'
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17", "timezone": "Europe/Berlin"}'
