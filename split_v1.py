files_train = {'cv1':[], 'cv2':[], 'cv3':[], 'cv4':[], 'cv5':[]}
m = 0
for k in files_train.keys():
    for j in range(len(splits['digit']['train'][m])):
        if list(splits['digit']['train'][m])[j]<10:
            a = 'audio-mnist/data/0' + str(list(splits['digit']['train'][m])[j])
        else:
            a = 'audio-mnist/data/' + str(list(splits['digit']['train'][m])[j])  
        files_train[k].append([y for y in files if y.startswith(a)]) 
    m += 1    
    
files_validate = {'cv1':[], 'cv2':[], 'cv3':[], 'cv4':[], 'cv5':[]}
m = 0
for k in files_validate.keys():
    for j in range(len(splits['digit']['validate'][m])):
        if list(splits['digit']['validate'][m])[j]<10:
            b = 'audio-mnist/data/0' + str(list(splits['digit']['validate'][m])[j])
        else:
            b = 'audio-mnist/data/' + str(list(splits['digit']['validate'][m])[j])  
    m += 1
    files_validate[k].append([w for w in files if w.startswith(b)]) 
    

files_test = {'cv1':[], 'cv2':[], 'cv3':[], 'cv4':[], 'cv5':[]}
m = 0
for k in files_test.keys():
    for j in range(len(splits['digit']['test'][m])):
        if list(splits['digit']['test'][m])[j]<10:
            c = 'audio-mnist/data/0' + str(list(splits['digit']['test'][m])[j])
        else:
            c = 'audio-mnist/data/' + str(list(splits['digit']['test'][m])[j])  
    m += 1
    files_test[k].append([z for z in files if z.startswith(c)]) 
