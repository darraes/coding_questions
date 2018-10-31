# http://www.careercup.com/question?id=4892713614835712

def bit_sum(bit1, bit2, carry):
    if (bit1 == "0" and bit2 == "0"): return (carry, "0")
    if (bit1 == "1" and bit2 == "1"): return (carry, "1")
    else:
        if carry == "0": return ("1", "0")
        else: return ("0", "1")

def sum(bits1, bits2):
    carry = "0";
    result = ""

    if len(bits1) < len(bits2):
        bits1 = bits1.zfill(len(bits2))
    else:
        bits2 = bits2.zfill(len(bits1))

    for i in reversed(range(len(bits1))):
        tmp, carry = bit_sum(bits1[i], bits2[i], carry)
        result = tmp + result

    if carry > "0":
        result = "1" + result;

    return result;

##############   CALL         ########################

print sum("100011", "100100")