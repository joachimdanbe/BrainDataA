import numpy as np
import matplotlib.pyplot as plt


# ==========================================================================
# background functions: provided to read data

def read_in_dataset(fname):
    """
Parameters
----------
fname_dat : str
    filename of data (of the particular dimensions included in this function)

Returns
-------
data : np.ndarray
    3D array of data, representing a slice of data (first 2 coords) and a time
    series at each location (3rd dimension)
"""

    # read in: brain time series data
    fff = open(fname, "r")
    X = fff.readlines()
    fff.close()
    brain = [line.split() for line in X]

    # dimensions of brain data (slice + time)
    N = 144
    dimx = 70-11+1
    dimy = 74-8+1

    # brain data: initialize+populate
    data = np.zeros((dimx,dimy,N))
    n = 0
    for j in range(0,dimy):
        for i in range(0,dimx):
            for k in range(0,N):
                # don't need these coord values, but just keep track
                x = brain[n][0]
                y = brain[n][1]
                z = brain[n][2]
                data[i,j,k] = brain[n][3+k]
            n+=1

    Nx, Ny, Nt = np.shape(data)

    print("++ Read in data array with dimensions: {}, {}, {}\n"
          "   The first two are spatial dimensions, and the third is time."
          "".format(Nx, Ny, Nt))

    return data

def read_in_refwav(fname):
    """Read in a file fname that contains a single reference time series.

Parameters
----------
fname_ref : str
    filename of reference wave (of particular len included in this function)

Returns
-------
refwav : np.ndarray
    1D array of data, representing reference time series
"""

    # read in: brain time series data
    fff = open(fname, "r")
    X = fff.readlines()
    fff.close()
    boxcar = [line.split() for line in X]

    # dimensions of reference wave (number of time points)
    N = len(boxcar)

    # make refwav
    refwav = np.zeros(N)
    for k in range(0,N):
        refwav[k] = boxcar[k][0]

    print("++ Read in reference time series of length: {}"
          "".format(N))

    return refwav

# =========================================================================

if __name__ == "__main__":
    
    # read in a slice of FMRI data (3D array): first 2 dims are
    # spatial indices, and third is index of time points
    data = read_in_dataset("AIMSftap.dat")
    Nx, Ny, Nt = np.shape(data)

    # the sampling time for this data
    Ts = 2.5

    # read in a reference time series (1D array)
    refwav = read_in_refwav("Ref.1D")
    L = len(refwav)    

    data_mean = np.zeros((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            data_mean[i,j] = np.mean(data[i,j,:])

    plt.imshow(data_mean)
    plt.show()
