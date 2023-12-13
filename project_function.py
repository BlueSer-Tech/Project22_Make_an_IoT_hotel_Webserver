import os
import cv2
import random
import math
import datetime
string = "062201002944|233306838|Trần Đăng Huy|17112001|Nam|68/31 Hàm Nghi Tổ 8, Duy Tân, Thành phố Kon Tum, Kon Tum|22112021"
today = datetime.datetime.now()
year= today.year


def format(str):
  str = str[:2] + '/' + str[2:4] + '/' + str[4:]
  return str
def step_list(str):
  list = str.split('|')
  list[3] = format(list[3])
  list[6] = format(list[6])
  for i in range(len(list)):
    if list[i] == '':
      list[i] = None
  return list
def make_folder(directory_name):
    parent_dir = r"C:\Users\Huy\Documents\DATH\face_detect"
    path = os.path.join(parent_dir, directory_name)
    os.mkdir(path)
def count_dir(dir_path):
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a folder
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1
    return count
def count_file(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count
def pin_random():
  ## storing strings in a list
  digits = [i for i in range(0, 10)]
  ## initializing a string
  random_str = ""
  ## we can generate any lenght of string we want
  for i in range(6):
    index = math.floor(random.random() * 10)
    random_str += str(digits[index])
  ## displaying the random string
  return random_str
def list_insert(checkin,checkout,length_of_stay, cccd, fname, birth, gender, email, phone, payment, room_id):
    list_pile = []
    list_pile.append(checkin)
    list_pile.append(checkout)
    list_pile.append(length_of_stay)
    list_pile.append(cccd)
    list_pile.append(fname)
    list_pile.append(birth)
    list_pile.append(gender)
    list_pile.append(email)
    list_pile.append(phone)
    list_pile.append(payment)
    list_pile.append(room_id)
    return list_pile
def calendar_operator(day, month, year, leng_stay):
    year = int(year)
    calendar = {
        "Jan": 31,
        "Feb": 29 if year % 4 == 0 else 28,
        "Mar": 31,
        "Apr": 30,
        "May": 31,
        "Jun": 30,
        "Jul": 31,
        "Aug": 31,
        "Sep": 30,
        "Oct": 31,
        "Nov": 30,
        "Dec": 31
    }
    index = list(calendar).index(month)
    sum_day = int(leng_stay) + int(day)
    while(sum_day > list(calendar.values())[index]):
        print(index)
        sum_day -= list(calendar.values())[index]
        index += 1
        if (index == 12):
            index = 0
            year += 1
    month = list(calendar)[index]
    return str(sum_day)+ " " + month + " " + str(year)

def format_date(string_date):
    list_date = string_date.split()
    month = list_date[1]
    day = list_date[2]
    year = list_date[3]
    return day, month, year
