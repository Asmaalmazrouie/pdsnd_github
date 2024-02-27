import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("\nSelect a city: Chicago, New York City, or Washington?\n").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("invalid city")
            continue
        else:
            break
        
    while True:
        month = input("\nSelect a month: January, February, March, April, May, June, all\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("invalid month")
            continue
        else:
            break
    
    while True:
        day = input("\n Select a day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,all \n").lower()
        if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print("invalid day")
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1
        df = df[df['month'] == month]

        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('\n The most common month :', months[df['month'].mode()[0] - 1])

    print('\n The most common day of the week: ', df['day_of_week'].mode()[0])

    print('\n The most common start hour is: ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('\n The most common start station is: ', df['Start Station'].value_counts().idxmax())

    print('\nThe most common end station:', df['End Station'].value_counts().idxmax())

    Combination_Station =df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most frequent combination of start station and end station:', df['Start Station'].value_counts().idxmax(), " & ", df['End Station'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('Total travel time', df['Trip Duration'].sum().round(), " Days")
    print('The Mean travel time', df['Trip Duration'].mean().round(), " Minutes")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User Types:\n', df['User Type'].value_counts())

   
    try:
      print('\n gender types:', df['Gender'].value_counts())
    except KeyError:
      print("no data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      print('\n Most earliest year is:', df['Birth Year'].min())
    except KeyError:
      print("no data available")

    try:
      print('\n Most recent year:', df['Birth Year'].max())
    except KeyError:
      print("no data available")

    try:
      print('\n Most common year:', int(df['Birth Year'].value_counts().idxmax()))
    except KeyError:
      print(" no data available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while view_data.lower() == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input( 'Do you wish to continue?:')
            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
