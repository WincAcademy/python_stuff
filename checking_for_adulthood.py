from datetime import date


def date_is_more_than_18_years_ago(given_date):
    vandaag = date.today()

    if vandaag.year - given_date.year > 18:
        return True
    elif vandaag.year - given_date.year < 18:
        return False

    if vandaag.month > given_date.month:
        return True
    elif vandaag.month < given_date.month:
        return False

    return vandaag.day >= given_date.day


print("----We doen iets")
assert date_is_more_than_18_years_ago(date(1981, 7, 16))
assert date_is_more_than_18_years_ago(date(2002, 4, 29))
assert date_is_more_than_18_years_ago(date(2002, 4, 30))
assert not date_is_more_than_18_years_ago(date(2002, 5, 1))
assert not date_is_more_than_18_years_ago(date(2015, 11, 9))
print("----We zijn klaar")
