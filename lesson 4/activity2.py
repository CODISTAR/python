# taking total  amount from the frontend
amount=int(input("Enter the total  withdrawal amount: "))
#mentioning the diffrent notes available
note_1=amount//500
note_2=(amount%500)//200
note_3=(amount%500%200)//100


print("notes of five hundred rupees", note_1)
print("notes of two hundred rupees", note_2)
print("notes of hundred rupees", note_3)
