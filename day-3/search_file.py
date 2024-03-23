import os
import time

require_file=input('What file are you searching?: ')

start_time = time.time()
for p,d,f in os.walk('c:\\'):
    for file in f:
        if file == require_file:
            print(os.path.join(p,file))
            
print("--- %s seconds ---" % (time.time() - start_time))