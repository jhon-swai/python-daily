# Horoscope program

# Pseudocode
# Loop to get user input
# function to determine the horoscope based on their zodiac sign
# function to determine the zodiac sign

import datetime
# Aries - March 21 to April 19
# Taurus - April 20 - May 20
# Gemini - May 21 - June 21
# Cancer - June 21 - July 22
# Leo - July 23 -August 22
# Virgo - August 23 - September 22
# Libra - September 23 - October 22
# Scorpio - October 23 - November 21
# Sagittarius - November 22 - December 21
# Capricorn - December 22 - January 19
# Aquarius - January 20 - February 18
# Pisces - February 19- March 20

def zodiacSign(day, month):
    if( (month == 1 and day <= 19 ) or (month == 12 and day >= 22) ):
        return 'Capricorn'
    elif( (month == 1 and day >= 20 ) or ( month == 2 and day <= 18) ):
        return 'Aquarius'
    elif ( (month ==2 and day >= 19 ) or (month == 3 and day <= 20) ):
        return 'Pisces'
    elif ( (month == 3 and day >= 21 ) or (month == 4 and day <= 19 ) ):
        return 'Aries'
    elif ( (month == 4 and day >= 20 ) or (month == 5 and day <= 20) ):
        return 'Taurus'
    elif ( (month == 5 and day >= 21 ) or (month == 6 and day <= 21) ):
        return 'Gemini'
    elif ( (month == 6 and day >= 21 ) or (month == 7 and day <= 21) ):
        return 'Cancer'
    elif ( (month == 7 and day >= 23 ) or (month == 8 and day <= 22) ):
        return 'Leo'
    elif ( (month == 8 and day >= 23 ) or (month == 9 and day <= 22) ):
        return 'Virgo'
    elif ( (month == 9 and day >= 23 ) or (month == 10 and day <= 22) ):
        return 'Libra'
    elif ( (month == 10 and day >= 23 ) or (month == 11 and day <= 21) ):
        return 'Scorpio'
    elif ( (month == 11 and day >= 22 ) or (month == 12 and day <= 21) ):
        return 'Sagittarius'

def yesOrNo(answer):
    if(answer.lower() == 'yes' or answer.lower() == 'y'):
        return True
    else:
        return false

def monthDay():
    print('Do you want to know your zodiac sign: ', end="")
    answer = input()
    if(yesOrNo(answer)):
        print('Enter your month of birth: ', end='')
        month = input()
        print('Enter day of the month: ', end='')
        day = input()
        year = datetime.datetime.now().year
        try:
            xDate = datetime.datetime(year,int(month), int(day))
            return xDate
        except NameError:
            print('Wrong input, lets do this again')
            monthDay()
    else:
        return null
xDate = monthDay()
zSign = zodiacSign(xDate.day , xDate.month)
# zSign = zodiacSign(2, 1)
print(type(zSign))

print('Your are ' + zSign)
