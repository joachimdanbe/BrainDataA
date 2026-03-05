Functional magnetic resonance imaging (FMRI) data typically has many
time series, which were acquired across the brain, while a subject was
involved in a task.  For example, it is common to have the subject do
a task for some time, then pause for a bit, then do a task, then
pause, etc.  Blood oxygen level dependent changes are measured, and
those can be correlated with the timing that the subject was doing the
task.  As a rough approximation of which part of the brain was
engaged, we can correlate the "ideal" pattern of a response with the
actual measured ones, using correlation.

In the attached (download all 3 files and put them in the same
directory), you are given 2 text files of data and one "starter"
python program that has functions to read in the data to two arrays:

+ the data array has 3 dimensions, 2 of spatial extent and one of time.
+ the refwav array has 1 dimension, of time.

The time axis in data has the same length as in refwav. The sampling
time of Ts=2.5 s is also given. The program shows the mean of each
time series in data using Matplotlib's imshow() function.






