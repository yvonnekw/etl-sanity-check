from etl_sanity_checks import *
import time
import datetime

print("Starting data pipeline at ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("_____________________________________")

# Step 1: check for duplicates in the source file
t0 = time.time()
test_check_duplicates()
t1 = time.time()
print("Step 1: Done")
print("-----> Test completed in ", str(t1-t0), " seconds ", "\n")

# Step 2: # test if target is not blank
t0 = time.time()
test_dat_completeness()
t1 = time.time()
print("Step 2: Done")
print("-----> Test completed in ", str(t1-t0), " seconds ", "\n")

# Step 3: # test if target is not blank
t0 = time.time()
test_deptno_for_null_value_check()
t1 = time.time()
print("Step 3: Done")
print("-----> Test completed in ", str(t1-t0), " seconds ", "\n")

# Step 4: # test if target is not blank
t0 = time.time()
test_eno_for_unique_value_check()
t1 = time.time()
print("Step 4: Done")
print("-----> Test completed in ", str(t1-t0), " seconds ", "\n")