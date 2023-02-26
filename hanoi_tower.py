def Hanoi_tower(n,source,destination,aux):
    if n==1:
        #agar faghat ye disk dashte bashim ba enteghal be destination tamoome!!
        print('Move disk 1 from source',source,'to destination',destination)
        return

    #in mige ke be komake mile destination n-1 disk e ma montaghel beshan be
    # mile aux;yani func ke var migire destination esh mishe hamoon mile aux!
    Hanoi_tower(n-1,source,aux,destination)

    # inja mige ke hame disk ha ke montaghel shodan be aux akharin disk
    # ke hamoon n om bashe montaghel mishe be destination e ma
    print('Move disk',n,'from source',source,'to destination',destination)

    #bad az inke akharin disk(disk n om) raft be destination,disk haye roo
    # aux be komake mile source va avalie montaghel beshan be destination!!!
    Hanoi_tower(n-1,aux,destination,source)

Hanoi_tower(4,'A','C','B')