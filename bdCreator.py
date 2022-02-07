import sqlite3
import colorama
from colorama import Fore, Back, Style

def tables_check():
    #создаем базу данных
    print(Fore.BLUE + "Создание БД...." + " \n")
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    print(Fore.BLUE + "Создание таблицы с юзерами" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, mail TEXT UNIQUE, user_name TEXT, date_of_birth DATE, sex BOOLEAN, horoscope_sign INTEGER)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с аффирмациями" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Affirmations (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, text TEXT, picture BLOB)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с показанными аффирмациями" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Affirmations_shown (user_id INTEGER PRIMARY KEY, affirm_id INTEGER)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с квадратом пифагора" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS pifagor_square (num INTEGER, num_count INTEGER, text TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")

    # 1 - capricorn
    # 2 - taurus
    # 3 - virgo
    # 4 - aquarius
    # 5 - gemini
    # 6 - libra
    # 7 - pisces
    # 8 - cancer
    # 9 - scorpio
    # 10 - aries
    # 11 - leo
    # 12 - sagittarius

    print(Fore.BLUE + "Создание таблицы с гороскопами today" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS today_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами next_day" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS next_day_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами week" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS week_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами month" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS month_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами year" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS year_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")

    print(Fore.BLUE + "Создание таблицы с гороскопами характеристика" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS character_horoscopes (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, charact TEXT, love TEXT, career TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    #создали