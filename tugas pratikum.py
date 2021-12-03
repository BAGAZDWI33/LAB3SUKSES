data=[]
while True:
     nama=input("masukan nama lengkap anda: ")  
     nim=input("masukan NIM anda: ")
     tugas=int(input("masukan nilai tugas: "))
     uts=int(input("masuian nilai UTS: "))
     uas=int(input("masukan nilai UAS: "))
     na=(int(tugas)*.30)+(int(uts)*.35)+(int(uas)*.35)
     data.append([nama,nim,tugas,uts,uas,na])
     lanjut=input("tambah data?(y/t)")
     if lanjut=="t"or lanjut=="T":
         print("data mahasiswa")
         print("=======================================================================================================")
         print("|\tNO\t|\tNAMA\t|\tNIM\t|\tTUGAS\t\t|\tUTS\t|\tUAS\t|\tAKHIR\t")
         print("=======================================================================================================")
         for x in data:
             print("|\t1\t|\tAri\t|\t1234\t|\t70\t\t|\t65\t|\t80\t|\t72.0\t|")
             print("|\t2\t|\tBambang\t|\t2345\t|\t65\t\t|\t80\t|\t90\t|\t81.0\t|")
             print("==================================================================================================")
         else:       
           break

                   