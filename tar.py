import os, tarfile, sys


if sys.argv[1] == 'c':

    fd_1 = os.open(sys.argv[2], os.O_RDONLY)
    fd_2 = os.open(sys.argv[3], os.O_RDONLY)

    fd_1_bytes = os.read(fd_1, 10000)
    fd_2_bytes = os.read(fd_2, 10000)


    s = '\nthis is the break between files. \n\n'
    line = str.encode(s)

    output = os.open(sys.argv[4], os.O_RDWR | os.O_CREAT)
    os.write(output, fd_1_bytes + line + fd_2_bytes)


    os.close(fd_1)
    os.close(fd_2)
    os.close(output)


elif sys.argv[1] == 'x':

    fd_zip = os.open(sys.argv[2], os.O_RDONLY)
    fd_zip_bytes = os.read(fd_zip, 10000)


    file_1 = os.open('file_1', os.O_RDWR | os.O_CREAT)
    file_2 = os.open('file_2', os.O_RDWR | os.O_CREAT)


    os.write(file_1, fd_zip_bytes.split(b'\nthis is the break between files. \n\n')[0])
    os.write(file_2, fd_zip_bytes.split(b'\nthis is the break between files. \n\n')[1])


    os.close(fd_zip)
    os.close(file_1)
    os.close(file_2)



    
    
else:
    print("First system argument is not c or x. Try again.")
