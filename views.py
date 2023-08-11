from calculate import judge_fasta,get_peptide,core
import time
import os
def predict(file,peptide,types):
    path=[]
    p=os.getcwd()
    if peptide!='':
        with open(p+'\\statics\\userpep\\inputpep.fasta', 'w') as f:
            f.write(peptide)
        path=p+'\\statics\\userpep\\inputpep.fasta'

    else:
        path = file


    filetype = judge_fasta(path)

    if filetype:

        dataframe = get_peptide(path,types)
        if len(dataframe) > 0:
            predict_result = core(dataframe,types)
            ppp=predict_result
            if len(predict_result) > 1000000000000:
                return_result = predict_result[:len(predict_result)]
            else:
                 return_result = predict_result
            items = []
            line = {}
            for i in range(len(return_result)):
                line['protein'] = list(return_result['Protein'])[i]
                line['position'] = list(return_result['Position'])[i]
                line['sequence_l'] = list(return_result['Sequence'])[i][:18]
                line['sequence_19'] = list(return_result['Sequence'])[i][18]
                line['sequence_r'] = list(return_result['Sequence'])[i][19:]
                line['score'] = list(return_result['Score'])[i]
                line['prediction'] = list(return_result['Prediction'])[i]
                items.append(line.copy())

            itemss = []
            lines = {}
            for i in range(len(ppp)):
                lines['protein'] = list(ppp['Protein'])[i]
                lines['position'] = list(ppp['Position'])[i]
                lines['sequence_l'] = list(ppp['Sequence'])[i][:18]
                lines['sequence_19'] = list(ppp['Sequence'])[i][18]
                lines['sequence_r'] = list(ppp['Sequence'])[i][19:]
                lines['score'] = list(ppp['Score'])[i]
                lines['prediction'] = list(ppp['Prediction'])[i]
                itemss.append(lines.copy())
            return items,itemss
        else:
            if type=='K':
                return 10,11
            elif type=='H':
                return 20,21
            else:
                return 30,31
    else:
        return  0,1



