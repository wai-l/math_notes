# Bayes's theorem on probaility - expanded version

# a = actually having medical condition
a=0.01
# b = testing positive

# ba = P(B|A) - cnoditioanl probability where the person actualy has the medical condition when tested positive
ba = 0.95

# bna = P(B|not A) - probability where the person doesn't have the condition when tested positive (false positive)
bna = 0.02

# a_n = P(A') - prob of A does not occur
a_n = 1-a

# P(A|B) = P(B|A) * P(A) / (P(B|A) * P(A) + P(B|not A) * P(not A))

P_A_B = 0.95 * 0.01 / (0.95*0.01 + 0.02 * 0.99)

print(P_A_B)