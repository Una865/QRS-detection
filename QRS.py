import os
import sys
from util.QRS_util import*
import pywt
import wfdb

'''
QRS detection demo 
@author: Kemeng Chen: kemengchen@email.arizona.edu
'''

def QRS_test():
	'''
	QRS detection on file_name
	assuming 360 Hz sampling rate, may not work with very low sampling rate signal
	args:
		file_name: file containing ecg data in one column
	'''
	fs=360
	#file_path=os.path.join(os.getcwd(), 'data', file_name)
	#if not os.path.isfile(file_path):
		#raise AssertionError(file_path, 'not exists')
	#ecg=read_ecg(file_path)
	signals, fields= wfdb.rdsamp('mitdb/200')
	
	R_peaks, S_pint, Q_point=EKG_QRS_detect(signals[:,0], fs, False, True)

if __name__ == '__main__':
	
	QRS_test()
