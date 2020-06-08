import math
import random
import time
import sys
import ray


#ray.init(address="auto")
def sample(num_samples):
    num_inside = 0
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.hypot(x, y) <= 1:
            num_inside += 1
    return num_inside


def approximate_pi_distributed(num_samples):
    from ray.util.multiprocessing.pool import Pool  # NOTE: Only the import statement is changed.
    pool = Pool()

    start = time.time()
    num_inside = 0
    sample_batch_size = 100000
    for result in pool.map(
            sample,
        [sample_batch_size for _ in range(num_samples // sample_batch_size)]):
        num_inside += result

    print("pi ~= {}".format((4 * num_inside) / num_samples))
    print("Finished in: {:.2f}s".format(time.time() - start))


if __name__ == "__main__":
    print(sys.argv[1:])
    input = sys.argv[1]
    print(input)
    res = approximate_pi_distributed(int(input))
