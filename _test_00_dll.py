from decoder import *
from types import *
from ctypes import cast
import time

def Test_Deinterleve_16Bytes_to_2x8Bytes():
    arr_in = (BYTE * 16)(1,11,2,22,3,33,4,44,5,55,6,66,7,77,8,88)
    
    for b in arr_in:
        print(b)
    
    Deinterleve_16Bytes_to_2x8Bytes(arr_in,1)

    print()
    for b in arr_in:
        print(b)


def Test_TransposeByte8x8():

    print ()
    print ("TransposeByte8x8")
    a = [   0b00000001, 
            0b10000001, 
            0b00000001, 
            0b10000000, 
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b00000000,
           ]

    arr = (BYTE * len(a))(*a)
    brr = (BYTE * len(a))(*a)
    
    print ("\ninput")
    for i,b in enumerate(arr):     
        if (i%8)==0:
            print()
        print ((('{0:08b}'.format(0x0ff & b)).replace('0','-')))

    TransposeByte8x8(arr,brr)

    print ("\noutput")
    for i,b in enumerate(brr):     
        if (i%8)==0:
            print()
        print ((('{0:08b}'.format(0x0ff & b)).replace('0','-')))

        

def Test_TransposeBits_16xI8_to_8xI16():
    
    print ()
    print ("Test_TransposeBits_16xI8_to_8xI16")
    
    arr_in = [   
            0b11111111, 
            0b10000000, 
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b00000000,
            0b00000000,
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b11000000, 
            0b11000000, 
            0b11000000, 
            0b11000000,
            
            0b11111111, 
            0b10000000, 
            0b10000000, 
            0b10000000, 
            0b00000000, 
            0b00000000, 
            0b00000000, 
            0b00000000,
            0b00000000,
            0b00000000, 
            0b00000000, 
            0b00000001, 
            0b00000001, 
            0b00010001, 
            0b00010001, 
            0b00010001,
            ]
    
    chunk_nr = len(arr_in)//16
    
    arr_in_p= (BYTE * len(arr_in))(*arr_in)    
    
    for i,b in enumerate(arr_in_p):
        if (i%8)==0:
            print()
        print ((('{0:08b}'.format(0x0ff & b)).replace('0','-')))
    
    TransposeBits_16xI8_to_8xI16(arr_in_p,2)
    
    arr_in_p = cast(arr_in_p, POINTER(WORD))
    
    print()
    for i in range(16):
        if (i%8)==0:
            print()
        print ((('{0:016b}'.format(0x0ffFF & arr_in_p[i])).replace('0','-')))

def Test_TransposeBits_16xI8_to_8xI16_perform():
    
    print ()
    print ("Test_TransposeBits_16xI8_to_8xI16")
    
    
    arr= (BYTE * (16*3670016))()    
    
    _ = time.time()
    TransposeBits_16xI8_to_8xI16(arr,len(arr)//16)
    print(time.time() - _)
    
#    arr_in_p = cast(arr_in_p, POINTER(WORD))

def Test_Deinterleve_14x8Words_to_8x14Words():
    
    arr_in = (WORD * (2*14*8))(0)
    
    
    for c in range(1,3):
        for j in range(1,15):
            for i in range(8):
                arr_in[((c-1)*14*8)+((j-1)*8)+i]=(c*1000)+(j*10)+i
            
    for b in arr_in:
        print(b)
    
    Deinterleve_14x8Words_to_8x14Words(arr_in,2)
    
    print()
    for b in arr_in:
        print(b)

def Test_TransposeBits_14xI16_to_16xI16():
    
    print ()
    print ("Test_TransposeBits_16xI8_to_8xI16")
    
    arr_in = [   
            0b1010000000001001, 
            0b1000000000000000, 
            0b1000000000000000, 
            0b0000000000000000, 
            0b0000000000000000, 
            0b0000000000000000, 
            0b1111000000000000, 
            0b0000000000000000,
            0b0000000000000000,
            0b0000000000000000, 
            0b0000000000000001, 
            0b0000000000000001, 
            0b0000000000011111, 
            0b0000000000000011, 
            
            0b1000000000001001, 
            0b1000000000000000, 
            0b1000000000000000, 
            0b1000000000000000, 
            0b0000000000000000, 
            0b0000000000000000, 
            0b0000000000001100, 
            0b0000000000000000,
            0b0000000000000000,
            0b0000000000000000, 
            0b0000000000000000, 
            0b1000000000000011, 
            0b1000000000000011, 
            0b1000000000000011, 
            
            ]
    
    chunk_nr = len(arr_in)//14
    
    arr_in= (WORD * (chunk_nr*14))(*arr_in)
    arr_out= (WORD * (chunk_nr*16))() 
    
    for i,b in enumerate(arr_in):
        if (i%14)==0:
            print()
        print ((('{0:014b}'.format(0x3fff & b)).replace('0','-')))
    
    TransposeBits_14xI16_to_16xI16(arr_in,arr_out,chunk_nr)
        
    print()
    for i,b in enumerate(arr_out):
        if (i%16)==0:
            print()
        print ((('{0:016b}'.format(0xffff & b)).replace('0','-')))
    
def Test_TransposeWords16x16():

    print ()
    print ("Test_TransposeWords16x16")
    a = [   0b0000000111001010, 
            0b1000000100000001, 
            0b0000000101010101, 
            0b1000000011001101, 
            0b0000000000001100, 
            0b0000000000000000, 
            0b0000000000000000, 
            0b0000000000000000,
            0b1111111111111111,
            0b1111111100000000,
            0b0011001100110011,
            0b0000000000000000,
            0b0000000000000000,
            0b1111111111111111,
            0b1011100011101010,
            0b0000000000000000,
           ]

    arr = (WORD * len(a))(*a)
    brr = (WORD * len(a))(*a)
    
    print ("\ninput")
    for i,b in enumerate(arr):     
        if (i%16)==0:
            print()
        print ((('{0:16b}'.format(0xffff & b)).replace('0','-').replace(' ','-')))

    TransposeWords16x16(arr,brr)

    print ("\noutput")
    for i,b in enumerate(brr):     
        if (i%16)==0:
            print()
        print ((('{0:16b}'.format(0xffff & b)).replace('0','-').replace(' ','-')))