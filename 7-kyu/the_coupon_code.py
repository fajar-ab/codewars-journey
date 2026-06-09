# Rank  : 7 kyu
# Title : The Coupon Code
# Link  : https://www.codewars.com/kata/539de388a540db7fec000642

from datetime import datetime


def check_coupon(
    entered_code, correct_code, current_date: str, expiration_date: str
) -> bool:
    return all(
        [
            entered_code == correct_code and type(entered_code) is type(correct_code),
            datetime.strptime(current_date, "%B %d, %Y")
            <= datetime.strptime(expiration_date, "%B %d, %Y"),
        ]
    )


check_coupon("123", "123", "September 5, 2014", "October 1, 2014")
