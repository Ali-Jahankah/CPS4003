def display_leader(steps):
    for step in range(0,steps,1):
        print(f"""
              *****
              | {step+1} |""")
    return

def create_ladder():
    steps = int(input("How many steps left?  "))
    return display_leader(steps)

create_ladder()