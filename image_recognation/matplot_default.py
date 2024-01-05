import matplotlib.pyplot as plt
import numpy as np

class plot_progress():
    def __init__(self,acc_train,loss_train,acc_valid,loss_valid,path,save=False):
        self.acc_train=acc_train
        self.loss_train=loss_train
        self.acc_valid=acc_valid
        self.loss_valid=loss_valid
        self.save=save
        self.path=path

    def plot(self):
        fig = plt.figure(figsize = (10,10))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        x=np.arange(1,len(self.acc_train)+1,1)
        c1,c2='blue','orange'

        ax1.plot(x,self.loss_train,color=c1)
        ax1.plot(x,self.loss_valid,color=c2)
        ax2.plot(x,self.acc_train,color=c1)
        ax2.plot(x,self.acc_valid,color=c2)
        ax1.set_xlabel('epoch')
        ax2.set_xlabel('epoch')
        ax1.set_ylabel('loss')
        ax2.set_ylabel('accuracy')
        ax1.legend(loc = 'upper right',fontsize='x-large') 
        ax2.legend(loc = 'upper right',fontsize='x-large') 

        plt.show()

    def save(self):
        if self.save:
            plt.savefig(self.path)


