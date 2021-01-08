import os

def set_environment_variables():
    os.environ["MASTER_ADDR"] = os.environ["AZ_BATCHAI_MPI_MASTER_NODE"]
    os.environ["MASTER_PORT"] = "6105"
    os.environ["NODE_RANK"] = os.environ[
        "OMPI_COMM_WORLD_RANK"
    ]  # node rank is the world_rank from mpi run
    print("MASTER_ADDR = {}".format(os.environ["MASTER_ADDR"]))
    print("MASTER_PORT = {}".format(os.environ["MASTER_PORT"]))
    print("NODE_RANK = {}".format(os.environ["NODE_RANK"]))

