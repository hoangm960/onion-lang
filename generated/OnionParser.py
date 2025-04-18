# Generated from grammar/Onion.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
<<<<<<< HEAD
        4,1,43,318,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
=======
        4,1,43,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
>>>>>>> 999756586236c54f54652a32539758acf18a5460
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,73,8,2,1,3,1,3,1,3,1,3,3,3,79,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,4,4,90,8,4,11,4,12,4,91,3,4,94,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,102,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        112,8,6,1,7,1,7,4,7,116,8,7,11,7,12,7,117,1,7,1,7,1,7,1,7,1,7,1,
        7,4,7,126,8,7,11,7,12,7,127,1,7,1,7,1,7,1,7,3,7,134,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
<<<<<<< HEAD
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,162,8,8,1,9,1,9,5,9,166,8,9,
        10,9,12,9,169,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,
        10,180,8,10,10,10,12,10,183,9,10,1,10,1,10,1,10,1,10,1,10,3,10,190,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,198,8,11,11,11,12,11,199,
        1,11,1,11,1,11,1,11,1,11,3,11,207,8,11,1,12,1,12,1,12,1,12,5,12,
        213,8,12,10,12,12,12,216,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,
        1,14,5,14,226,8,14,10,14,12,14,229,9,14,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,245,8,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,3,16,254,8,16,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,266,8,17,1,18,1,18,1,18,1,18,
        5,18,272,8,18,10,18,12,18,275,9,18,1,18,1,18,1,18,1,19,1,19,5,19,
        282,8,19,10,19,12,19,285,9,19,1,20,1,20,1,20,1,20,1,21,1,21,4,21,
        293,8,21,11,21,12,21,294,1,21,1,21,1,22,1,22,1,22,1,22,5,22,303,
        8,22,10,22,12,22,306,9,22,1,22,1,22,1,22,1,23,4,23,312,8,23,11,23,
        12,23,313,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,36,39,344,0,51,1,0,0,
        0,2,57,1,0,0,0,4,72,1,0,0,0,6,78,1,0,0,0,8,93,1,0,0,0,10,101,1,0,
        0,0,12,111,1,0,0,0,14,133,1,0,0,0,16,161,1,0,0,0,18,163,1,0,0,0,
        20,170,1,0,0,0,22,191,1,0,0,0,24,208,1,0,0,0,26,220,1,0,0,0,28,223,
        1,0,0,0,30,230,1,0,0,0,32,253,1,0,0,0,34,265,1,0,0,0,36,267,1,0,
        0,0,38,279,1,0,0,0,40,286,1,0,0,0,42,290,1,0,0,0,44,298,1,0,0,0,
        46,311,1,0,0,0,48,315,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,
        56,1,1,0,0,0,57,58,5,1,0,0,58,59,3,4,2,0,59,60,5,2,0,0,60,3,1,0,
        0,0,61,73,3,8,4,0,62,73,3,10,5,0,63,73,3,30,15,0,64,73,3,36,18,0,
        65,73,3,40,20,0,66,73,3,32,16,0,67,73,3,6,3,0,68,73,3,24,12,0,69,
        73,3,26,13,0,70,73,3,46,23,0,71,73,3,28,14,0,72,61,1,0,0,0,72,62,
        1,0,0,0,72,63,1,0,0,0,72,64,1,0,0,0,72,65,1,0,0,0,72,66,1,0,0,0,
        72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,
        0,0,0,73,5,1,0,0,0,74,75,5,3,0,0,75,79,5,40,0,0,76,77,5,4,0,0,77,
        79,5,40,0,0,78,74,1,0,0,0,78,76,1,0,0,0,79,7,1,0,0,0,80,81,5,5,0,
        0,81,82,5,40,0,0,82,94,3,10,5,0,83,89,5,5,0,0,84,85,5,1,0,0,85,86,
        5,40,0,0,86,87,3,10,5,0,87,88,5,2,0,0,88,90,1,0,0,0,89,84,1,0,0,
        0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,80,
        1,0,0,0,93,83,1,0,0,0,94,9,1,0,0,0,95,102,3,48,24,0,96,102,5,40,
        0,0,97,98,5,1,0,0,98,99,3,12,6,0,99,100,5,2,0,0,100,102,1,0,0,0,
        101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,102,11,1,0,0,0,103,
        112,3,14,7,0,104,112,3,16,8,0,105,112,3,18,9,0,106,112,3,28,14,0,
        107,112,3,20,10,0,108,112,3,22,11,0,109,112,3,38,19,0,110,112,3,
        34,17,0,111,103,1,0,0,0,111,104,1,0,0,0,111,105,1,0,0,0,111,106,
        1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,110,
        1,0,0,0,112,13,1,0,0,0,113,115,5,6,0,0,114,116,3,10,5,0,115,114,
        1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,134,
        1,0,0,0,119,120,5,7,0,0,120,121,3,10,5,0,121,122,3,10,5,0,122,134,
        1,0,0,0,123,125,5,8,0,0,124,126,3,10,5,0,125,124,1,0,0,0,126,127,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,134,1,0,0,0,129,130,
        5,9,0,0,130,131,3,10,5,0,131,132,3,10,5,0,132,134,1,0,0,0,133,113,
        1,0,0,0,133,119,1,0,0,0,133,123,1,0,0,0,133,129,1,0,0,0,134,15,1,
        0,0,0,135,136,5,10,0,0,136,137,3,10,5,0,137,138,3,10,5,0,138,162,
        1,0,0,0,139,140,5,11,0,0,140,141,3,10,5,0,141,142,3,10,5,0,142,162,
        1,0,0,0,143,144,5,12,0,0,144,145,3,10,5,0,145,146,3,10,5,0,146,162,
        1,0,0,0,147,148,5,13,0,0,148,149,3,10,5,0,149,150,3,10,5,0,150,162,
        1,0,0,0,151,152,5,14,0,0,152,153,3,10,5,0,153,154,3,10,5,0,154,162,
        1,0,0,0,155,156,5,15,0,0,156,157,3,10,5,0,157,158,3,10,5,0,158,162,
        1,0,0,0,159,160,5,16,0,0,160,162,3,10,5,0,161,135,1,0,0,0,161,139,
        1,0,0,0,161,143,1,0,0,0,161,147,1,0,0,0,161,151,1,0,0,0,161,155,
        1,0,0,0,161,159,1,0,0,0,162,17,1,0,0,0,163,167,5,17,0,0,164,166,
        3,10,5,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,
        1,0,0,0,168,19,1,0,0,0,169,167,1,0,0,0,170,171,5,18,0,0,171,172,
        3,10,5,0,172,181,3,2,1,0,173,174,5,1,0,0,174,175,5,19,0,0,175,176,
        3,10,5,0,176,177,3,2,1,0,177,178,5,2,0,0,178,180,1,0,0,0,179,173,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,189,
        1,0,0,0,183,181,1,0,0,0,184,185,5,1,0,0,185,186,5,20,0,0,186,187,
        3,2,1,0,187,188,5,2,0,0,188,190,1,0,0,0,189,184,1,0,0,0,189,190,
        1,0,0,0,190,21,1,0,0,0,191,197,5,21,0,0,192,193,5,1,0,0,193,194,
        3,10,5,0,194,195,3,2,1,0,195,196,5,2,0,0,196,198,1,0,0,0,197,192,
        1,0,0,0,198,199,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,206,
        1,0,0,0,201,202,5,1,0,0,202,203,5,22,0,0,203,204,3,2,1,0,204,205,
        5,2,0,0,205,207,1,0,0,0,206,201,1,0,0,0,206,207,1,0,0,0,207,23,1,
        0,0,0,208,209,5,23,0,0,209,210,5,40,0,0,210,214,5,1,0,0,211,213,
        5,40,0,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,
        1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,2,0,0,218,219,
        3,46,23,0,219,25,1,0,0,0,220,221,5,24,0,0,221,222,3,10,5,0,222,27,
        1,0,0,0,223,227,5,40,0,0,224,226,3,10,5,0,225,224,1,0,0,0,226,229,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,29,1,0,0,0,229,227,1,
        0,0,0,230,231,5,25,0,0,231,232,3,10,5,0,232,31,1,0,0,0,233,234,5,
        26,0,0,234,235,3,10,5,0,235,236,3,46,23,0,236,254,1,0,0,0,237,238,
        5,27,0,0,238,239,5,40,0,0,239,240,5,28,0,0,240,241,5,1,0,0,241,242,
        3,10,5,0,242,244,3,10,5,0,243,245,3,10,5,0,244,243,1,0,0,0,244,245,
        1,0,0,0,245,246,1,0,0,0,246,247,5,2,0,0,247,248,3,46,23,0,248,254,
        1,0,0,0,249,250,5,29,0,0,250,251,3,10,5,0,251,252,3,46,23,0,252,
        254,1,0,0,0,253,233,1,0,0,0,253,237,1,0,0,0,253,249,1,0,0,0,254,
        33,1,0,0,0,255,256,5,30,0,0,256,266,3,10,5,0,257,258,5,31,0,0,258,
        266,3,10,5,0,259,260,5,32,0,0,260,261,3,10,5,0,261,262,3,10,5,0,
        262,266,1,0,0,0,263,264,5,33,0,0,264,266,3,10,5,0,265,255,1,0,0,
        0,265,257,1,0,0,0,265,259,1,0,0,0,265,263,1,0,0,0,266,35,1,0,0,0,
        267,268,5,34,0,0,268,269,5,40,0,0,269,273,5,1,0,0,270,272,5,40,0,
        0,271,270,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,
        0,274,276,1,0,0,0,275,273,1,0,0,0,276,277,5,2,0,0,277,278,3,46,23,
        0,278,37,1,0,0,0,279,283,5,40,0,0,280,282,3,10,5,0,281,280,1,0,0,
        0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,39,1,0,0,0,
        285,283,1,0,0,0,286,287,5,35,0,0,287,288,5,40,0,0,288,289,3,42,21,
        0,289,41,1,0,0,0,290,292,5,1,0,0,291,293,3,44,22,0,292,291,1,0,0,
        0,293,294,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,
        0,296,297,5,2,0,0,297,43,1,0,0,0,298,299,5,23,0,0,299,300,5,40,0,
        0,300,304,5,1,0,0,301,303,5,40,0,0,302,301,1,0,0,0,303,306,1,0,0,
        0,304,302,1,0,0,0,304,305,1,0,0,0,305,307,1,0,0,0,306,304,1,0,0,
        0,307,308,5,2,0,0,308,309,3,46,23,0,309,45,1,0,0,0,310,312,3,2,1,
        0,311,310,1,0,0,0,312,313,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,
        0,314,47,1,0,0,0,315,316,7,0,0,0,316,49,1,0,0,0,26,53,72,78,91,93,
        101,111,117,127,133,161,167,181,189,199,206,214,227,244,253,265,
        273,283,294,304,313
