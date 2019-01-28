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

def loss_and_acc_2para(hist, epochs, outputpath):

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
    
    acc_sigmax = hist.history['output_sigmax_acc']
    acc_sigmay = hist.history['output_sigmay_acc']
    val_acc_sigmax = hist.history['val_output_sigmax_acc']
    val_acc_sigmay = hist.history['val_output_sigmay_acc']
    
    plt.subplot(122)
    plt.plot(range(1, epochs+1), acc_sigmax, color='b', marker='.', label='sigmax_acc')
    plt.plot(range(1, epochs+1), acc_sigmay, color='b', marker='.', linestyle="dashed", label='sigmay_acc')
    plt.plot(range(1, epochs+1), val_acc_sigmax, color='g', marker='.', label='val_sigmax_acc')
    plt.plot(range(1, epochs+1), val_acc_sigmax, color='g', marker='.', linestyle="dashed", label='val_sigmay_acc')
    plt.legend(loc='best', fontsize=10)
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('acc')
    plt.xlim([0.0, epochs])
    plt.ylim([0.0, 1.0])
    
    plt.tight_layout()
    plt.savefig(outputdir)
