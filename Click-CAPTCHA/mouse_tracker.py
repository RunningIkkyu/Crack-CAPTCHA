import pyautogui as pag
import json
import time

def mouse_tracker():
    start_point = tuple(pag.position())
    co = 0.01
    track = []
    sleep_time = []
    track.append(start_point)
    old = start_point
    num = 0
    print('move mouse')
    while True:
        new = tuple(pag.position())
        time.sleep(co)
        if new == start_point:
            continue
        if new == old:
            num = num + 1
        else:
            track.append(new)
            sleep_time.append(num*co)
            num = 1
        old = new
        if num > 50:
            break;
    sleep_time.append(0)

    tuple_minus = lambda x,y:(x[0]-y[0],x[1]-y[1])
    _range = range(1,len(track))
    diff = [tuple_minus(track[x],track[x-1]) for x in _range]
    diff.insert(0,(0,0))
    l = []
    for i in range(len(track)):
        l.append((diff[i], sleep_time[i]))
    return l


if __name__ == '__main__':
    #track, sleep_time = mouse_tracker()
    #print(len(track), len(sleep_time))
    #tuple_minus = lambda x,y:(x[0]-y[0],x[1]-y[1])
    #_range = range(1,len(track))
    #diff = [tuple_minus(track[x],track[x-1]) for x in _range]
    #diff.insert(0,(0,0))
    ##m = map(tuple_minus, track, [track[0] for i in _range])
    ##l = list(m)
    #for i in range(len(track)):
    #    print (diff[i])
    #    print ('sleep for {0} secondes'.format(sleep_time[i]))
    l = mouse_tracker()
    for i in l:
        print(i)
    with open('track.txt','w') as f:
        json.dump(l, f)
