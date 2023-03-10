import ar
frequency_table = {"K": 2,"i": 3,"r": 1,"t": 4, "i": 5}
AE = ar.ArithmeticEncoding(frequency_table)
original_msg = "Kirti"
print("Original Message: {msg}".format(msg=original_msg))
encoder, encoded_msg = AE.encode(msg=original_msg,
                    probability_table=AE.probability_table)
print("Encoded Message: {msg}".format(msg=encoded_msg))
decoder, decoded_msg = AE.decode(encoded_msg=encoded_msg,
msg_length=len(original_msg),probability_table=AE.probability_table)
print("Decoded Message: {msg}".format(msg=decoded_msg))
print("Message Decoded Successfully? -> {result}".format(result=original_msg == decoded_msg))
