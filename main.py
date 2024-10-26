from time import *
import random as r
def mistakes(c_sentence,i_sentence):
    error=0
    for i in range(len(c_sentence)):
        try:
            if c_sentence[i]!=i_sentence[i]:
                error=error+1
        except:
            error=error+1
    return error
def time_taken(s_time,e_time,i_sentence):
    time_delay=e_time-s_time
    speed=len(i_sentence.split())/(time_delay/60)
    return round(speed,2)


sentence=['''The quick brown fox jumps over the lazy dog.''',
'''A soft rain began to fall, creating a soothing melody against the windows.''',
'''In the distance, a lone owl hooted, adding an air of mystery to the night.''']

choose_sentence=r.choice(sentence)
print("___Typing Speed Test____")
print("Enter this Sentence to Check speed:")
print(choose_sentence)
start_time=time()
input_sentence=input()
end_time=time()

mistakes_count=mistakes(choose_sentence,input_sentence)

time_count=time_taken(start_time,end_time,input_sentence)

print(f"Error : {mistakes_count}\nspeed {time_count} w/sec")