=======
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,161,8,8,1,9,1,9,5,9,165,8,9,10,9,
        12,9,168,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,179,
        8,10,10,10,12,10,182,9,10,1,10,1,10,1,10,1,10,1,10,3,10,189,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,4,11,197,8,11,11,11,12,11,198,1,11,
        1,11,1,11,1,11,1,11,3,11,206,8,11,1,12,1,12,1,12,1,12,5,12,212,8,
        12,10,12,12,12,215,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,
        5,14,225,8,14,10,14,12,14,228,9,14,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,244,8,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,253,8,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,265,8,17,1,18,1,18,1,18,1,18,5,18,
        271,8,18,10,18,12,18,274,9,18,1,18,1,18,1,18,1,19,1,19,5,19,281,
        8,19,10,19,12,19,284,9,19,1,20,1,20,1,20,1,20,1,21,1,21,4,21,292,
        8,21,11,21,12,21,293,1,21,1,21,1,22,1,22,1,22,1,22,5,22,302,8,22,
        10,22,12,22,305,9,22,1,22,1,22,1,22,1,23,4,23,311,8,23,11,23,12,
        23,312,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,36,39,342,0,51,1,0,0,0,
        2,57,1,0,0,0,4,71,1,0,0,0,6,77,1,0,0,0,8,92,1,0,0,0,10,100,1,0,0,
        0,12,110,1,0,0,0,14,132,1,0,0,0,16,160,1,0,0,0,18,162,1,0,0,0,20,
        169,1,0,0,0,22,190,1,0,0,0,24,207,1,0,0,0,26,219,1,0,0,0,28,222,
        1,0,0,0,30,229,1,0,0,0,32,252,1,0,0,0,34,264,1,0,0,0,36,266,1,0,
        0,0,38,278,1,0,0,0,40,285,1,0,0,0,42,289,1,0,0,0,44,297,1,0,0,0,
        46,310,1,0,0,0,48,314,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,
        56,1,1,0,0,0,57,58,5,1,0,0,58,59,3,4,2,0,59,60,5,2,0,0,60,3,1,0,
        0,0,61,72,3,8,4,0,62,72,3,10,5,0,63,72,3,30,15,0,64,72,3,36,18,0,
        65,72,3,40,20,0,66,72,3,32,16,0,67,72,3,6,3,0,68,72,3,24,12,0,69,
        72,3,26,13,0,70,72,3,46,23,0,71,61,1,0,0,0,71,62,1,0,0,0,71,63,1,
        0,0,0,71,64,1,0,0,0,71,65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,
        68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,5,1,0,0,0,73,74,5,3,0,
        0,74,78,5,40,0,0,75,76,5,4,0,0,76,78,5,40,0,0,77,73,1,0,0,0,77,75,
        1,0,0,0,78,7,1,0,0,0,79,80,5,5,0,0,80,81,5,40,0,0,81,93,3,10,5,0,
        82,88,5,5,0,0,83,84,5,1,0,0,84,85,5,40,0,0,85,86,3,10,5,0,86,87,
        5,2,0,0,87,89,1,0,0,0,88,83,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,
        90,91,1,0,0,0,91,93,1,0,0,0,92,79,1,0,0,0,92,82,1,0,0,0,93,9,1,0,
        0,0,94,101,3,48,24,0,95,101,5,40,0,0,96,97,5,1,0,0,97,98,3,12,6,
        0,98,99,5,2,0,0,99,101,1,0,0,0,100,94,1,0,0,0,100,95,1,0,0,0,100,
        96,1,0,0,0,101,11,1,0,0,0,102,111,3,14,7,0,103,111,3,16,8,0,104,
        111,3,18,9,0,105,111,3,28,14,0,106,111,3,20,10,0,107,111,3,22,11,
        0,108,111,3,38,19,0,109,111,3,34,17,0,110,102,1,0,0,0,110,103,1,
        0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,110,107,1,
        0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,13,1,0,0,0,112,114,5,6,
        0,0,113,115,3,10,5,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,
        0,0,116,117,1,0,0,0,117,133,1,0,0,0,118,119,5,7,0,0,119,120,3,10,
        5,0,120,121,3,10,5,0,121,133,1,0,0,0,122,124,5,8,0,0,123,125,3,10,
        5,0,124,123,1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,
        0,0,127,133,1,0,0,0,128,129,5,9,0,0,129,130,3,10,5,0,130,131,3,10,
        5,0,131,133,1,0,0,0,132,112,1,0,0,0,132,118,1,0,0,0,132,122,1,0,
        0,0,132,128,1,0,0,0,133,15,1,0,0,0,134,135,5,10,0,0,135,136,3,10,
        5,0,136,137,3,10,5,0,137,161,1,0,0,0,138,139,5,11,0,0,139,140,3,
        10,5,0,140,141,3,10,5,0,141,161,1,0,0,0,142,143,5,12,0,0,143,144,
        3,10,5,0,144,145,3,10,5,0,145,161,1,0,0,0,146,147,5,13,0,0,147,148,
        3,10,5,0,148,149,3,10,5,0,149,161,1,0,0,0,150,151,5,14,0,0,151,152,
        3,10,5,0,152,153,3,10,5,0,153,161,1,0,0,0,154,155,5,15,0,0,155,156,
        3,10,5,0,156,157,3,10,5,0,157,161,1,0,0,0,158,159,5,16,0,0,159,161,
        3,10,5,0,160,134,1,0,0,0,160,138,1,0,0,0,160,142,1,0,0,0,160,146,
        1,0,0,0,160,150,1,0,0,0,160,154,1,0,0,0,160,158,1,0,0,0,161,17,1,
        0,0,0,162,166,5,17,0,0,163,165,3,10,5,0,164,163,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,19,1,0,0,0,168,166,1,
        0,0,0,169,170,5,18,0,0,170,171,3,10,5,0,171,180,3,2,1,0,172,173,
        5,1,0,0,173,174,5,19,0,0,174,175,3,10,5,0,175,176,3,2,1,0,176,177,
        5,2,0,0,177,179,1,0,0,0,178,172,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,188,1,0,0,0,182,180,1,0,0,0,183,184,
        5,1,0,0,184,185,5,20,0,0,185,186,3,2,1,0,186,187,5,2,0,0,187,189,
        1,0,0,0,188,183,1,0,0,0,188,189,1,0,0,0,189,21,1,0,0,0,190,196,5,
        21,0,0,191,192,5,1,0,0,192,193,3,10,5,0,193,194,3,2,1,0,194,195,
        5,2,0,0,195,197,1,0,0,0,196,191,1,0,0,0,197,198,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,205,1,0,0,0,200,201,5,1,0,0,201,202,
        5,22,0,0,202,203,3,2,1,0,203,204,5,2,0,0,204,206,1,0,0,0,205,200,
        1,0,0,0,205,206,1,0,0,0,206,23,1,0,0,0,207,208,5,23,0,0,208,209,
        5,40,0,0,209,213,5,1,0,0,210,212,5,40,0,0,211,210,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,
        1,0,0,0,216,217,5,2,0,0,217,218,3,46,23,0,218,25,1,0,0,0,219,220,
        5,24,0,0,220,221,3,10,5,0,221,27,1,0,0,0,222,226,5,40,0,0,223,225,
        3,10,5,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,29,1,0,0,0,228,226,1,0,0,0,229,230,5,25,0,0,230,231,
        3,10,5,0,231,31,1,0,0,0,232,233,5,26,0,0,233,234,3,10,5,0,234,235,
        3,46,23,0,235,253,1,0,0,0,236,237,5,27,0,0,237,238,5,40,0,0,238,
        239,5,28,0,0,239,240,5,1,0,0,240,241,3,10,5,0,241,243,3,10,5,0,242,
        244,3,10,5,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,
        246,5,2,0,0,246,247,3,46,23,0,247,253,1,0,0,0,248,249,5,29,0,0,249,
        250,3,10,5,0,250,251,3,46,23,0,251,253,1,0,0,0,252,232,1,0,0,0,252,
        236,1,0,0,0,252,248,1,0,0,0,253,33,1,0,0,0,254,255,5,30,0,0,255,
        265,3,10,5,0,256,257,5,31,0,0,257,265,3,10,5,0,258,259,5,32,0,0,
        259,260,3,10,5,0,260,261,3,10,5,0,261,265,1,0,0,0,262,263,5,33,0,
        0,263,265,3,10,5,0,264,254,1,0,0,0,264,256,1,0,0,0,264,258,1,0,0,
        0,264,262,1,0,0,0,265,35,1,0,0,0,266,267,5,34,0,0,267,268,5,40,0,
        0,268,272,5,1,0,0,269,271,5,40,0,0,270,269,1,0,0,0,271,274,1,0,0,
        0,272,270,1,0,0,0,272,273,1,0,0,0,273,275,1,0,0,0,274,272,1,0,0,
        0,275,276,5,2,0,0,276,277,3,46,23,0,277,37,1,0,0,0,278,282,5,40,
        0,0,279,281,3,10,5,0,280,279,1,0,0,0,281,284,1,0,0,0,282,280,1,0,
        0,0,282,283,1,0,0,0,283,39,1,0,0,0,284,282,1,0,0,0,285,286,5,35,
        0,0,286,287,5,40,0,0,287,288,3,42,21,0,288,41,1,0,0,0,289,291,5,
        1,0,0,290,292,3,44,22,0,291,290,1,0,0,0,292,293,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,0,295,296,5,2,0,0,296,43,1,
        0,0,0,297,298,5,23,0,0,298,299,5,40,0,0,299,303,5,1,0,0,300,302,
        5,40,0,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,307,5,2,0,0,307,308,
        3,46,23,0,308,45,1,0,0,0,309,311,3,2,1,0,310,309,1,0,0,0,311,312,
        1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,47,1,0,0,0,314,315,7,
        0,0,0,315,49,1,0,0,0,26,53,71,77,90,92,100,110,116,126,132,160,166,
        180,188,198,205,213,226,243,252,264,272,282,293,303,312
