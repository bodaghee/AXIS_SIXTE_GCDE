# AXIS_SIXTE_GCDE
## Shell and Python Scripts for Simulating a Galactic Center Deep Exposure with AXIS

The notebook describes an end-to-end simulation of a GCDE with AXIS using the SIXTE software package. 

This includes: 
* making a source catalog and spectra; 
* making an image for the diffuse background emission; 
* making SIMPUT files; 
* making events files, images (including an RGB-like image), and an exposure map; 
* finding sources with wavdetect; 
* and extracting spectra.

The instructions are for Shell scripts since it's the language used in the SIXTE documentation, which makes it easier for first-timers. I also included their equivalent Python scripts since that's what I prefer.
