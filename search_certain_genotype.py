f1 =  open("Snps_Candidates.Genmod.WES.genotypes", "r")
f2 = open("Snps_Canditates_Genmod.WES.genotypes.carriers", "w")

while True:
    line = f1.readline()
    if not line:
        break
    info = line.split()
    for i in range(5, len(info)):
        if info[2]+"/"+info[2] in info[i].split(":",1)[1] and len(info[i].split(":",1)[1]) <= 3:
            out1 = info[2]+"/"+info[2],info[i]
            #print type(info[2]+"/"+info[2])
        else:
            out = "\t".join((info[0],info[1],info[4],info[i]))
            f2.write(out+"\n")

