#!/usr/bin/env python
'''
DOCUMENTATION strings (Dict and sets examples for class)

'''

def main():
    '''
    program entry

    :return: None
    '''
    #get cmd line options
    dict_examples()
    set_examples()

def dict_examples():
    """
    dict files
    :return: None
    """
    d1 = {
        's2': [1, 4, 9, 8],
        's3': [5, 8, 1, 7]
    }
    print(d1['s2'][2])
    d1['s4'] = [7,6,1,9]

    print(d1.keys())
    print(d1.values())

    for k, values in d1.items():
        print(k,values)

    print(d1['s2'])
    # using get is safer when looping especially as a default value can be specified when the data is not there
    print(d1.get('x5', []))

def set_examples():
    """
    documentation strings
    :return:  none
    """
    cities = {'albany', 'colonie', 'saratoga'}
    cities2 = {'colonie', 'troy', 'latham'}

    print("BOTH:", cities & cities2) #common
    print("just 1:", cities ^ cities2) #unique to 1
    print("All:", cities | cities2) #pipe is a unique union
    #can also subtract

    list = ['a', 'b', 'c','d']
    print(set(list)) # no order unique values

if __name__ == 'main': #allows the script to be imported or run individually
    main()

dict_examples()