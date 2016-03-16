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
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
class misc(object):
    def getdata(self, nameoffile):
        print ("Importing..")
        output = np.genfromtxt(nameoffile, delimiter=',')
        return output
    def display(self, data, candidates, fname, display):
        cans = np.array(candidates)
        plt.plot(cans[:,0],cans[:,1],'ro')
        plt.axhline(max(cans[:,1])/4, color='r')
        plt.axhline(max(cans[:,1]/2), color='r')
        plt.axhline(int(max(cans[:,1]))*0.75, color='r')
        red_patch = mpatches.Patch(color='red', label='75%, 50% and 25% \nof maximum frequency')
        plt.legend(handles=[red_patch])
        plt.ylabel('Frequency of occurence')
        plt.xlabel('separate items')
        plt.title('Frequency distribution estimation graph')
        plt.hist(data,range(int(min(data)),int(max(data)),1))
        ofile = fname[0:-3]+"png"
        print ("Writing outfile: %s") % (ofile)
        plt.savefig(ofile, bbox_inches='tight')
        if display == True: 
            plt.show()
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
        #print finallist
        part1 = finallist[:len(finallist)/2]
        part2 = finallist[len(finallist)/2:]
        
        meandiff=np.sqrt(np.power(np.mean(part2),2)-np.power(np.mean(part1),2))
        rangeA = max(part1)-min(part1)
        rangeB = max(part2)-min(part2)

        if meandiff> rangeA or meandiff> rangeB:
            print ("Comparing deviations..")
            print ("left|right: %d | %d"%(np.std(part1),np.std(part2)))     
            print ("Frequency quartile distribution")
            print(">25 percent: %d | >50 percent: %d | >75 percent: %d" % (count25,count50,count75))
            print ("Range difference A: %d\nRange difference B: %d\nDistribution distance: %d" % (rangeA,rangeB, meandiff))
            span = (rangeA+rangeB)/2
            dspan = meandiff/span
            
            print ("\nResults indicate two different distributions! Span: %d" % (dspan))
        else:
            print ("Comparing deviations..")
            print ("left|right: %d | %d"%(np.std(part1),np.std(part2)))     
            print ("Frequency quartile distribution")
            print(">25 percent: %d | >50 percent: %d | >75 percent: %d" % (count25,count50,count75))
            print (" Range difference A: %d\n Range difference B: %d\n Distribution distance: %d" % (rangeA,rangeB, meandiff))
            print ("\nResults indicate only one distribution!")
            span = (rangeA+rangeB)/2
            dspan = meandiff/span
            
            print ("\nResults indicate two different distributions! Span: %d" % (dspan))
        return candidates
        
                
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Genemapper tool!")
    parser.add_argument("fileinput", help="Input file, separated by , or ;", type=str)
    parser.add_argument('-d')
    parser.add_argument('-view')
    #parser.add_argument("-v", "--verbose", action="store_true",
                        #help="More program output")
    args = parser.parse_args()        
    filename = args.fileinput
    if args.d is not None:
        data = misc().getdata(filename)
        candidates = misc().keyalgo(misc().keypoints(data))
        if args.view is not None:
            show = True
            misc().display(data,candidates, filename, show)
        else:
            show=False
            misc().display(data,candidates, filename, show)        
else:
        data = misc().getdata(filename)
        candidates = misc().keyalgo(misc().keypoints(data))
    
                             
    
    

