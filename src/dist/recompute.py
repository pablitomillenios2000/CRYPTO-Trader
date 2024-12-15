#!/usr/bin/env python3

import time
import os

# Start the timer
start_time = time.time()

# Remove all .txt files
os.system("rm ../view/output/*.txt")

# Execute the commands
os.system("python3 ./pairname.py")
os.system("python3 ./compute_asset.py")
os.system("python3 ./compute_ema.py")
os.system("python3 ./compute_sma.py")
os.system("python3 ./slopedirection.py")
os.system("python3 ./compute_ema_micro.py")
os.system("python3 ./compute_trades_trailsl_localmin.py")
# os.system("python3 ./compute_trades_ema_algo_minloss.py")
# os.system("python3 ./compute_margin_requirement.py")
#os.system("python3 ./tradedirectionfilter.py") #filters non-steep
os.system("python3 ./compute_unt_portfolio.py")
os.system("python3 ./compute_final_portfolio.py")

# Stop the timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Time taken for execution: {elapsed_time:.2f} seconds")