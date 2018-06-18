from nptdms import TdmsFile
import numpy as np
import pandas as pd
# from matplotlib import pyplot


# load tdms file
# tdms_file = TdmsFile("test171011.tdms")
tdms_file = TdmsFile(
    "/Users/taku/Scripts/Python/DataAnalysis/LabVIEWtdms/test171011.tdms"
    )

# read channel, and arrange numpy array
trigger_channel = tdms_file.object('Voltage Task #0', '電圧_0')
sample_channel = tdms_file.object('Voltage Task #0', '電圧_1')
trigger_data = trigger_channel.data
sample_data = sample_channel.data
time = trigger_channel.time_track()

# pick data
grad = np.gradient(trigger_data, time)
thres = np.tile(0.1, trigger_data.shape[0])
band = 0.005

temp_normal = trigger_data - thres
normal = np.absolute(trigger_data - thres)
trigger_index = np.array(np.where(normal < band))
trigger_index = trigger_index[grad[trigger_index] > 0]
print(trigger_index)

sample_data = sample_data[trigger_index]
sample_time = time[trigger_index]
time_data = np.array((sample_time, sample_data))
df_time_data = pd.DataFrame(time_data)
print(sample_data)
print(time_data)
print(df_time_data)

df_time_data.to_csv('some.csv')

# pyplot.plot(sample_data)
# pyplot.show()
