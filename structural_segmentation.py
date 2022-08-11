# Simple MSAF example
from __future__ import print_function
import msaf

# 1. Select audio file
#
#audio_file = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/ezhel bul benı.wav"

def str_segmentation_function(audio_file):
    # 2. Segment the file using the default MSAF parameters (this might take a few seconds)
    boundaries, labels = msaf.process(audio_file, boundaries_id="sf", labels_id="fmc2d")
    return boundaries

"""
    print('Estimated boundaries:', boundaries)

    print("labels", labels)

    # 3. Save segments using the MIREX format
    out_file = 'segments.txt'
    print('Saving output to %s' % out_file)
    msaf.io.write_mirex(boundaries, labels, out_file)

    # 4. Evaluate the results
    try:
        evals = msaf.eval.process(audio_file)
        print(evals)
    except msaf.exceptions.NoReferencesError:
        file_struct = msaf.input_output.FileStruct(audio_file)
        print("No references found in {}. No evaluation performed.".format(file_struct.ref_file))


str_segmentation_function(audio_file)
print(msaf.get_all_boundary_algorithms())
print(msaf.get_all_label_algorithms())
"""

"""
boundary_algorithms()
'cnmf'      This script identifies the structure of a given track using a modified version
'vmo'       This script identifies the structure of a given track using the Variable
'olda'      This class implements the algorithm described here:
'sf'        This script identifies the boundaries of a given track using the Serrà
'scluster'  This script identifies the boundaries of a given track using the Spectral
'foote'     This script identifies the boundaries of a given track using the Foote

label_algorithms()
'cnmf'      This script identifies the structure of a given track using a modified version
'vmo'       This script identifies the structure of a given track using the Variable
'scluster'  This script identifies the boundaries of a given track using the Spectral
'fmc2d'     This method labels segments using the 2D-FMC method described here:
"""
