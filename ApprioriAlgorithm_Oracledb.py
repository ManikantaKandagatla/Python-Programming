__author__ = 'ManiKanta Kandagatla'

import itertools
import cx_Oracle

tid_keys = []
total_items = set()

def get_transaction_data():
    db = cx_Oracle.connect('system', '123', '127.0.0.1/XE')
    c = db.cursor()
    c.execute('select list from app_algo')
    for i in c:
        str = i[0]
        tid_keys.append(set(str.split(',')))
    print 'tid_items',tid_keys

#tid_keys = [{"I1","I2","I5"},{"I2","I4"},{"I2","I3"},{"I1","I2","I4"},{"I1","I3"},{"I2","I3"},{"I1","I3"},{"I1","I2","I3","I5"},{"I1","I2","I3"}]
#print tid_keys

def get_total_items():
    Total_items = set()
    for i in tid_keys:
        Total_items = Total_items | i
    Total_items =list(Total_items)
    return Total_items

def cal_frequency_of_item(Total_items , k ):
    freq = []
    for i in Total_items:
        count = 0
        for j in tid_keys:
            if k == 1:
                if i in j:
                    count = count + 1
            else:
                if set(i) & j == set(i):
                    count = count + 1
        freq.append(count)
    return freq

def filter_Candidate_items(Candidate_items, pre_freq_items,k):
    filtered_Candidate_items = []
    for i in Candidate_items:
        flag = 0
        for j in list(itertools.combinations(i, k)):
            if k==1:
                if set(j)& set(pre_freq_items)!=set(j):
                    flag = 1
            else:
                if j not in pre_freq_items:
                    flag = 1
        if flag == 0:
            filtered_Candidate_items.append(i)
    return filtered_Candidate_items

def cal_k_freq_items(Candidate_items , Candidate_freq ,k, min_support_count ,Total_items):
    if Candidate_items != []:
        print 'Candidate ', k, 'items' ,zip(Candidate_items,Candidate_freq)
        count = 0
        freq_set = []
        freq_item_set = []
        for i in Candidate_freq:
            if i >= min_support_count:
                freq_set.append(Candidate_items[count])
                freq_item_set.append((Candidate_items[count],i))
            count = count + 1
        print 'frequent ', k ,'items ',freq_item_set
        Candidate_items = list(itertools.combinations(Total_items , k+1))
        Candidate_items = filter_Candidate_items(Candidate_items , freq_set ,k)
        Candidate_freq = cal_frequency_of_item(Candidate_items, k+1 )
        cal_k_freq_items(Candidate_items , Candidate_freq , k+1 , min_support_count ,Total_items)

if __name__ == "__main__":
    get_transaction_data()
    Total_items=get_total_items()
    freq = cal_frequency_of_item(Total_items,1)
    cal_k_freq_items(Total_items,freq, 1 , 2 ,Total_items)
