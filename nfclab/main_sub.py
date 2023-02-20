from classes import MyCardReader 

if __name__ == '__main__':
    cr = MyCardReader.MyCardReader()

    cr.read_id_stab()
    print(cr.idm)
