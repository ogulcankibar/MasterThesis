import pandas as pd
import numpy as np
import musthe as m

import melodyDetection as md

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def quantize_notes(notesArray, keyandScale):

       key = keyandScale.split(" ")[0]
       scale = keyandScale.split(" ")[1]

       if scale == "minor":
              scale = "natural_minor"

       s = m.Scale(m.Note(key), scale)
       scaleArray = [str(s[i]) for i in range(len(s))]

       midi_df = pd.read_excel("/home/ogulcan/PycharmProjects/MasterThesis/MIDI Note to Frequency Conversion Table.xlsx").iloc[1: , :]
       test_df = midi_df[['note','Pitch']]
       test_arr = test_df.to_numpy()

       print_df = test_df.head(12)
       print_arr = print_df.to_numpy()

       index_arr = []
       for index in range(len(scaleArray)):
              #print(scaleArray[index])
              for inner_inderx in range(len(print_arr)):
                     #print(print_arr[inner_inderx])
                     if(scaleArray[index] == print_arr[inner_inderx][0][:-1]):
                            #print("Doğru")
                            #print(f"scaleArray: {scaleArray[index]} ¾ printArray: {print_arr[inner_inderx][0][:-1]}")
                            index_arr.append(print_arr[inner_inderx][1])

       index_np_array = np.array(index_arr)

       new_array = []
       for j in range(10):
              for i in range(len(index_arr)):
                     new_array.append(index_arr[i] + j * 12)


       for index in range(len(notesArray)):
              check = np.isin(notesArray[index], new_array)
              if(check == False):
                     #note = notes[index]
                     nearest = find_nearest(new_array, notesArray[index])
                     #print(f"Note: {note} Nearest: {nearest}")
                     notesArray[index] = nearest

       return notesArray

def quantize_durations(durationsArray, songBPM):

       duration_df = pd.DataFrame(durationsArray, columns=['Duration'])

       nduration_df = pd.read_excel("/home/ogulcan/PycharmProjects/MasterThesis/Duration Formula.xlsx")
       nduration_df["Length"] = round(nduration_df.Formula / songBPM,6)

       for index, row in duration_df.iterrows():
              time = round(row['Duration'], 6)
              #print(f"time {time}")

              result_index = nduration_df['Length'].sub(time).abs().idxmin()
              # print(result_index)

              duration_df.at[index, 'Calculated Duration'] = nduration_df["Length"][result_index]

       durationsArray = duration_df["Calculated Duration"].to_numpy()

       return durationsArray
