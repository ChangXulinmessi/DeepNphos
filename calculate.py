import re
import numpy as np
import tensorflow as tf
from keras import layers, optimizers,Sequential,losses
import pandas as pd
from keras.models import Model
import  os
from Bio import SeqIO
from keras.layers import Dense, Dropout, Conv1D,MaxPooling1D, Flatten,Input,BatchNormalization,Activation
from keras.optimizers import Adam,SGD
from keras.models import load_model,Model
def judge_fasta(filename):
    if filename:
        try:
            with open(filename, "r") as handle:
                fasta = SeqIO.parse(handle, "fasta")
                return any(fasta)
        except:
            return False
    else:
        return False


def get_peptide(filepath,type):
    try:
        predict_id = []
        predict_seq = []
        for index, record in enumerate(SeqIO.parse(filepath, 'fasta')):
            re_search = re.search(r"\|[-A-Za-z0-9]+\|", record.name)
            if re_search:
                name = re_search.group()[1:-1]
            else:
                name = record.name
            sequences = 'X' * 18 + str(record.seq) + 'X' * 18
            for location, seq in enumerate(sequences):
                if seq == 'K' and type=='K':

                    predict_id.append(name + '*' + str(location + 1 - 18))
                    predict_seq.append(sequences[location - 18:location + 19])
                elif seq == 'R' and type=='R':

                    predict_id.append(name + '*' + str(location + 1 - 18))
                    predict_seq.append(sequences[location - 18:location + 19])
                elif seq == 'H' and type=='H':

                    predict_id.append(name + '*' + str(location + 1 - 18))
                    predict_seq.append(sequences[location - 18:location + 19])
        csvfile = pd.DataFrame({'Protein': predict_id, 'Sequence': predict_seq})
        #print(csvfile)
        return csvfile
    except:
        return pd.DataFrame()


def Binary(dataframe):
    AA = 'ACDEFGHIKLMNPQRSTVWYX'
    encodings = []
    sequences = list(dataframe['Sequence'])
    for i in sequences:
        sequence = re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(i).upper())
        code = []
        for aa in sequence:
            singlecode = []
            for aa1 in AA:
                tag = 1 if aa == aa1 else 0
                singlecode.append(tag)
            code.append(singlecode)
        encodings.append(code)

    return np.array(encodings).astype(np.float64)



def DeeppArg():

    model = Sequential()
    model.add(Conv1D(64, 1, activation='relu', input_shape=(37, 21)))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.7))

    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.7))

    model.add(Conv1D(64, 5, activation='relu', padding='same'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.7))
    model.add(Flatten())
    # 全连接层
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    #model.summary()
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def DeeppHis():

    model = Sequential()
    model.add(Conv1D(64,1, activation='relu', input_shape=(37, 21)))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.6))

    model.add(Conv1D(64,3, activation='relu'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.6))

    model.add(Conv1D(128,7, activation='relu',padding='same'))
    model.add(MaxPooling1D(2))
    model.add(Dropout(0.6))
    model.add(Flatten())
    # 全连接层
    model.add(Dense(64,activation='relu'))

    #model.add(GlobalAveragePooling1D())
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model


def CNN():
    p = os.getcwd()
    path = p + '\\statics\\Kmodels\\Fold.h5'
    cnn = load_model(path)
    cnn.trainable = True #固定所有预训练模型层的参数
    base_model = Model(inputs=cnn.layers[0].input,outputs=cnn.layers[27].output)#输入全连接层之前所有层
    #print(base_model)
    #print(1)
    #base_model.summary()
    base_model.trainable = True
    '''for layer in base_model.layers[:]:#冻结前n层参数
        print(layer)
        print(0)
        layer.trainable = False'''
    model1 = tf.keras.Sequential([
        base_model
    ])
    model1.compile(optimizer=optimizers.Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    #model1.summary()
    return model1
def core(dataframe, type):
    x = Binary(dataframe)
    #print(x.shape)
    sign = list(dataframe['Protein'])
    #types=list(dataframe['Type'])
    name = []
    position = []
    for s in sign:
        reversal = s[::-1]
        site = reversal.index('*')
        name.append(reversal[site + 1:][::-1])
        position.append(reversal[:site][::-1])
    folds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    predict_score = np.zeros((len(x), len(folds)))
    predict_result = []
    predict_confidence = []
    predict_average_score=[]
    p = os.getcwd()

    if type=='K':
        network_pLys = CNN()

        for fold in folds:

            modelName = 'Fold' + str(fold) + '.h5'
            modelpath = p+"\\statics\\Kmodels\\%s" % modelName
            network_pLys.load_weights(modelpath)
            predict_score[:, fold - 1:fold] = network_pLys.predict(x)

        predict_average_score.append(np.average(predict_score, axis=1))
    elif type=='R':
        network_pArg = DeeppArg()

        for fold in folds:
            modelName = 'Fold' + str(fold) + '.h5'
            modelpath = p+"\\statics\\Rmodels\\%s" % modelName
            network_pArg.load_weights(modelpath)
            predict_score[:, fold - 1:fold] = network_pArg.predict(x)

        predict_average_score.append(np.average(predict_score, axis=1))
    elif type =='H':
        network_His = DeeppHis()

        for fold in folds:
            modelName = 'Fold' + str(fold) + '.h5'
            modelpath = p+"\\statics\\Hmodels\\%s" % modelName
            network_His.load_weights(modelpath)
            predict_score[:, fold - 1:fold] = network_His.predict(x)
        predict_average_score.append(np.average(predict_score, axis=1))
    predict_average_score=np.array(predict_average_score).reshape(-1)
    for i in predict_average_score:
        if i >= 0.85:
            predict_result.append(1)
            predict_confidence.append('Very High confidence')
        elif i >= 0.7:
            predict_result.append(2)
            predict_confidence.append('High confidence')
        elif i >= 0.5:
            predict_result.append(3)
            predict_confidence.append('Medium confidence')
        else:
            predict_result.append(0)
            predict_confidence.append('No')
    result = pd.DataFrame({'Protein': name, 'Position': position, 'Sequence': dataframe['Sequence'],
                           'Score': predict_average_score, 'Prediction': predict_confidence})
    '''saveCsv = pd.DataFrame({'Protein': name, 'Position': position, 'Sequence': dataframe['Sequence'],
                           'Prediction score': predict_average_score, 'Prediction category': predict_confidence})
    saveCsv.to_csv(path, index=None)'''

    return result
