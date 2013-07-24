import os
import sys
import csv #lib to read in csv files and content
import ystockquote #lib with rich set of yahoo api functions.
import time #to time the whole process, hopefully improve it in the future

#create a new file to store things in
f = open ('output', 'w')

#start data processing
start_time = time.time()
#1st, get a list of all the symbols
sym_nasdaq_raw = csv.reader(open('companylist_nasdaq.csv', 'r'))
sym_nyse_raw = csv.reader(open('companylist_nyse.csv', 'r'))
sym_nasdaq = []
sym_nyse = []

#take out the symbols only from the data
#in the future, we can use if condition to check which sector is it, and act accordingly
for row in sym_nasdaq_raw:
  sym_nasdaq.append(row[0])
for row in sym_nasdaq_raw:
  sym_nyse.append(row[0])
end_time = time.time()
print("Stage One Elapsed time was %g seconds" % (end_time - start_time))

#2nd, store relevant parameters related to each symbol to an array structure
start_time = time.time()
count = 0
for sym in sym_nasdaq:
  data = ystockquote.get_price(str(sym)) #for next step, will model the things in this step,
                                         #calculate a score, and sort all things in different industry
  f.write(str(sym))
  f.write(': ')
  f.write(str(data))
  f.write('\n')
  print count
  count += 1
end_time = time.time()
print("Stage Two Elapsed time was %g seconds" % (end_time - start_time))

#for sym in sym_nyse:
# data = ystockquote.get_price(str(sym))
#  f.write(str(sym))
#  f.write(': ')
#  f.write(str(data))
#  f.write('\n')
print 'end of stage 2'
print 'succeed!'
#3rd, sort it, and gives you back the best value stock!

# ftp.nasdaqtrader.com

# and to further speed up => do one request with a huge url, then sort the data!