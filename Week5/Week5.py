import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randint(0,100,size=(1000000, 4)))

df = pd.concat([df, df[3]], axis=1, ignore_index=True)

print(df)

# Dump to HDF
store = pd.HDFStore('store.h5')
start1 =time.perf_counter()
store['df']=df
store.close()
print('HDF time:')
print(time.perf_counter()-start1)


# Dump to Feather
import pyarrow.feather as feather
start2 =time.perf_counter()

feather.write_feather(df,'Feather')
print('Feather time:')
print(time.perf_counter()-start2)

# Dump to Parquet
import pyarrow as pa
import pyarrow.parquet as pq
start3 =time.perf_counter()
table = pa.Table.from_pandas(df, preserve_index=False)
pq.write_table(table, 'Parquet')

print('Parquet time:')
print(time.perf_counter()-start3)