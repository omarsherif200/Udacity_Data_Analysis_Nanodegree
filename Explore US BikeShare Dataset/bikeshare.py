import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the name of a city from one of those cities [chicago, new york city, washington] ").lower().strip()
        if city not in CITY_DATA:
            print("Invalid input! Please enter the name of one of the stated cities")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('Which month to filter by [January, February, March, April, May, June] or type all to apply no filter: ')
        month=month.lower().strip()
        if month not in months and month !='all':
            print("Invalid input! Please enter a month from [January to June] or type all to apply no filter")
            continue
        else:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('which day of week to filter by [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday], or "all" to apply no day filter: ').lower().strip()
        if day not in days and day!='all':
            print("Invalid input! Please enter a day from [Sunday to Saturday] or type all to apply no filter")
            continue
        else:
            break
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['day_of_week']=df['day_of_week'].str.lower()
#calendar.day_name[(df['Start Time'].dt.week)]

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = [x+1 for x in range(len(months)) if months[x]==month][0]
        # filter by month to create the new dataframe
        df = df[df['month']==month]
        #print(df.head())

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print("most common month is {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("most common day of week is {}".format(most_common_day))
    # TO DO: display the most common start hour
    most_common_start_hour=df['Start Time'].dt.hour.mode()[0]
    print("most common start hour is {}".format(most_common_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("most common used start station is {}".format(most_common_start_station))
    

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("most common used end station is {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=(df['Start Station']+'--'+df['End Station']).mode()[0]
    print("most most frequent combination of start station and end station trip is {}".format(most_common_start_end_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time is {} ,".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("average travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    unique_user_type_list=df["User Type"].value_counts()
    print("count of user types is \n")   
    for user_type,count in unique_user_type_list.iteritems():
        print(str(user_type)+"  "+str(count))

    if 'Gender' not in df:
        print("There are no Gender and Birth information for Washington")
        return
    # TO DO: Display counts of gender
    gender_list=df["Gender"].value_counts()
    print("count of user types is \n")   
    for gender,count in gender_list.iteritems():
        print(str(gender)+"  "+str(count))

    # TO DO: Display earliest, most recent, and most common year of birth
    earlist_year_of_birth=df['Birth Year'].min()
    print("Earlist year of birth is {}".format(earlist_year_of_birth))
    
    most_recent_year_of_birth=df['Birth Year'].max()
    print("most recent year of birth is {}".format(most_recent_year_of_birth))
    
    most_common_year_of_birth=df['Birth Year'].mode()[0]
    print("most common year of birth is {}".format(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    idx=0
    while(True):
        view_more_data=input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower().strip()
        if view_more_data=="yes":
            print(df.iloc[idx:idx+5])
            idx+=5
        elif view_more_data=="no":
            break
        else:
            print("Invalid Input! Please enter Yes or No\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        


if __name__ == "__main__":
	main()

