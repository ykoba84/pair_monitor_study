from keras.utils import plot_model
import numpy as np

def ModelOutput(model, outputpath):
    outputdir = outputpath + '/model.png'
    plot_model(model, to_file=outputdir, show_shapes=True)

def TotalTimeOutput(time, outputpath):
    outputdir = outputpath + '/total_time.txt'
    f = open(outputdir, 'w')
    f.write(format(time) + ' sec')
    f.close()

def EvaluateOutput(score, outputpath):
    outputdir = outputpath + '/score.txt'
    f = open(outputdir, 'w')
    f.write('Test_loss:' + str(score[0]))
    f.write(' Test_accuracy:' + str(score[1]))
    f.close()

def CsvOutput(data, outputpath):
    outputdir = outputpath + '/prediction.csv'
    fmts = ["%.0f", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e"]
    np.savetxt(outputdir, data, fmt=fmts, delimiter=',')

def CsvOutput_detail(data, outputpath):
    outputdir = outputpath + '/prediction.csv'
    fmts = ["%.0f", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e"]
    np.savetxt(outputdir, data, fmt=fmts, delimiter=',')

def CsvOutput_0238(data, outputpath):
    outputdir = outputpath + '/prediction.csv'
    fmts = ["%.0f", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e", "%.6e"]
    np.savetxt(outputdir, data, fmt=fmts, delimiter=',')

def HyperParameterOutput(batch_size, outputpath):
    outputdir = outputpath + '/hyperparameter.txt'
    f = open(outputdir, 'w')
    f.write('Batch size = ' + str(batch_size))
    f.close()

