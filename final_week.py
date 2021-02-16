# 
# 
# 
# 
# 
# import my_package
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# database resource
dynamodb = boto3.resource('dynamodb')
s3r = boto3.resource('s3')
s3c = boto3.client('s3')


def user_menu():
    print('\n\n\t1: View Group Schedule\n',
          '\t2: Register for Group Class\n',
          '\t3: Unregister for Group Class\n',
          '\t4: Download Group Schedule\n',
          '\t5: Body Mass Index Calculator\n',
          '\t6: Upload Exercise Photo for Social Media Posting\n',
          '\t0: Exit')
     
    try:
        user_selection = int(input('\n Please enter your menu selection:\n\t>>>>  '))
    except ValueError as in_e:
        print('TRY SOMETHING ELSE, LIKE FOLLOWING INSTRUCTIONS,\n'
              'OR SIMPLY PICKING A NUMBER FROM THE LIST!\n', in_e)
        user_menu()
                               
    while user_selection != 0:
        
        if user_selection == 1:
            view_schedule()
        elif user_selection == 2:
            register_class()
        elif user_selection == 3:
            unregister_class()
        elif user_selection == 4:
            download_schedule()
        elif user_selection == 5:
            bmi_index()
        elif user_selection == 6:
            upload_photo()
        else:
            print('\nNOPE!!\nselect a NUMBER from THIS menu')
            user_menu()
    print('ZERO')
    

def view_schedule():
    """ """
    bucket = 'richard.w.brown420'

    s3 = boto3.resource('s3')
    group_String = 'group_schedule.json'
    s3.Bucket(bucket).download_file('group_schedule.json', group_String)
    
    with open(group_String) as f:
        print(f.read())
        user_menu()


def register_class():
    """ """
    print ('\nPlease choose which class you want to register for:\n',
                                     '\t1: Spin Cycle with Jesse\n',
                                     '\t2: Rock Solid\n',
                                     '\t3: Yoga Chill\n',
                                     '\t4: More Jesse Spin\n',
                                     '\t0: Return to main menu\n')
    try:                                 
        user_register_choice = int(input('\t>>> '))
    except ValueError as e:
        print('NO SIR, make a valid selection!!!\n', e)
        register_class()
        
    while user_register_choice != 0:
        if user_register_choice == 1:
            table = dynamodb.Table('SpinCycleWithJesse')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
                user_first = input('\nPlease provide the first name on the account\n\t >>>  ')
                user_last = input('\nPlease provide the last name on the account\n\t >>>  ')
            except ValueError as e:
                print('NOPE', e)
            with table.batch_writer() as table_writing:
                table_writing.put_item(
                    Item = {
                        "PhoneNumber": user_phone,
                        "FirstName": user_first,
                        "LastName": user_last
                    })
            print('\nNOPE!!')
            register_class()
            
        elif user_register_choice == 2:
            table = dynamodb.Table('RockSolid')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
                user_first = input('\nPlease provide the first name on the account\n\t >>>  ')
                user_last = input('\nPlease provide the last name on the account\n\t >>>  ')
            except ValueError as e:
                print('NOPE\nselect a NUMBER from THIS menu', e)
                
            with table.batch_writer() as table_writing:
                table_writing.put_item(
                    Item = {
                        "PhoneNumber": user_phone,
                        "FirstName": user_first,
                        "LastName": user_last
                    })
            register_class()
            
        elif user_register_choice == 3:
            table = dynamodb.Table('YogaChill')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
                user_first = input('\nPlease provide the first name on the account\n\t >>>  ')
                user_last = input('\nPlease provide the last name on the account\n\t >>>  ')
            except ValueError as e:
                print('That is not correct', e)

            with table.batch_writer() as table_writing:
                table_writing.put_item(
                    Item = {
                        "PhoneNumber": user_phone,
                        "FirstName": user_first,
                        "LastName": user_last
                    })
            register_class()
            
        elif user_register_choice == 4:
            table = dynamodb.Table('MoreJesseSpin')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
                user_first = input('\nPlease provide the first name on the account\n\t >>>  ')
                user_last = input('\nPlease provide the last name on the account\n\t >>>  ')
            except ValueError as e:
                print("Let's try again")

            with table.batch_writer() as table_writing:
                table_writing.put_item(
                    Item = {
                        "PhoneNumber": user_phone,
                        "FirstName": user_first,
                        "LastName": user_last
                    })
            register_class()
            
        else: 
            print('\nYou did not choose a valid option from the menu\n')
            register_class()
    user_menu()


