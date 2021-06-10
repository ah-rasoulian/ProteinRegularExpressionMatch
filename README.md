# ProteinRegularExpressionMatch

A program which gets a protein motif regular expression and several protein motifs. Then, checks whether each protein motif matches the regular expression or not.
It also, determines the positions of matches and mismatches using 1 and 0.

input example:

[AS]-D-[IVL]-G-X(4)-{PG}-C-[DE]-R-[FY](2)-Q<br>
4<br>
ATLGAVFALCDRYFQ<br>
WDVGPRSCFCDREYR<br>
ADWGRTQNRCDCYYQ<br>
ADIGQPHSLCERYFQ<br>

output:

Yes 101111111111111<br>
No 011111111111010<br>
Yes 110111111110111<br>
Yes 111111111111111<br>
