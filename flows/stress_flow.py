from multiprocessing import Pool
from multiprocessing import cpu_count
import time
from prefect import flow, get_run_logger
from prefect_dataops.deployments import deploy_to_s3


def multiply_a_lot(x):
    set_time = 5
    timeout = time.time() + 60 * float(set_time)
    while True:
        if time.time() > timeout:
            break
        x * x


@flow
def run_stress_test():
    processes = cpu_count()
    logger = get_run_logger()
    logger.info("utilizing %d cores\n", processes)
    pool = Pool(processes)
    pool.map(multiply_a_lot, range(processes))


deploy_to_s3(run_stress_test)
