import hashlib
import time
import statistics

def read_file():
    afile = open("MobyDickFulltxt.txt", 'rb').read()
    return afile


def test_hash(fp):
    hasher = hashlib.sha1()
    final = " "
    for word in fp.split():
        hasher.update(word)
        x = hasher.digest()
        x_str = x.decode("ISO-8859-1")
        final = final + x_str
    return final
    #print(len(final_a))

def write_file(array):
    fp = open("test_file_test.txt", 'w')
    for i in range(len(array)):
        fp.write(array[i])
    fp.close()


def loop_func():
    array_o_bytes = []
    for i in range(1):
        x = test_hash(read_file())
        array_o_bytes.append(x)
    print(len(array_o_bytes))
    return array_o_bytes


def test_functs():
    total_time = []
    hash_time = []
    write_time = []
    read_time = []

    for i in range(10):
        tt0 = time.time()
        #a = loop_func()

        tr0 = time.time()
        fp = read_file()
        tr1 = time.time()

        th0 = time.time()
        a = test_hash(fp)
        th1 = time.time()

        tw0 = time.time()
        write_file(a)
        tw1 = time.time()

        tt1 = time.time()

        read_time.append(tr1-tr0)
        hash_time.append(th1-th0)
        write_time.append(tw1-tw0)
        total_time.append(tt1-tt0)

    print('\tMEAN of read time ', statistics.mean(read_time))
    print('\tMEAN of hash function time ', statistics.mean(hash_time))
    print('\tMEAN of Write time ', statistics.mean(write_time))
    print('\tMEAN of total time ', statistics.mean(total_time))

    print("Total Time:", total_time)

def main():
    test_functs()

main()
