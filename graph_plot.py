import matplotlib.pyplot as plt

def loss_and_acc(hist, epochs, outputpath):

    outputdir = outputpath + '/image.png'
    
    plt.figure(figsize=(7,5))
    
    loss = hist.history['loss']
    val_loss = hist.history['val_loss']
    plt.subplot(121)
    plt.plot(range(1, epochs+1), loss, marker='.', label='loss')
    plt.plot(range(1, epochs+1), val_loss, color='g', marker='.', label='val_loss')
    plt.legend(loc='best', fontsize=10)
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.xlim([0.0, epochs])
    plt.ylim([0.0, 2.5])
    
    acc = hist.history['acc']
    val_acc = hist.history['val_acc']
    plt.subplot(122)
    plt.plot(range(1, epochs+1), acc, marker='.', label='acc')
    plt.plot(range(1, epochs+1), val_acc, color='g', marker='.', label='val_acc')
    plt.legend(loc='best', fontsize=10)
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('acc')
    plt.xlim([0.0, epochs])
    plt.ylim([0.0, 1.0])

    plt.tight_layout()
    plt.savefig(outputdir)
