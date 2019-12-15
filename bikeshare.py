import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
monthly = ["january", "february", "march", "april", "may", "june", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city  = input(" Which city will you like to explore. (chicago, new york city or washington): ")
        if city in CITY_DATA:
            break
        else:
            print("Sorry wrong input, try again\n")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month  = input(" Select the month: (january, february, march, april, may, june or all): ")
        if month in monthly:
            break
        else:
             print("Sorry wrong input, try again\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day  = input(" Select the day of week (monday, tuesday... or all ): ")
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
             print("Sorry wrong input, try again\n")

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    
    print("most common month is: {}\n".format(months[common_month-1]))

    # TO DO: display the most common day of week
    
    print("most common day of the week: {}\n".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("most common start hour: {}\n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "," + df['End Station']
    common_station = combine_stations.mode()[0]
    print('\nMost frequent used combinations are:\n{} \nto\n{}'.format(common_station.split(',')[0], common_station.split(',')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total trip duration: {} days".format(round(total_travel_time/(60*60*24),2)))
    # TO DO: display mean travel time
    
    average_travel_time = df['Trip Duration'].mean()
    print("The mean trip duration: {} seconds".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("\n The count of various genders\n")
    print(gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common = df['Birth Year'].mode()[0]
    print("\nThe earliest year of birth is: {}, \nThe most recent year of birth is: {}  \
          \nThe most common year of birth is: {}".format(earliest, most_recent, most_common))

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
