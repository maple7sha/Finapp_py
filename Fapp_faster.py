import os
import sys
import csv #lib to read in csv files and content
import ystockquote #lib with rich set of yahoo api functions.
import time #to time the whole process, hopefully improve it in the future
try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode

def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    return str(resp.read().decode('utf-8').strip())

def get_stockdata(stat, csvfile):
  #read in list of symbols
  sym_stockdata_raw = csv.reader(open(csvfile, 'r'))

  #convert object to list of list of strings
  symlist_stockdata = (list(sym_stockdata_raw))
  symlist_stockdata = symlist_stockdata[1:] #remove first row
  #count
  numrows_stockdata = len(symlist_stockdata)
  count  = 1 #count total iteration
  count200 = 0 #count 200-cycle iteration
  datastr_stockdata = '' #store requested data
  sym = '' #temp store 200 syms for sending
  for row in symlist_stockdata:
    sym += '+'
    sym += str(row[0]) #first elem of row is SYMBOL
    if sym[0] == '+':
      sym = sym[1:]
    count200 += 1
    count  += 1
    #request 200 stocks info a time
    if count200 == 200 or count == numrows_stockdata :
      ret = (_request(sym, stat))
      datastr_stockdata += ret
      count200 = 0
      count += 1
      sym = ''
  #print
  return datastr_stockdata

def main():
  #determine what data are requested
  ###################################
  stat = 'nk' #requested info keys###
  ###################################
  datastr_nasdaq = get_stockdata(stat, 'companylist_nasdaq.csv')
  prt_data(datastr_nasdaq)

  datastr_nyse = get_stockdata(stat, 'companylist_nyse.csv')
  prt_data(datastr_nyse)

### future plans:
#algo to refine the searching process; each algo can be done here

def prt_data(datastr):
  print datastr
  datalist = datastr.split('\r\n')
  print len(datalist)

if __name__ == '__main__':
  print 'go'
  main()
  print 'stop'






#for (s, d) in zip(symlist, datalist):
   # print "%s: %s \n" % (s[0], d)
#  f = open('nyse_52high', 'w')
 # for (name, data) in zip(sym_nyse_raw, datastr_nyse):
  #  print str(data)
   # f.write(str(name))
    #f.write(': ')
    #f.write(str(data))
    #f.write('\n')
#  count2 = 0
#  for row in sym_nyse_raw:
#    sym_nyse   += '+'
#    sym_nyse   += str(row[0])
#    if sym_nyse == '+Symbol':
#      sym_nyse = 'DDD'
#    count2 += 1
#  print sym_nyse
#  sym_nyse='ZMH+ZB^A+ZB^C+ZB^F+ZB^G+ZB^H+ZTS+ZA+ZF+ZTR'
#  stat = 'r'
#  datastr = _request(sym_nyse, stat)
#  print datastr


#"""
#def get_nyse(stat):
#  #read in list of symbols
#  sym_nyse_raw = csv.reader(open('companylist_nyse.csv', 'r'))
#
#  #convert object to list of list of strings
#  symlist_nyse = (list(sym_nyse_raw))
#  symlist_nyse = symlist_nyse[1:] #remove first row
#  #count
#  numrows_nyse = len(symlist_nyse)
#  count  = 1 #count total iteration
#  count200 = 0 #count 200-cycle iteration
#  datastr_nyse = '' #store requested data
#  sym = '' #temp store 200 syms for sending
#  for row in symlist_nyse:
#    sym += '+'
#    sym += str(row[0]) #first elem of row is SYMBOL
#    if sym[0] == '+':
#      sym = sym[1:]
#    count200 += 1
#    count  += 1
#    #request 200 stocks info a time
#    if count200 == 200 or count == numrows_nyse :
#      ret = (_request(sym, stat))
#      datastr_nyse += ret
#      count200 = 0
#      count += 1
#      sym = ''
#  #print
#  return datastr_nyse
#"""