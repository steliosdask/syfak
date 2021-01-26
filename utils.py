
def csvtoexcel(cf):
    cf = cf.loc[(cf['ΠΕΡΙΓΡΑΦΗ'] == '="ΜΕΛΟΣ"') | (cf['ΠΕΡΙΓΡΑΦΗ'] == '="ΜΗ ΜΕΛΟΣ-ΦΑΡΜΑΚΕΙΟ"')]

    cf = cf[['ΠΕΡΙΓΡΑΦΗ', 'ΚΩΔ. ΠΕΛΑΤΗ', 'ΕΠΩΝΥΜΙΑ', 'ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ', 'ΓΑΛΑΤΑ ΤΖΙΡΟΣ']].sort_values(['ΠΕΡΙΓΡΑΦΗ', 'ΕΠΩΝΥΜΙΑ'])

    cf = cf.drop(columns=['ΠΕΡΙΓΡΑΦΗ'])
    cf = cf.drop(cf.index[0])
    titlestofloat = ['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ','ΓΑΛΑΤΑ ΤΖΙΡΟΣ']
    for i in titlestofloat:
        cf[i] = cf[i].str.replace(',', '.').astype(float)
    titlesvalues = ['ΚΩΔ. ΠΕΛΑΤΗ','ΕΠΩΝΥΜΙΑ']
    for j in titlesvalues:
        cf[j] = cf[j].str.replace('[=,"]', '')

    cf['ΣΥΝΟΛΟ'] = cf.iloc[:, 2:5].sum(axis=1)
    return cf





    ''' cf['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'] = cf['ΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
        cf['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'] = cf['ΠΑΡΑΦΑΡΜΑΚΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
        cf['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'] = cf['ΓΑΛΑΤΑ ΤΖΙΡΟΣ'].str.replace(',', '.').astype(float)
         
        cf['ΚΩΔ. ΠΕΛΑΤΗ'] = cf['ΚΩΔ. ΠΕΛΑΤΗ'].str.replace('[=,"]', '')
        cf['ΕΠΩΝΥΜΙΑ'] = cf['ΕΠΩΝΥΜΙΑ'].str.replace('[=,"]', '')'''
