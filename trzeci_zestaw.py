def deleting_strings():
    infile = r'C:\Users\student\Pictures\testin.txt'
    outfile = r'C:\Users\student\Pictures\testout.txt'

    delete_list = ["sie", "oraz", "nigdy", "dlaczego", " i "]
    with open(infile) as filein, open(outfile, "w+") as fileout:
        for line in filein:
            for word in delete_list:
                line = line.replace(word, "")
            fileout.write(line)

def replacing_strings():
    infile = r'C:\Users\student\Pictures\testin.txt'
    outfile = r'C:\Users\student\Pictures\testout.txt'

    delete_dict = {
        "oraz" : " i ",
        "nigdy" : " prawie nigdy ",
        "dlaczego" : " czemu ",
        " i " : " oraz "
    }
    with open(infile) as filein, open(outfile, "w+") as fileout:
        for line in filein:
            for word in delete_dict:
                line = line.replace(word, delete_dict[word])
            fileout.write(line)

replacing_strings();