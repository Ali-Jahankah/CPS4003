print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
rows = int(input("\nHow many rows should I display? \n"))
columns = int(input("\nHow many columns should I display? \n"))
print("\nHere I go...\n")

for index in range(0,rows,1):
    for column_index in range(1,columns+1,1):
        if (column_index+1) % 2 == 0:
            print(" ❌ ",end='')
        else:
            print(" ☠️ ",end='')
    print('\n')





print('\nDone!')
