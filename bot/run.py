from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='GBP')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date="2025-05-16",
                     check_out_date='2025-05-23')
    bot.select_adults()
     




