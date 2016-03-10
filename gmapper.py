'''
This software enables calculation of key points within frequency distributions.
Its main use is to find local maxima and provide insights on them. Its primary use
is distinguising between various peaks within data.

This is an open license program, under GNU.
by Blaz Skrlj
'''
import matplotlib as plt
import argparse
import numpy as np
import matplotlib.pyplot as plt
class misc(object):
    def getdata(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("fileinput", help="Input file, separated by , or ;", type=str)
        parser.add_argument("-v", "--verbose", action="store_true",
                            help="More program output")
        args = parser.parse_args()        
        filename = args.fileinput
        print ("Importing..")
        output = np.genfromtxt(filename, delimiter=',')
        return output
    def display(self, data, candidates):
        cans = np.array(candidates)
        plt.plot(cans[:,0],cans[:,1],'ro')
        plt.axhline(int(np.mean(data)), color='r')
        plt.axhline(int(np.mean(data)*1.5), color='r')
        plt.axhline(int(np.mean(data)*0.5), color='r')
        plt.ylabel('Frequency of occurence')
        plt.xlabel('separate items')
        plt.title('Frequency distribution estimation graph')
        plt.show(plt.hist(data,range(int(min(data)),int(max(data)),1)))
        return;
    def keypoints(self, data):
        #vzame pare
        unique, counts = np.unique(data, return_counts=True)
        workdata = np.asarray((unique, counts)).T
        return workdata
    def keyalgo(self,data):
        indices = []
        freqs = []
        for entry in data:
            indices. append(entry[0])
            freqs. append(entry[1])
        # print indices
        # print freqs
        count75=0
        count50=0
        count25=0
        candidates = []
        a3q = int(np.mean(data)*1.5)
        a2q = int(np.mean(data))
        a1q = int(np.mean(data)*0.5)
        for j in freqs:
            if j> a1q:
                count25 +=1
            if j > a2q:
                count50+=1
            if j > a3q:
                count75 +=1
        for k in range(1, len(indices)):
            #print ("%d and %d") % (indices[k],freqs[k])
            try:
                dist = range(-2,2)
                temphit = 0
                #print ("Analysing current candidate: %s"%(indices[k]))
                for l in dist:
                    if freqs[k]>freqs[k+l]:
                        temphit+=1 
                #print ("%d and %d")%(temphit, len(dist))
                if temphit == len(dist)-1 and freqs[k]>a3q:
                    print "Found a good candidate! %d" % (indices[k])
                    candidates.append([indices[k],freqs[k]])
            except:
                print ("Index out of bounds, trimming the range.")
                pass
                    
        #print candidates
        finallist=[]
        for c in candidates:
            finallist.append(c[0])
        print finallist
        part1 = finallist[:len(finallist)/2]
        part2 = finallist[len(finallist)/2:]
        print ("Comparing deviations..")
        print ("left|right: %d | %d"%(np.std(part1),np.std(part2)))
        if np.std(part1)/4 > np.std(part2):
            print ("Distributions are significantly different - you have two samples!")
        else:
            print ("You probably have only one sample!")
        
                
        print ("Frequency quartile distribution")
        print(">25 percent: %d | >50 percent: %d | >75 percent: %d" % (count25,count50,count75))
        return candidates
        
                
            
        
if __name__ == '__main__':
    data = misc().getdata()
    candidates = misc().keyalgo(misc().keypoints(data))
    misc().display(data,candidates)
    
    
                             
    
    

