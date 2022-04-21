from sys import argv

script, user_name = argv

prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Can I asked you some questions {user_name}?")
print(f"Do you like me?")
like = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"""
Alight {user_name}, you have said {like} about liking me.  You live in {lives}. And you have a {computer} computer.  Very nice.
      """)