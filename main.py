import twint
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 1, 13)
end_date = date(2022, 1, 13)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))

    # Configure
    c = twint.Config()
    keyword = 'vaksin'
    c.Search = keyword # masukkan kata kunci

    c.Since = single_date.strftime("%Y-%m-%d") + ' 00:00:00'
    c.Until = single_date.strftime("%Y-%m-%d") + ' 23:59:59'  
    c.Store_csv = True
    c.Output = single_date.strftime("%Y-%m-%d") +".csv"
    c.Hide_output = True

    # Run
    twint.run.Search(c)
