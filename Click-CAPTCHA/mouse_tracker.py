import pyautogui as pag
import json
import time

class mouseTracker(object):
    '''
    This function will generate tracks which is used to move mouse like human in selenium.
    the date will save to a string file. The format of the result:
    [[(x1,y1), delay1], [(x2, y2), delay2], [(x3, y3), delay3]...]
    '''
    def __init__(self, filename='track.txt', period=0.01, max_stop_time=0.5):
        '''
        :para filename: the filename to save the track of mouse.
        :para period: the fixed time to record mouse position.
        :para max_stop_time: the max_time user stayed which will be considerd as finishing record.
        '''

        self.period = period
        self.filename = filename
        self.stop_num = int(max_stop_time/period)
        self.res = []

        # record start point of mouse
        self.start_point = tuple(pag.position())
        # this variable is to previous point 
        self.previous_point = self.start_point
        # save the record of track
        self.track = []
        # save the interval between each point
        self.sleep_time = []
        # calculate loop times
        self.track.append(self.start_point)

    def record(self):
        '''
        Record the relative displacement of user's mouse each fixed time.
        '''

        print('Moving your mouse to start record, stop moving to finish')

        # record the number of same position.
        num = 0
        # dead loop, break when staying longer than max_stop_time
        while True:
            new = tuple(pag.position())
            time.sleep(self.period)
            if new == self.start_point:
                continue
            if new == self.previous_point:
                num = num + 1
            else:
                self.track.append(new)
                self.sleep_time.append(num*self.period)
                num = 1
            self.previous_point = new
            if num > self.stop_num:
                break;
        self.sleep_time.append(0)

        # A function used to minus two point, like (3,2)-(2,1) is (1,1)
        tuple_minus = lambda x,y:(x[0]-y[0],x[1]-y[1])
        # save generator to speed up
        _range = range(1,len(self.track))
        # get relative displacement, that is the diff coordinate of neightbour
        diff = [tuple_minus(self.track[x],self.track[x-1]) for x in _range]
        # make sure the length of diff list is eaqual to sleep_time's
        diff.insert(0,(0,0))
        # get results list
        for i in range(len(self.track)):
            self.res.append((diff[i], self.sleep_time[i]))


    def print_res(self):
        for i in self.res:
            print(i)

    # save results to file
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.res, f)
            
    def generate(self):
        self.print_res()
        self.record()
        self.save()

if __name__ == "__main__":
    mouseTracker().generate()
