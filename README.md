# Berkeley and Christian Algorithm Implementation in Python

## Description
This project implements the Berkeley and Christian algorithms in Python for clock synchronization in distributed systems. The Berkeley algorithm is used to synchronize the clocks of multiple nodes by calculating the average time among them, while the Christian algorithm synchronizes clocks by obtaining the time from a trusted time server.

## Berkeley Algorithm Implementation
The `node.py` file contains the implementation of the Berkeley algorithm. It consists of a `Node` class that can act as both a server and a client. Each node communicates with other nodes to synchronize their clocks using a barrier for synchronization.

## Christian Algorithm Implementation
The christian folder has two files `server.py`   `client.py` file contains the implementation of the Christian algorithm. 

## Usage
To run the code, execute the following command in the terminal:

`python berkeley.py [server/client]`


Replace `[server/client]` with either `server` or `client` to specify the role of the node.

## Requirements
- Python 3.x
- mpi4py library (for communication between nodes)

**Note:** Ensure that MPI is installed and properly configured on each system in the cluster. Adjust the hostfile and network settings as needed for communication between nodes.

## Contributors
- [Your Name]

## License
This project is licensed under the [license name]. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Special thanks to [mentor/supervisor name] for guidance and support.
- Inspired by [source of inspiration, if any].
