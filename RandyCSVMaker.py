import PySimpleGUI as sg
import pandas as pd
import os

def writeCSV(contentList, path):
    with open(path+'/IP-Output.csv', 'w') as file:
        for line in contentList:
            file.write(line+'\n')

def printCSVFile(path, savePath):
    df = pd.read_csv(path)
    print(path)
    contentList = ['Station Index,Equipment Type,IP,Subnet Mask,Gateway']

    for mrnumber in df['Station Index']:
        if str(df.loc[df['Station Index']==mrnumber]['COMIP'].values[0])[0]=='1':

            comIP = df.loc[df['Station Index']==mrnumber]['COMIP'].values[0]
            if comIP[-2]=='.':
                subNet = df.loc[df['Station Index']==mrnumber]['Subnet Mask'].values[0]
                ir829IP = comIP[:-1] + str(int(comIP[-1:])+1)
                upsIP = comIP[:-1] + str(int(comIP[-1:])+2)
                ebcsIP = comIP[:-1] + str(int(comIP[-1:])+3)
                smarcIP = comIP[:-1] + str(int(comIP[-1:])+4)
                ipsla = comIP[:-1] + str(int(comIP[-1:])+5)

            elif comIP[-3]=='.':
                subNet = df.loc[df['Station Index']==mrnumber]['Subnet Mask'].values[0]
                ir829IP = comIP[:-2] + str(int(comIP[-2:])+1)
                upsIP = comIP[:-2] + str(int(comIP[-2:])+2)
                ebcsIP = comIP[:-2] + str(int(comIP[-2:])+3)
                smarcIP = comIP[:-2] + str(int(comIP[-2:])+4)
                ipsla = comIP[:-2] + str(int(comIP[-2:])+5)

            elif comIP[-4]=='.':
                subNet = df.loc[df['Station Index']==mrnumber]['Subnet Mask'].values[0]
                ir829IP = comIP[:-3] + str(int(comIP[-3:])+1)
                upsIP = comIP[:-3] + str(int(comIP[-3:])+2)
                ebcsIP = comIP[:-3] + str(int(comIP[-3:])+3)
                smarcIP = comIP[:-3] + str(int(comIP[-3:])+4)
                ipsla = comIP[:-3] + str(int(comIP[-3:])+5)


            
            singleList = [str(mrnumber) + ',IR829,' + ir829IP + ',' + subNet + ',' + comIP,
                str(mrnumber) + ',UPS,' + upsIP + ',' + subNet + ',' + ir829IP,
                str(mrnumber) + ',EBCS,' + ebcsIP + ',' + subNet + ',' + ir829IP,
                str(mrnumber) + ',SMARC,' + smarcIP + ',' + subNet + ',' + ir829IP,
                str(mrnumber) + ',SLA,' + ipsla + ',' + subNet + ',' + comIP]

            contentList.extend(singleList)
        else:
            print(str(mrnumber)+' skiped because it superloops')

    writeCSV(contentList, savePath) 

    return



# All the stuff inside your window.
layout = [ [sg.Text("Choose a csv file:\t\t"), sg.Input(key="-CSVPATH-" ,change_submits=True), sg.FileBrowse(key="-IN-", file_types=(("CSV Files", "*.csv"),))],
           [sg.Text("Choose a where to save:\t"), sg.Input(key="-SAVEPATH-" ,change_submits=True), sg.FolderBrowse(key="-IN3-")],
            [sg.Button('Generate CSV'), sg.Exit()]
]

# Create the Window
window = sg.Window('EBCS Config Writer', layout).Finalize()

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    elif event == 'Generate CSV':
        printCSVFile(values['-CSVPATH-'], values['-SAVEPATH-'])

window.Close()
