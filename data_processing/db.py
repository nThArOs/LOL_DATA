import io
import time

import pandas as pd
import psycopg2
from constants import *
from sqlalchemy import create_engine

conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_name)


def Open_Conn():
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_name)
    # cur = conn.cursor()
    return conn
    # print('PostgreSQL database version:')
    # cur.execute('SELECT version()')
    # db_version = cur.fetchone()
    # print(db_version)


def insert_leaderboard(df_leaderboard):
    conn_string = 'postgresql://postgres:postgres@localhost/postgres'
    db = create_engine(conn_string)
    start_time = time.time()
    conn = psycopg2.connect(conn_string)
    df_leaderboard.to_sql('leaderboard1', con=db, if_exists='replace', index=False)

    # conn.autocommit = True
    # cursor = conn.cursor()

    conn.close()
    print("COPY duration: {} seconds".format(time.time() - start_time))


def get_db_leaderboard():
    conn_string = 'postgresql://postgres:postgres@localhost/postgres'
    db = create_engine(conn_string)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query = """Select "summonerId" from public.leaderboard1"""
    cursor.execute(query)
    leaderboard_summoner = cursor.fetchall()
    query_name = """Select "summonerName" from public.leaderboard1"""
    cursor.execute(query_name)
    leaderboard_summonerName = cursor.fetchall()
    cursor.close()
    conn.close()
    return leaderboard_summoner,leaderboard_summonerName

def insert_db_puuid_csv():
    conn_string = 'postgresql://postgres:postgres@localhost/postgres'
    db = create_engine(conn_string)
    start_time = time.time()
    conn = psycopg2.connect(conn_string)
    df_puuid = pd.read_csv('summoner_puuid.csv')
    df_puuid.to_sql('user_puuid', con=db, if_exists='replace', index=False)
    # conn.autocommit = True
    # cursor = conn.cursor()
    conn.close()
    print("COPY duration: {} seconds".format(time.time() - start_time))

def get_db_puuid():
    conn_string = 'postgresql://postgres:postgres@localhost/postgres'
    db = create_engine(conn_string)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query = """Select "puuid" from public.user_puuid"""
    cursor.execute(query)
    list_puuid = cursor.fetchall()
    query_name = """Select "name" from public.user_puuid"""
    cursor.execute(query_name)
    leaderboard_summonerName = cursor.fetchall()
    cursor.close()
    conn.close()
    return list_puuid, leaderboard_summonerName