#!/usr/bin/env python3

def birthState(presidentname):
   presidentBirthPlace = {
     'Barack Hussein Obama II':'Hawaii',
     'George Walker Bush':'Connecticut',
     'William Jefferson Clinton':'Arkansas',
     'George Herbert Walker Bush':'Massachussetts',
     'Ronald Wilson Reagan':'Illinois',
     'James Earl Carter, Jr':'Georgia'
   }

   if presidentname in presidentBirthPlace:
     return presidentBirthPlace[presidentname]
   else:
     return "Birth Place Does not Exist"


def dayOfTheWeek():
   days = {
     'Mo': 'Monday',
     'Tu': 'Tuesday',
     'We': 'Wednesday'
   }
   print(days)
   moreDays = {'Sa': 'Saturday','Su': 'Sunday'}
   days.update(moreDays)
   print(days)
   days.pop('Tu')
   print(days)
   keys = days.keys()
   print(keys)

   for key in days.keys():
       print(key, end=' ')

   for value in days.values():
       print(value, end=' ')


def freqConter(lstObj):
    print("\nNew Operation\n-------------------")
    print(lstObj)
    frqc = {}
    for newItem in lstObj:
        if newItem in frqc:
           frqc[newItem] += 1
        else:
           frqc[newItem] = 1

    print(frqc)


if __name__ == '__main__':
   print(birthState('Ronald Wilson Reagan'))
   print(birthState('Willy Mays'))
   dayOfTheWeek()
   students = ['Cindy','John','Cindy','Adam','Adam','Jimmy','Joan','Cindy','Joan','Uche']
   freqConter(students)

