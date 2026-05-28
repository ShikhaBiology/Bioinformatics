sequence1 = "ATGCTAGCTAGCTAACG"
sequence2 = "ATGCTGGCTAGCTTACG"

for i in range(len(sequence1)):

    if sequence1[i] != sequence2[i]:

        print(f"Position {i+1}: {sequence1[i]} → {sequence2[i]}")
