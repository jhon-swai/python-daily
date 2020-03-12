# Horoscope program

# Pseudocode
# Loop to get user input
# function to determine the horoscope based on their zodiac sign
# function to determine the zodiac sign
import datetime
Aries - March 21 to April 19
Taurus - April 20 - May 20
Gemini - May 21 - June 21
Cancer - June 21 - July 22
Leo - July 23 -August 22
Virgo - August 23 - September 22
Libra - September 23 - October 22
Scorpio - October 23 - November 21
Sagittarius - November 22 - December 21
Capricorn - December 22 - January 19
Aquarius - January 20 - February 18
Pisces - February 19- March 20

def zodiacSign(day, month):
    if((month == 1 and day < = 19 ) or (month == 12 and day >= 22 ):
        return 'Capricorn'
    elif( (month == 1 and day >= 20 ) or ( month == 2 and day <= 18) ):
        return 'Aquarius'
    elif ( (month ==2 and day >= 19 ) or (month == 3 and day <= 20) ):
        return 'Pisces'
    elif ( (month == 3 and day >= 21 ) or (month == 4 and day <= 19 ) ):
        return 'Aries'
    elif ( (month ==  and day) or (month == and day ) ):
        return






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
            xDate = datetime.datetime(year,month, day)
        except NameError:
            print('Wrong input, lets do this again')
            monthDay()
        return xDate
    else:
        print('Thank you for your time, hit enter to exit')
        input()
