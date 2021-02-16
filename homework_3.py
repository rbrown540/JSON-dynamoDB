# 
# 
# 
# 

import boto3
import json
import decimal
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr


def create_dyno_table():
    """   """    
    dyno_table = dynamodb.create_table(
        TableName = 'Courses',
        KeySchema = [
            {
                'AttributeName': 'CourseID',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'CourseID',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits': 20,
            'WriteCapacityUnits': 20
        })
    return dyno_table


def fill_dyno_table(table_in):
    """   """
    table_to_fill = dynamodb.Table(table_in)
    
    with table_to_fill.batch_writer() as table_batch:
        
        table_batch.put_item(
            Item = {
                "CourseID": 100,
                "CatalogNbr": 17254,
                "NumberCredits": 1,
                "Subject": "Zero Training",
                "Title": "Advanced Officer Training"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 200,
                "CatalogNbr": 35645,
                "NumberCredits": 3,
                "Subject": "Lower Mafia Training",
                "Title": "Advanced Soldier Training"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 300,
                "CatalogNbr": 43651,
                "NumberCredits": 3,
                "Subject": "Workhorse Training",
                "Title": "Advanced NCO Training"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 400,
                "CatalogNbr": 56872,
                "NumberCredits": 3,
                "Subject": "Old Gray Dog Training",
                "Title": "Advanced Senior NCO Training"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 101,
                "CatalogNbr": 19654,
                "NumberCredits": 1,
                "Subject": "Zero Training",
                "Title": "Drop Zone Key location management"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 102,
                "CatalogNbr": 14692,
                "NumberCredits": 1,
                "Subject": "Zero Training",
                "Title": "Basic ID 10 Tango appropriation"
            })

        table_batch.put_item(
            Item = {
                "CourseID": 201,
                "CatalogNbr": 35649,
                "NumberCredits": 3,
                "Subject": "Lower Mafia Training",
                "Title": "Introduction to Soft Armor Checks"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 202,
                "CatalogNbr": 39645,
                "NumberCredits": 3,
                "Subject": "Lower Mafia Training",
                "Title": "Vehicle Exhaust Sample Collection procedures"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 301,
                "CatalogNbr": 49631,
                "NumberCredits": 3,
                "Subject": "Workhorse Training",
                "Title": "Proper Communication through Prickie-6"
            })
        
        table_batch.put_item(
            Item = {
                "CourseID": 401,
                "CatalogNbr": 59321,
                "NumberCredits": 3,
                "Subject": "Old Gray Dog Training",
                "Title": "Bravo Alpha Eleven Double Zero November chasing"
            })


def user_search(table_in):
    table = dynamodb.Table(table_in)
    try:
        user_subject = input('Please provide the course Subject: \n\t>>  ').title()
        if(user_subject == ''):
            print('Try again with correct information')
            user_subject = input('Please provide the course Subject: \n\t>>  ').title()
        
        user_catalogNbr = int(input('Please provide the course Catalog Number: \n\t>>  '))
        if(user_catalogNbr == ' '):
            user_catalogNbr = int(input('Please provide the course Catalog Number: \n\t>>  '))
        
    except ValueError as in_e1:
        print('Try again by providing correct information')
        user_catalogNbr = int(input('Please provide the course Catalog Number: \n\t>>  '))
    
    response = table.scan(FilterExpression = Attr('Subject').eq(user_subject) & Attr('CatalogNbr').eq(user_catalogNbr))
    items = response['Items']
    
    for i in items:
        print('The title of that course is:\n\t', i['Title'], '\n\n')
    user_menu()


def user_menu():
    """ """
    try:
        user_y_n = input('Would you like to search for a class? (Y or N):\n\t  ').title()
        while (user_y_n != 'N'):
            user_search('Courses')
    except ValueError as in_e:
        print('Nope, try again')
        user_menu()


    exit(0)


# create_dyno_table()
# fill_dyno_table('Courses')
# user_search('Courses')
user_menu()
