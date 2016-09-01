from datetime import datetime
from collections import OrderedDict
import collections
import sys
import os
import re


class MonthData(object):
    '''
    A class to store the weather stats for a month.
    '''
    def __init__(self, month, max_temps, min_temps, avg_temps, precips):
        '''
        INPUT:
            - month: name of the month (e.g. 01/14)
            - max_temps: list of the maximum temperatures per day
            - min_temps: list of the minimum temperatures per day
            - avg_temps: list of the average temperatures per day
            - precips: list of the precipation amounts per day

        Fill in the data for the month.

        Create these instance variables:
            - month: name of the month
            - avg_temp: average of all the average temperatures
            - min_temp: minimum of all the minimum temperatures
            - max_temp: maximum of all the maximum temperatures
            - total_precip: total of all the precipitation
            - days_precip: number of days where there was precipitation
        '''
        self.month = month
        self.avg_temp = sum(avg_temps)/float(len(avg_temps))
        self.min_temp = min(min_temps)
        self.max_temp = max(max_temps)
        self.total_precip = sum (precips)
        self.days_precip = len([day for day in precips if day>0])

class MonthlyWeather(object):
    '''
    A class to store the month by month weather stats for a city.
    '''
    def __init__(self, name, filename):
        '''
        INPUT:
            name: str (the city name)
            filename: str (name of tsv file of the data)

        Fill in the data for a city from a tsv file.
        '''
        self.name = name
        self.data = self._read_data(filename)
        #print self.data
        #a = MonthData(self.month, self.max_temps, self.min_temps, self.avg_temps, self.precips)

    def _read_data(self, filename):
        '''
        INPUT:
            filename: str
        OUTPUT: dict (str => MonthData)

        Read in the data from the filename and store it in an OrderedDict.
        The keys are the month names (e.g. 01/14) and the values are the
        associated MonthData objects.
        '''
        od = OrderedDict()
        d = self.load_month_data(filename)
        for month in sorted(d):
            s = MonthData(month, d[month]['max_temp'], d[month]['min_temp'], d[month]['avg_temp'], d[month]['prec'])
            od[month] = [s.max_temp, s.min_temp, s.avg_temp, s.total_precip, s.days_precip]

        return od

    def load_month_data(self, filename):
        d = collections.defaultdict(dict)

        with open(filename) as f:
            for line in f:
                a = line.strip('\n').split('\t')
                year = a[0].split('-')[0][-2:]
                month = a[0].split('-')[1]

                if 'max_temp' in d[month + '/' + year]:
                    d[month + '/' + year]['max_temp'].append(float(a[1]))
                    d[month + '/' + year]['min_temp'].append(float(a[2]))
                    d[month + '/' + year]['avg_temp'].append(float(a[3]))
                    if 'T' not in a[7]:
                        d[month + '/' + year]['prec'].append(float(a[7]))
                else:
                    d[month + '/' + year]['max_temp'] = [float(a[1])]
                    d[month + '/' + year]['min_temp'] = [float(a[2])]
                    d[month + '/' + year]['avg_temp'] = [float(a[3])]
                    if 'T' not in a[7]:
                        d[month + '/' + year]['prec'] = [float(a[7])]
                    else:
                        d[month + '/' + year]['prec'] = []

        return d


    def __str__(self):
        '''
        INPUT: None
        OUTPUT: str

        Return a string demonstrating these values for each month:
            - average temperature
            - number of days with precipitation
            - total amount of precipitation
        '''
        ourstr = '\t\tprecipitation\nmonth\ttemp\tdays\ttotal\n'

        ourstr += ''.join(['{}\t{:.2f}\t{}\t{}\n'.format(m, self.data[m][2], \
        self.data[m][4], self.data[m][3]) for m in self.data])
        #print ourstr
        return ourstr


class WeatherByCity(object):
    '''
    A class for representing weather data for a city
    '''
    def __init__(self, directory):
        self.data = dict()
        self.months = set()

        #openfiles(directory)
        #within the each file, use a methods to accomplish filldata (city)


        '''
        INPUT: directory: str (location of tsv data files)

        Fill in the data for all the city tsv files in the directory.

        Create these instance variables:
            - data: dict (str => MonthlyWeather)
            - months: set (strs)

        The data dictionary should have the city names as keys and their
        associated MonthlyWeather objects as values.

        The months are all the months that are in any of the datasets.

        Raise an IOError if the directory given doesn't exist.
        '''
        pass