def unregister_class():
    """ """
    print('\nPlease choose a class you no longer want to attend:\n',
                                     '\t1: Spin Cycle with Jesse\n',
                                     '\t2: Rock Solid\n',
                                     '\t3: Yoga Chill\n',
                                     '\t4: More Jesse Spin\n',
                                     '\t0: Return to main menu\n')
    try:
        user_unregister_choice = int(input('\t>>> '))
    except ValueError as e:
        print('Ugh, please follow instructions. Start with this...\n', e)
        unregister_class()
                                     
    while user_unregister_choice != 0:
        if user_unregister_choice == 1:
            table = dynamodb.Table('SpinCycleWithJesse')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
            except ValueError as e:
                print('Really?')
                
            table.delete_item(
                Key={
                    'PhoneNumber': user_phone
                })
            unregister_class()
                
        elif user_unregister_choice == 2:
            table = dynamodb.Table('RockSolid')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
            except ValueError as e:
                print('Once more we do this')
                
            table.delete_item(
                Key={
                    'PhoneNumber': user_phone
                })
            unregister_class()
                
        elif user_unregister_choice == 3:
            table = dynamodb.Table('YogaChill')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
            except ValueError as e:
                print('Once more into the breach')

            table.delete_item(
                Key={
                    'PhoneNumber': user_phone
                })
            unregister_class()
                
        elif user_unregister_choice == 4:
            table = dynamodb.Table('MoreJesseSpin')
            try:
                user_phone = int(input('\nPlease provided the phone number on the account\n\t >>>  '))
            except ValueError as e:
                print('Great job, try again')

            table.delete_item(
                Key={
                    'PhoneNumber': user_phone
                })
            unregister_class()
                
        else: 
            print('\nYou did not choose a valid option from this menu\n')
            unregister_class()
    user_menu()


def download_schedule():
    """ """
    bucket = 'richard.w.brown420'

    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file('group_schedule.json', 'Group Schedule Downloaded')
    print('\nThe schedule has been downloaded.\nCheck your project for:\n\n\t\"Group Schedule Downloaded\"')
    user_menu()


def bmi_index():
    """ """
    try:
        user_height = int(input('\nPlease provide your height in TOTAL INCHES\n\t>>>  '))
    except ValueError as e:
        print('Come on man, provide an integer height in inches')
        bmi_index()
    try:
        user_weight = int(input('\nPlease provide your INTEGER weight, nothing irrational please\n\t>>>  '))
    except ValueError as e:
        print('Could you please provide your integer weight in pounds\n..please?')
        user_weight = int(input('\nPlease provide your INTEGER weight, nothing irrational please\n\t>>>  '))
        
    user_bmi = (703 * user_weight) / (user_height * user_height)

    print('Your body mass index is: ', user_bmi)
    try:
        moving_along = input('\n\nWould you like to calculate again? y/n\n\t>>>  ').title()
    except ValueError as e:
        print('Simple y = yes and n = no')
        moving_along
    if moving_along != 'y':
        user_menu()
    elif moving_along != 'n':
        bmi_index()
    else:
        print('Come on man')
        bmi_index()
    

def upload_photo():
    """ """
    bucket = 'social.media.photos.420'
    user_object = input('\nPlease provide the file name\n\t>>>  ')
    src_data = input('\nPlease provide the file path\n\t>>>  ')
    s3c.put_object(Bucket=bucket, Key=user_object, Body=(src_data))
    user_menu()

    
user_menu()
