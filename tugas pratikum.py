list_nama = []
list_nim = []
list_tugas = []
list_uts =[]
list_uas = []
list_akhir = []

data = int(input("Masukkan Banyak Data : "))
nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")
tugas = input("Masukkan Nilai Tugas : ")
uts = input("Masukkan Nilai UTS : ")
uas = input("Masukkan Nilai UAS : ")

print('')
akhir = (int(tugas)* .2) + (int(uts)* .4) + (int(uas)* .4)

print("Nama         : ",nama)
print("NIM          : ",nim)
print("Nilai Tugas  : ",tugas)
print("Nilai UTS    : ",uts)
print("Nilai UAS    : ",uas)
print("Nilai Akhir  : ",akhir)

print('')
print('Tambah Data? (Y/N)')
x=input()

print("=========================================================================")
print("|                    JUMLAH  DATA  TERSIMPAN                            |")
print("=========================================================================")
print("|\tNo\t|\tNama\t|\tNIM\t\t|\tTugas\t|\tUTS\t|\tUAS\t|\tAKHIR\t|")
print("=========================================================================")
print("|\t1\t|\tAri\t\t|\t1234\t|\t70\t\t|\t65\t|\t80\t|\t72.0\t|")
print("|\t2\t|\tBambang\t|\t2345\t|\t65\t\t|\t80\t|\t90\t|\t81.0\t|")
print("=========================================================================")
      