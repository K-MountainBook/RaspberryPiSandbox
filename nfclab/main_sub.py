from classes import MyCardReader 

if __name__ == '__main__':
    print('Hello world!!')
    cr = MyCardReader.MyCardReader()

    cr.read_id_stab()
    print(cr.idm)
