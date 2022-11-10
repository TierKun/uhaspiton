import sys
import base64

exitmsg = 'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KVGhhbmtzIEZvciBVc2UgVGhpcyBUb29scwpCeSA6IEB0aWVya3Vubl8gKFRpZXIgU2lueW8pCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0='

temp_list = ['mada 80', 'sinyo 100', 'bebek 90']
#membuat menu
def menu():
    print ('Edit Daftar Nilai UAS PK X TM B')
    print ('1. Daftar Nilai\n2. exit') #pilihan menu
    
    pilih = input ('pilih menu : ') #input pilihan menu
    if (pilih == '1' or pilih.lower() == 'daftar nilai'):
        tanya()
    elif (pilih == '2' or pilih.lower() == 'exit'):
        exit()
        
#
def tanya():
    tanya=input('Tambah/hapus/selesai?')
    if (tanya.lower() =='tambah'):
        daftar_add()
    elif (tanya.lower() =='hapus'):
        daftar_delete() 
    elif (tanya.lower() =='selesai'):
        printdaftar()
     
def daftar_add():
    kamu_nanyahh = input('(nama)<spasi>(nilai): ')
    temp_list.append(kamu_nanyahh)
    tanya()
   
def daftar_delete():  
    kamu_nanyahhh = input('(nama)<spasi>(nilai): ')
    try:
        temp_list.remove(kamu_nanyahhh)
    except:
        print(f'ga iso bro, {kamu_nanyahhh} ra ketemu...')
        tanya()
        
def printdaftar():
    print ('Daftar Nama & Nilai:')
    for i in temp_list:
        print (i)
     
def exit():
    base64_bytes = exitmsg.encode("ascii") #encode base64 (anti recode exit message:v)
    string_bytes = base64.b64decode(base64_bytes)
    encode_exit = string_bytes.decode("ascii")
    sys.exit(encode_exit)
    
if __name__=='__main__':
    menu()    