>>>>>>> 999756586236c54f54652a32539758acf18a5460
    ]

class OnionParser ( Parser ):

    grammarFileName = "Onion.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'inc'", "'dec'", "'let'", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'not'", "'list'", "'if'", "'elif'", 
                     "'else'", "'cond'", "'t'", "'def'", "'return'", "'print'", 
                     "'repeat'", "'loop'", "'range'", "'while'", "'head'", 
                     "'tail'", "'getid'", "'sizeof'", "'macro'", "'class'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "INT", "FLOAT", "STRING", "IDENTIFIER", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementType = 2
    RULE_incDecStmt = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_compoundExpr = 6
    RULE_arithmeticExpr = 7
    RULE_booleanExpr = 8
    RULE_listExpr = 9
    RULE_ifExpr = 10
    RULE_branchExpr = 11
    RULE_functionDef = 12
    RULE_returnStmt = 13
    RULE_functionCall = 14
    RULE_printStatement = 15
    RULE_loopStatement = 16
    RULE_listOpExpr = 17
    RULE_macroDef = 18
    RULE_macroCall = 19
    RULE_classDef = 20
    RULE_classBody = 21
    RULE_methodDef = 22
    RULE_block = 23
    RULE_literal = 24

    ruleNames =  [ "program", "statement", "statementType", "incDecStmt", 
                   "assignment", "expression", "compoundExpr", "arithmeticExpr", 
                   "booleanExpr", "listExpr", "ifExpr", "branchExpr", "functionDef", 
                   "returnStmt", "functionCall", "printStatement", "loopStatement", 
                   "listOpExpr", "macroDef", "macroCall", "classDef", "classBody", 
                   "methodDef", "block", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    BOOL=36
    INT=37
    FLOAT=38
    STRING=39
    IDENTIFIER=40
    WS=41
    COMMENT=42
    LINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OnionParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OnionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.statement()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 55
            self.match(OnionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementType(self):
            return self.getTypedRuleContext(OnionParser.StatementTypeContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OnionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(OnionParser.T__0)
            self.state = 58
            self.statementType()
            self.state = 59
            self.match(OnionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(OnionParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(OnionParser.PrintStatementContext,0)


        def macroDef(self):
            return self.getTypedRuleContext(OnionParser.MacroDefContext,0)


        def classDef(self):
            return self.getTypedRuleContext(OnionParser.ClassDefContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(OnionParser.LoopStatementContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(OnionParser.IncDecStmtContext,0)


        def functionDef(self):
            return self.getTypedRuleContext(OnionParser.FunctionDefContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(OnionParser.ReturnStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(OnionParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_statementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementType" ):
                listener.enterStatementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementType" ):
                listener.exitStatementType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementType" ):
                return visitor.visitStatementType(self)
            else:
                return visitor.visitChildren(self)




    def statementType(self):

        localctx = OnionParser.StatementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementType)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.printStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.macroDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.classDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.loopStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.incDecStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.functionDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.returnStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 70
                self.block()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 71
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecStmt" ):
                return visitor.visitIncDecStmt(self)
            else:
                return visitor.visitChildren(self)




    def incDecStmt(self):

        localctx = OnionParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_incDecStmt)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(OnionParser.T__2)
                self.state = 75
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(OnionParser.T__3)
                self.state = 77
                self.match(OnionParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = OnionParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(OnionParser.T__4)
                self.state = 81
                self.match(OnionParser.IDENTIFIER)
                self.state = 82
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(OnionParser.T__4)
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 84
                    self.match(OnionParser.T__0)
                    self.state = 85
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 86
                    self.expression()
                    self.state = 87
                    self.match(OnionParser.T__1)
                    self.state = 91 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(OnionParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def compoundExpr(self):
            return self.getTypedRuleContext(OnionParser.CompoundExprContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OnionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(OnionParser.T__0)
                self.state = 98
                self.compoundExpr()
                self.state = 99
                self.match(OnionParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpr(self):
            return self.getTypedRuleContext(OnionParser.ArithmeticExprContext,0)


        def booleanExpr(self):
            return self.getTypedRuleContext(OnionParser.BooleanExprContext,0)


        def listExpr(self):
            return self.getTypedRuleContext(OnionParser.ListExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(OnionParser.FunctionCallContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(OnionParser.IfExprContext,0)


        def branchExpr(self):
            return self.getTypedRuleContext(OnionParser.BranchExprContext,0)


        def macroCall(self):
            return self.getTypedRuleContext(OnionParser.MacroCallContext,0)


        def listOpExpr(self):
            return self.getTypedRuleContext(OnionParser.ListOpExprContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_compoundExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundExpr" ):
                listener.enterCompoundExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundExpr" ):
                listener.exitCompoundExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundExpr" ):
                return visitor.visitCompoundExpr(self)
            else:
                return visitor.visitChildren(self)




    def compoundExpr(self):

        localctx = OnionParser.CompoundExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compoundExpr)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.arithmeticExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.booleanExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.listExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.ifExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.branchExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 109
                self.macroCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 110
                self.listOpExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_arithmeticExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticExpr(self):

        localctx = OnionParser.ArithmeticExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arithmeticExpr)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(OnionParser.T__5)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.expression()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(OnionParser.T__6)
                self.state = 120
                self.expression()
                self.state = 121
                self.expression()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(OnionParser.T__7)
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 124
                    self.expression()
                    self.state = 127 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.match(OnionParser.T__8)
                self.state = 130
                self.expression()
                self.state = 131
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_booleanExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpr(self):

        localctx = OnionParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_booleanExpr)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(OnionParser.T__9)
                self.state = 136
                self.expression()
                self.state = 137
                self.expression()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(OnionParser.T__10)
                self.state = 140
                self.expression()
                self.state = 141
                self.expression()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(OnionParser.T__11)
                self.state = 144
                self.expression()
                self.state = 145
                self.expression()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(OnionParser.T__12)
                self.state = 148
                self.expression()
                self.state = 149
                self.expression()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.match(OnionParser.T__13)
                self.state = 152
                self.expression()
                self.state = 153
                self.expression()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.match(OnionParser.T__14)
                self.state = 156
                self.expression()
                self.state = 157
                self.expression()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 159
                self.match(OnionParser.T__15)
                self.state = 160
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_listExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)




    def listExpr(self):

        localctx = OnionParser.ListExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(OnionParser.T__16)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 164
                self.expression()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = OnionParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(OnionParser.T__17)
            self.state = 171
            self.expression()
            self.state = 172
            self.statement()
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.match(OnionParser.T__0)
                    self.state = 174
                    self.match(OnionParser.T__18)
                    self.state = 175
                    self.expression()
                    self.state = 176
                    self.statement()
                    self.state = 177
                    self.match(OnionParser.T__1) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 184
                self.match(OnionParser.T__0)
                self.state = 185
                self.match(OnionParser.T__19)
                self.state = 186
                self.statement()
                self.state = 187
                self.match(OnionParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_branchExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranchExpr" ):
                listener.enterBranchExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranchExpr" ):
                listener.exitBranchExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranchExpr" ):
                return visitor.visitBranchExpr(self)
            else:
                return visitor.visitChildren(self)




    def branchExpr(self):

        localctx = OnionParser.BranchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_branchExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(OnionParser.T__20)
            self.state = 197 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 192
                    self.match(OnionParser.T__0)
                    self.state = 193
                    self.expression()
                    self.state = 194
                    self.statement()
                    self.state = 195
                    self.match(OnionParser.T__1)

                else:
                    raise NoViableAltException(self)
                self.state = 199 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 201
                self.match(OnionParser.T__0)
                self.state = 202
                self.match(OnionParser.T__21)
                self.state = 203
                self.statement()
                self.state = 204
                self.match(OnionParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = OnionParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(OnionParser.T__22)
            self.state = 209
            self.match(OnionParser.IDENTIFIER)
            self.state = 210
            self.match(OnionParser.T__0)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 211
                self.match(OnionParser.IDENTIFIER)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self.match(OnionParser.T__1)
            self.state = 218
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = OnionParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(OnionParser.T__23)
            self.state = 221
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = OnionParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(OnionParser.IDENTIFIER)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 224
                self.expression()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = OnionParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(OnionParser.T__24)
            self.state = 231
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = OnionParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(OnionParser.T__25)
                self.state = 234
                self.expression()
                self.state = 235
                self.block()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(OnionParser.T__26)
                self.state = 238
                self.match(OnionParser.IDENTIFIER)
                self.state = 239
                self.match(OnionParser.T__27)
                self.state = 240
                self.match(OnionParser.T__0)
                self.state = 241
                self.expression()
                self.state = 242
                self.expression()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                    self.state = 243
                    self.expression()


                self.state = 246
                self.match(OnionParser.T__1)
                self.state = 247
                self.block()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(OnionParser.T__28)
                self.state = 250
                self.expression()
                self.state = 251
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_listOpExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListOpExpr" ):
                listener.enterListOpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListOpExpr" ):
                listener.exitListOpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOpExpr" ):
                return visitor.visitListOpExpr(self)
            else:
                return visitor.visitChildren(self)




    def listOpExpr(self):

        localctx = OnionParser.ListOpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_listOpExpr)
        try:
<<<<<<< HEAD
            self.state = 265
=======
            self.state = 264
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(OnionParser.T__29)
<<<<<<< HEAD
                self.state = 256
=======
                self.state = 255
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self.expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< HEAD
                self.state = 257
                self.match(OnionParser.T__30)
                self.state = 258
=======
                self.state = 256
                self.match(OnionParser.T__30)
                self.state = 257
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self.expression()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
<<<<<<< HEAD
                self.state = 259
                self.match(OnionParser.T__31)
                self.state = 260
                self.expression()
                self.state = 261
=======
                self.state = 258
                self.match(OnionParser.T__31)
                self.state = 259
                self.expression()
                self.state = 260
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self.expression()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
<<<<<<< HEAD
                self.state = 263
                self.match(OnionParser.T__32)
                self.state = 264
=======
                self.state = 262
                self.match(OnionParser.T__32)
                self.state = 263
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_macroDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroDef" ):
                listener.enterMacroDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroDef" ):
                listener.exitMacroDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroDef" ):
                return visitor.visitMacroDef(self)
            else:
                return visitor.visitChildren(self)




    def macroDef(self):

        localctx = OnionParser.MacroDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_macroDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 267
            self.match(OnionParser.T__33)
            self.state = 268
            self.match(OnionParser.IDENTIFIER)
            self.state = 269
            self.match(OnionParser.T__0)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 270
                self.match(OnionParser.IDENTIFIER)
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.match(OnionParser.T__1)
            self.state = 277
=======
            self.state = 266
            self.match(OnionParser.T__33)
            self.state = 267
            self.match(OnionParser.IDENTIFIER)
            self.state = 268
            self.match(OnionParser.T__0)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 269
                self.match(OnionParser.IDENTIFIER)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self.match(OnionParser.T__1)
            self.state = 276
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_macroCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroCall" ):
                listener.enterMacroCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroCall" ):
                listener.exitMacroCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroCall" ):
                return visitor.visitMacroCall(self)
            else:
                return visitor.visitChildren(self)




    def macroCall(self):

        localctx = OnionParser.MacroCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macroCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 279
            self.match(OnionParser.IDENTIFIER)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 280
                self.expression()
                self.state = 285
=======
            self.state = 278
            self.match(OnionParser.IDENTIFIER)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 279
                self.expression()
                self.state = 284
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def classBody(self):
            return self.getTypedRuleContext(OnionParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDef" ):
                return visitor.visitClassDef(self)
            else:
                return visitor.visitChildren(self)




    def classDef(self):

        localctx = OnionParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_classDef)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 286
            self.match(OnionParser.T__34)
            self.state = 287
            self.match(OnionParser.IDENTIFIER)
            self.state = 288
=======
            self.state = 285
            self.match(OnionParser.T__34)
            self.state = 286
            self.match(OnionParser.IDENTIFIER)
            self.state = 287
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.MethodDefContext)
            else:
                return self.getTypedRuleContext(OnionParser.MethodDefContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = OnionParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 290
            self.match(OnionParser.T__0)
            self.state = 292 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 291
                self.methodDef()
                self.state = 294 
=======
            self.state = 289
            self.match(OnionParser.T__0)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 290
                self.methodDef()
                self.state = 293 
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

<<<<<<< HEAD
            self.state = 296
=======
            self.state = 295
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            self.match(OnionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_methodDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDef" ):
                listener.enterMethodDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDef" ):
                listener.exitMethodDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDef" ):
                return visitor.visitMethodDef(self)
            else:
                return visitor.visitChildren(self)




    def methodDef(self):

        localctx = OnionParser.MethodDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_methodDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 298
            self.match(OnionParser.T__22)
            self.state = 299
            self.match(OnionParser.IDENTIFIER)
            self.state = 300
            self.match(OnionParser.T__0)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 301
                self.match(OnionParser.IDENTIFIER)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
            self.match(OnionParser.T__1)
            self.state = 308
=======
            self.state = 297
            self.match(OnionParser.T__22)
            self.state = 298
            self.match(OnionParser.IDENTIFIER)
            self.state = 299
            self.match(OnionParser.T__0)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 300
                self.match(OnionParser.IDENTIFIER)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(OnionParser.T__1)
            self.state = 307
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = OnionParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 311 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 310
                self.statement()
                self.state = 313 
=======
            self.state = 310 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 309
                self.statement()
                self.state = 312 
>>>>>>> 999756586236c54f54652a32539758acf18a5460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(OnionParser.INT, 0)

        def FLOAT(self):
            return self.getToken(OnionParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(OnionParser.BOOL, 0)

        def STRING(self):
            return self.getToken(OnionParser.STRING, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = OnionParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< HEAD
            self.state = 315
=======
            self.state = 314
>>>>>>> 999756586236c54f54652a32539758acf18a5460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





