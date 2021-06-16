from numpy.core.shape_base import block
import fetch
import plotter


import sys, os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

test1 = False
test2 = False
test3 = False
test4 = False

blockPrint()

try:
    SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD = fetch.get_lw_data();
    test1 = True
except:
    pass


try:
    x = fetch.pack_week(SP500, DJIA, NASDAQ, EURUSD, OIL, GOLD);
    test2 = True
except:
    pass


try:
    plotter.plot_last_week(test = True)
    test3 = True
except:
    pass


try:
    plotter.plot_historical_week([321], test = True)
    test4 = True
except:
    pass


enablePrint()

print('\n')
print("======== UNIT TEST RESULTS ========")
if test1:
    print("1. Online fetch test OK.")
else:
    print("1. Online fetch test FAILED.")

if test2:
    print("2. Data conversion test OK.")
else:
    print("2. Data conversion test FAILED.")

if test3:
    print("3. Last Week Plot test OK.")
else:
    print("3. Last Week Plot test FAILED.")

if test4:
    print("4. Historical Plot test OK.")
else:
    print("4. Historical Plot FAILED.")