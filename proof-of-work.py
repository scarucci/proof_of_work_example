# example of proof-of-work algorithm (inspired by Andreas Antonopolous)

import haslib
import time

max_nonce = 2 ** 32 # which equals to 4 billion

def proof_of_work(header, difficulty_bits):

    # difficulty target
    target = 2 ** (256-difficulty_bits)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        # validity of result
        if long(hash_result, 16) < target:
            print "Success with nonce %d" % nonce
            print "Hash is %s" % hash_result
            return (hash_result, nonce)

    print "Failed after %d (max_nonce) tries" % nonce
    return nonce

if __name__ == '__main__':

    nonce = 0
    hash_result = ''

    # 0 to 31 bits difficulty
    for difficulty_bits in range(32):

        difficulty = 2 ** difficulty_bits
        print "Difficulty %1d (%d bits)" % (difficulty, difficulty_bits)

        print "Beginning search.."

        # timestamp

        start_time = time.time()


        # create block which implements previous hash
        new_block = 'test block with transaction' + hash_result

        # find new valid nonce
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # timestamp of the lapse it took to figure out a result
        end_time = time.time()

        elapsed_time = end_time - start_time
        print "Elapsed time: %.4 seconds" % elapsed_time

        if elapsed_time > 0:

            # hashes per second (estimate)
            hash_power = float(long(nonce)/elapsed_time)
            print "Hashing power: %1d hashes per second" % hash_power
