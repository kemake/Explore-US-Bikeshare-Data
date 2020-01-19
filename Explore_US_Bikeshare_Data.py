import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list=['chicago', 'new york city', 'washington']
month_list=['january', 'february', 'march', 'april', 'may', 'june','all']
week_list=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    def input_check(v_list, input_message, error_message):
        """
        Asks user to input messages and check if it is valid
        """
        while True:
            v = input(input_message).lower()
            if v in v_list:
                return v
                break
            else:
                print(error_message)
                
    #filter city
    city = input_check(city_list,"Would you like to see data for Chicago, New York City, or Washington?", " Please input the right city name")
    
    #filter month
    month = input_check(month_list,"Which month? all, january, february, ... , june?", " Please input the right month")
    
    #filter weekday
    day = input_check(week_list,"Which day? all, monday, tuesday, ... sunday?", " Please input the right weekday")

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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday']=df['Start Time'].dt.weekday_name
    if month != 'all':
        df = df[df['month'] == month_list.index(month) + 1]
    if day != 'all':
      df=df[df['weekday'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].value_counts().index[0]
    print("Most common month:", common_month)

    # display the most common day of week
    common_day = df['weekday'].value_counts().index[0]
    print("Most common day of week:", common_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().index[0]
    print("Most common start hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].value_counts().index[0]
    print("Most commonly used start station:", popular_start_station)
    
    # display most commonly used end station
    popular_end_station=df['End Station'].value_counts().index[0]
    print("Most commonly used end station:", popular_end_station)
    
    # display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total traVel time is", total_time)
    
    #  display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean traVel time is", mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of User Type: \n", df['User Type'].value_counts())
    
    #  Display counts of gender
    if 'Gender' in df.columns:
        print('-' * 30)
        print("Counts of Gender: \n", df['Gender'].value_counts())
        
    
    # Display earliest , most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('-' * 30)
        print("Earliest year of birth: ", int(df['Birth Year'].min()))
        print("Most recent year of birth: ", int(df['Birth Year'].max()))
        print("Most common year of birth: ", int(df['Birth Year'].value_counts().index[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
