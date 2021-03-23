

import os
import sys
import platform


def genome_splitter(genomes):
    genomes = genomes.split('>')

    for index, gene_and_tag in enumerate(genomes):
        if index == 0:
            pass
        else:
            gene_and_tagplain = gene_and_tag
            gene_and_tag = gene_and_tag.split('|')
            a = gene_and_tag[2].replace('/', '_')
            with open("infl/" + str(a) + ".fasta", 'w') as wr:

                wr.write('>'+''.join(gene_and_tagplain))
                wr.flush()
                wr.close()
    print("splitting is DONE!")


def get_genome_file():
    filepath = ''

    if platform.platform()[:7] == 'Windows':
        print('Operating System: ' + str(platform.platform()))
        files = os.listdir(os.getcwd())
        print("try to find ...")
        for i in files:
            if os.path.splitext(i)[1] == '.fasta':
                print("found the genome file")
                filepath = os.getcwd() + '\\' + i
                break
            else:
                pass

        if filepath == '':
            print("Couldn't find it! check the genome files in the path")
            sys.exit(0)

        else:
            return open(filepath, 'r')

    else:
        print('Operating System: ' + str(platform.platform()))
        files = os.listdir(os.getcwd())
        file_list = []
        print("try to find ...")
        for i in files:
            if os.path.splitext(i)[1] == '.fasta':
                print("found the genome file")
                filepath = os.getcwd() + '/' + i
                break
            else:
                pass

        if filepath == '':
            print("Couldn't find it! check the genome files in the path")
            sys.exit(0)

        else:
            return open(filepath, 'r')


genes = get_genome_file().read()
genome_splitter(genes)
